# class Notebook:
#     def __init__(self, ram, memory, cpu):
#         self.ram = ram
#         self.memory = memory
#         self.cpu = cpu

#     def info(self):
#         return f'Размер оперативной памяти:{self.ram},\n Размер внутренней памяти:{self.memory} \n Количество ядер в процессоре:{self.cpu}'
    
#     @classmethod
#     def add_notebook(cls, notebook_dict):
#         ram = notebook_dict.get('ram', 0)
#         memory = notebook_dict.get('memory', 0)
#         cpu = notebook_dict.get('cpu', 0)
#         return cls(ram, memory, cpu)

# notebook_dict = {
#     'ram': 12,
#     'memory': 500,
#     'cpu': 4
# }

# notebook_instance = Notebook.add_notebook(notebook_dict)
# print(notebook_instance.info())