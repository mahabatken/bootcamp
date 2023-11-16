# mixins
# Миксины - классы которые используются для наследования и передачи
# дочерним классам определенных методов, но от них не создаются
# обьекты для чего :
#1 вы хотите предоставить множество доп методов для классов
#2 вы хотите использовать один конкретный метод во множестве
# разных классов

# class EndineMixin:
#     def start_engine(self):
#         print("start engine")

# class RadioMixin:
#     def play_radio(self):
#         print("mysic is playong")        

# class Avto(EngineMixin, RadioMixin):
#     pass

# class Plane(EngineMixin):
#     pass

# class Smartphone(EngineMixin):
#     pass

# class Train(EngineMixin):
#     pass


class FlyMixin:
    def fly(self):
        print("I cam fly!")


class WalkMixin:
    def walk(self):
        print("I cam walk!")


class SwimMixin:
    def swim(self):
        print("I cam swim!")                
class Human( WalkMixin,  SwimMixin):
    name = "human"

    def talk():
        print("I can talk!")


class Fish(SwimMixin):
    name = "fish"


class Volan(SwimMixin, FlyMixin):
    name = "volan" 


class Duck(SwimMixin, FlyMixin, WalkMixin):
    name = "duck"

obj = Human()
obj.walk()
obj.swim()    


    