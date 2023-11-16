class Notebook:
    def __init__(self, ram, memory, cpu):
        self.ram = ram
        self.memory = memory
        self.cpu = cpu

    def info(self):
        return f'Размер оперативной памяти:{self.ram},\n Размер внутренней памяти:{self.memory} \n Количество ядер в процессоре:{self.cpu}'
    
    @classmethod
    def add_notebook(cls, notebook_dict):
        ram = notebook_dict.get('ram', 0)
        memory = notebook_dict.get('memory', 0)
        cpu = notebook_dict.get('cpu', 0)
        return cls(ram, memory, cpu)
    
notebook_dict = {
    'ram': 12,
    'memory': 500,
    'cpu': 4
}

acer = Notebook.add_notebook(notebook_dict)
# print(notebook_instance.info())





class Person:
    def __init__(self, name, birth_year) -> None:
        self.name = name 
        self.birth_year = birth_year

class Student(Person):
    def __init__(self, name, birth_year, course, notebook):
        super().__init__(name, birth_year)
        self.course = course
        self.notebook = notebook
        self.__payments = []
        # print(self.notebook)

    def do_payment(self, amount):
        self.__payments.append(amount)

    def get_all_payment(self):
        return self.__payments
    
    def check_pc(self):
        print(self.notebook.ram)
        list_ = [self.notebook.ram >= 4, self.notebook.memory >= 120, self.notebook.cpu >= 2]
        return all(list_)
        # return True if self.notebook.ram >= 4 or self.notebook.memory >= 120 or self.notebook.cpu >= 2 else False
    
    def __str__(self) -> str:
        return f'Наш студент {self.name}, {self.birth_year} года рождения, учится а {self.course} у него ноутбук \n{self.notebook.info()}. \nЗа крус оплачивает'



john = Student('John', 2000, 'python', acer)
print(john)
john.do_payment(20000)
john.do_payment(50)
print(john.get_all_payment())
# print(john.check_pc())

