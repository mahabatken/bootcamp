class University:
    def __init__(self, university_name):
        self.name = university_name
        self.departments = {}

    def add_department(self, department_name):
     
        if department_name not in self.departments:
            self.departments[department_name] = []

class Student:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

def main():
    university = University("Мой университет")

    student1 = Student("Иван", "Иванов")
    student2 = Student("Петр", "Петров")
    student3 = Student("Мария", "Сидорова")

    university.add_department("Факультет физики")
    university.add_department("Факультет химии")
    university.add_department("Факультет истории")

  
    university.departments["Факультет физики"].append(student1)
    university.departments["Факультет физики"].append(student2)
    university.departments["Факультет химии"].append(student3)

# if __name__ == "__main__":
#     main()