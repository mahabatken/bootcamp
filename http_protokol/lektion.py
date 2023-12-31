# HTTP (HyperText Transfer Protocol)ПРОТОКОЛ ПЕРЕДАЧИ ГИПЕРТЕКСТОВОЙ ИНФОРМАЦИИ СТАЛ УНЕВЕРСАЛЬНЫМ СРЕДСТВОМ ВЗАИМОДЕЙСТВИЯ 
# МЕЖДУ УЗЛАМИ В WWW(ВСЕМИРНОЙ ПАУТИНЕ))
# КЛИЕНТ - СЕРВЕР(ЧЕЛ ДЕЛ ЗАППОС И СЕРВЕР)
# СТРУРТУРА НТТР
# 1 СТАРТОВАЯ СТРАКА (ЛИНИЯ) ОПРЕДЕЛЯЕТ КАКОЕ СООБЩЕНИЯ МЫ ПОЛУЧАЕМ
#      ЗАПРОС: GET/wiki/HTTPS HTTP/1.0 
# ответ : HTTP/1.0 200 OK
#         HTTP/1.0 404 Not Found
# 2.Заголовки(Headers)несколько строчек которых уточнаяют запрос лидо опысывают тело сообшнений
# HOST : wikipedia.org
# User- Agent
# header ={
#     'User-Agent':"Mozilla/5/0(X11; Linux x86_64)'

# }(это описания )
# 3 Тело сообшения (body)непосредственно данные запроса либо ответа{
#   'comment':'GOAT BEST!
# }
# методы запроса:-> 1 GET ( для получения данных)
#                   2 POST(для создания данных)
#                   3 PUT(для полного обновления)
#                   4 PATCH(для частичного обновления)
#                   5 DELETE(для удаления данных)
# СТАТУСЫ ответов:
# 1XX Информационные
# 2XX запрос так или иначе прошел успешно
# 3XX перепаправления
# 4XX Ошибка на стороне клиента
# 5XX Ошибка на стороне сервера

import json
import os
import psycopg2

class TodoItem:
    def __init__(self, description):
        self.description = description
        self.is_done = False

    def check(self):
        self.is_done = True

    def uncheck(self):
        self.is_done = False

class Todo:
    def __init__(self):
        self.todo_items = []

    def add_todo(self, todo_item):
        self.todo_items.append(todo_item)

    def list_items(self):
        for index, item in enumerate(self.todo_items):
            status = "Done" if item.is_done else "Not Done"
            print(f"{index + 1}. {item.description} - {status}")

    def find(self, word):
        found_items = [(index + 1, item) for index, item in enumerate(self.todo_items) if word.lower() in item.description.lower()]
        return found_items

    def save_to_file(self, filename="todo.json"):
        with open(filename, 'w') as file:
            data = {"todo_items": [{"description": item.description, "is_done": item.is_done} for item in self.todo_items]}
            json.dump(data, file)

    def load_from_file(self, filename="todo.json"):
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                data = json.load(file)
                self.todo_items = [TodoItem(item["description"]) for item in data["todo_items"]]
                for index, item in enumerate(data["todo_items"]):
                    if item["is_done"]:
                        self.todo_items[index].check()

    def save_to_postgres(self, dbname, user, password, host, port):
        conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
        cur = conn.cursor()

        cur.execute("CREATE TABLE IF NOT EXISTS todo_items (id SERIAL PRIMARY KEY, description VARCHAR, is_done BOOLEAN);")

        for item in self.todo_items:
            cur.execute("INSERT INTO todo_items (description, is_done) VALUES (%s, %s);", (item.description, item.is_done))

        conn.commit()
        cur.close()
        conn.close()

    def load_from_postgres(self, dbname, user, password, host, port):
        conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
        cur = conn.cursor()

        cur.execute("SELECT * FROM todo_items;")
        rows = cur.fetchall()

        self.todo_items = [TodoItem(row[1]) for row in rows]
        for index, row in enumerate(rows):
            if row[2]:
                self.todo_items[index].check()

        cur.close()
        conn.close()

    def run(self):
        menu = {
            "1": self.list_items,
            "2": self.find,
            "3": self.add_todo,
            "4": self.save_to_file,
            "5": self.load_from_file,
            "6": self.save_to_postgres,
            "7": self.load_from_postgres,
            "8": exit
        }

        while True:
            print("\nTodo App Menu:")
            print("1. List Items")
            print("2. Find Items")
            print("3. Add Todo")
            print("4. Save to File")
            print("5. Load from File")
            print("6. Save to PostgreSQL")
            print("7. Load from PostgreSQL")
            print("8. Exit")

            choice = input("Enter your choice: ")
            if choice in menu:
                if choice == "2":
                    word = input("Enter a word to search: ")
                    result = menu[choice](word)
                    for index, item in result:
                        print(f"{index}. {item.description}")
                elif choice in ["3", "4", "5", "6", "7"]:
                    menu[choice]()
                else:
                    menu[choice]()
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    todo_app = Todo()
    todo_app.run()
