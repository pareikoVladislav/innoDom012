# class A:
#     def method_A(self):
#         print("Method A")
#
#
# class B:
#     def method_B(self):
#         print("Method B")
#
#
# class C(A, B):
#     pass
#
#
# c = C()
#
# c.method_A()
# c.method_B()
from datetime import datetime

# class object()

# class A:
#     def func(self):
#         print("A class function")
#
#
# class B(A):
#     def func(self):
#         print("B class function")
#
#
# class C(A):
#     def func(self):
#         print("C class function")
#
#
# class D(B, C):
#     pass
#
#
# d = D()
#
# d.func()
#
# print(D.mro())


#   A
#  / \
# B   C
#  \ /
#   D


# class Transistor:
#     def signal(self):
#         print("Transistor Signal ON")
#
#
# class Screen(Transistor):
#     def display(self):
#         print("""
#         🌕🌕🌕🌕🌕
#         🌕🌕🌕🌕🌕
#         🌕🌕🌕🌕🌕
#         🌕🌕🌕🌕🌕
#         """)
#
#
# class Processor(Transistor):
#     def signal(self):
#         print("Processor signal ON")
#
#
# class Phone(Screen, Processor):
#     def switch_on(self):
#         self.signal()
#
#
# pineapple = Phone()
# pineapple.switch_on()
#
# print(Phone.mro())


# class O:
#     pass
#
#
# class A(O):
#     pass
#
#
# class B(O):
#     pass
#
#
# class C(A):
#     pass
#
#
# class D(B):
#     pass
#
#
# class E(C, D):  # E, C, A, D, B, O
#     pass
#
#
# print(E.mro())


# class Animal:
#     def set_health(self, health: int) -> None:
#         print(f"set {health} health to animal")
#
#
# class Carnivore(Animal):
#     def set_health(self, health: int) -> None:
#         Animal.set_health(self, health)
#         print(f"set {health} in carnivore")
#
#
# class Mammal(Animal):
#     def set_health(self, health: int) -> None:
#         Animal.set_health(self, health)
#         print(f"set {health} in mammal")
#
#
# class Dog(Mammal, Carnivore):
#     def set_health(self, health: int) -> None:
#         Mammal.set_health(self, health)
#         Carnivore.set_health(self, health)
#         print(f"set {health} in dog")
#
#
# fluffy = Dog()
#
# fluffy.set_health(150)


# class Animal:
#     def set_health(self, health: int) -> None:
#         print(f"set {health} health to animal")
#
#
# class Carnivore(Animal):
#     def set_health(self, health: int) -> None:
#         super().set_health(health)
#         print(f"set {health} in carnivore")
#
#
# class Mammal(Animal):
#     def set_health(self, health: int) -> None:
#         super().set_health(health)
#         print(f"set {health} in mammal")
#
#
# class Dog(Mammal, Carnivore):
#     def set_health(self, health: int) -> None:
#         super().set_health(health)
#         print(f"set {health} in dog")


# fluffy = Dog()

# fluffy.set_health(150)

# print(Dog.mro())
# print(Carnivore.mro())
# print(Mammal.mro())
# print(Animal.mro())

# def request_data_getter():
#     return "None"
#
#
# class Test:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.secret = request_data_getter()
#
#
# test = Test("Vlad", 26)
#
# Test.new_attribute = "new_attribute"
#
# print(test.new_attribute)
#
# print(Test.new_attribute)

# class LoggerMixin:
#     def log_action(self, action):
#         return f"{self.__class__.__name__}: {action}"
#
#
# class Employee(LoggerMixin):
#     def __init__(self, name, position):
#         self.name = name
#         self.position = position
#
#     def promote(self):
#         return self.log_action(f"{self.__class__.__name__} {self.name} was promoted to a higher position.")
#
#
# class Customer(LoggerMixin):
#     def __init__(self, name):
#         self.name = name
#
#     def make_purchase(self, item):
#         return self.log_action(f"{self.__class__.__name__} {self.name} purchased {item}")


# oleg = Employee("Oleg", "HR Manager")
# mike = Customer("Mike")
# logger = LoggerMixin()

# print(logger.log_action("Hello"))

# print(oleg.promote())
# print(mike.make_purchase("Laptop"))


# class SafetyMixin:
#     def eneble_alarm(self):
#         print("Alarm is enabled")
#
#     def enable_airbag(self):
#         print("Подушка безопасности активирована")
#
#     def disable_airbag(self):
#         print("Подушка безопасности деактивирована")
#
#     def fasten_seat_belt(self):
#         print("Ремень безопасности пристёгнут")
#
#
# class EntertainmentMixin:
#     def play_music(self, track):
#         print(f"Включена песня - {track}")
#
#     def play_video(self, video):
#         print(f"Включили видео {video}")
#
#
# class ClimateMixin:
#     def set_temperature(self, temp):
#         print(f"Была установлена '{temp}' температура")
#
#     def enable_air_conditioning(self):
#         print("Кондиционер включен")
#
#     def disable_air_conditioning(self):
#         print("Кондиционер выключен")
#
#
# class Car(SafetyMixin, EntertainmentMixin, ClimateMixin):
#     def __init__(self, brand, model, year, color):
#         self.brand = brand
#         self.model = model
#         self.year = year
#         self.color = color
#
#     def display_info(self):
#         return f"Машина {self.brand} - {self.model}. {self.year} года выпуска. Цвет: {self.color}"
#
#     def start_engine(self):
#         print("Двигатель заведен")
#
#     def stop_engine(self):
#         print("Двигатель заглушен")
#
#
# car = Car("BMW", "X5", 2010, "Черный")
#
# print(car.display_info())
# car.start_engine()
# car.enable_airbag()
# car.enable_air_conditioning()
# car.fasten_seat_belt()
# car.play_music("Track 1")
# car.play_video("Video 1")

from social_mixins import (
    AuthorMixin,
    ContentMixin,
    TimestampMixin
)


class Article(AuthorMixin, TimestampMixin, ContentMixin):
    def __init__(self):
        self.set_timestamp()


class Comment(AuthorMixin, TimestampMixin):
    def __init__(self):
        self.set_timestamp()


article = Article()
comment = Comment()

article.set_author("Vlad")
article.set_content("TEST CONTENT")
print(f"Автор статьи: {article.get_author()}")
print(f"Дата публикации: {article.get_timestamp()}")
print(f"Статья: {article.get_content()}")

print("=" * 55)

comment.set_author("Vlad")

print(f"Автор коммента: {comment.get_author()}")
print(f"Время публикации: {comment.get_timestamp()}")
