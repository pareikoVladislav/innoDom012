# from abc import ABC, abstractmethod
import time

# class Dish(ABC):
    # def __init__(self):
    #     pass
    #
    # def dynamic_method(self):
    #     pass
    #
    # staticmethod
    # def static_method():
    #     pass
    #
    # classmethod
    # def class_method(cls):
    #     pass

#     @abstractmethod
#     def create_dish(self):
#         pass
#
#     @abstractmethod
#     def update_dish_info(self):
#         pass
#
#     @abstractmethod
#     def set_dish_price(self):
#         pass
#
#     @abstractmethod
#     def get_dishes(self):
#         pass
#
#     @abstractmethod
#     def get_dish_by_name(self):
#         pass
#
#
# class Desert(Dish):
#     def __init__(self):
#         print("Desert")
#
#     def create_dish(self):
#         print("DESERT DISH")
#
#     def update_dish_info(self):
#         print("DESERT DISH")
#
#     def set_dish_price(self):
#         print("DESERT DISH")
#
#     def get_dishes(self):
#         print("DESERT DISH")
#
#     def get_dish_by_name(self):
#         print("DESERT DISH")
#
#
# desert = Desert()
#
# desert.create_dish()
# desert.update_dish_info()
# desert.set_dish_price()
# desert.get_dishes()
# desert.get_dish_by_name()


# class ManagerResource:
#     def __enter__(self):
#         name = input("Enter your name: ")
#         surname = input("Enter your surname: ")
#
#         print(f"Hello, {name} {surname[0]}. !")
#         return self
#
#     def __exit__(self, exc_type, exc_value, traceback):
#         print("Resource is being closed. Bye.")
#         if exc_type:
#             print(f"Exception found: {exc_type}, {exc_value}")
#             return True
#
#     def print_greeting(self):
#         print(f"Hello from the '{self.__class__.__name__}' class context!!!!")
#
#
# with ManagerResource() as custom_manager:
#
#     # отрабатывает enter
#     custom_manager.print_greeting()
#     raise ValueError("Our custom exception")

    # если ничего больше нет, то отрабатывает exit


# class FileManager:
#     def __init__(self, file_name, mode):
#         self.file_name = file_name
#         self.mode = mode
#
#     def __enter__(self):
#         self.file = open(self.file_name, self.mode)
#         return self.file
#
#     def __exit__(self, exc_type, exc_value, traceback):
#         self.file.close()
#
#
# with FileManager("context_test.txt", "w") as custom_file:
#     custom_file.write("HELLO!!!\n")


# class TimingDecorator:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):  # аналогично функции wrapper
#         start_time = time.time()
#         result = self.func(*args, **kwargs)
#         end_time = time.time()
#         print(f"Execution time: {end_time - start_time} seconds.")
#         return result


# class TimingDecorator:
#     def __init__(self, ttl, message):
#         self.ttl = ttl
#         self.message = message
#
#     def __call__(self, func):  # аналогично функции wrapper
#         def wrapper(*args, **kwargs):
#             start_time = time.time()
#             result = func(*args, **kwargs)
#             end_time = time.time()
#             print(f"{self.message}!!!\nExecution time: {end_time - start_time} seconds.")
#             return result
#         return wrapper
#
#
# @TimingDecorator(ttl=3, message="HELLO")
# def some_func(arg_1, arg_2):
#     time.sleep(3)
#     result = arg_1 ** arg_2
#
#     return result
#
#
# print(some_func(5, 5))


# class MyClass:
#     # __dict__ = {"self.name": name, "self.surname": surname}
#
#     __slots__ = ("id", "name", "surname", "email", "phone")
#
#     def __init__(self, user_id, name, surname, email, phone):
#         self.id = user_id
#         self.name = name
#         self.surname = surname
#         self.email = email
#         self.phone = phone
#
#
# test = MyClass(1, "Vlad", "Black", "test.email@gmail.com", "+789456123")
#
# test.deleted = None

# print(test.deleted)
# class TestClass:

    # def __init__(self, name):
    #     self.name = name


# test_class = TestClass("Vlad")

# print(test_class.name)
# test_class.surname = input()
# print(test_class.surname)


# print(TestClass.surname)

# class ParentWithSlots:
#     __slots__ = ("name",)
#
#
# class ChildWithSlots(ParentWithSlots):
#     __slots__ = ("age",)
#
#
# child = ChildWithSlots()  # __slots__ = ("age", "name")
#
# child.name = "Alice"
# child.age = 30
#
# print(child.name)
# print(child.age)

# child.new_attribute = "New!!!!"  # вызовет ошибку!!!


# class DBConnectionSingleton(object):
#     _instance = None
#
#     def __new__(cls):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#         return cls._instance
#
#
# first_instance = DBConnectionSingleton()
# second_instance = DBConnectionSingleton()
#
# print(first_instance is second_instance)


# class Database:
#     def connect(self):
#         pass
#
#     def cursor(self):
#         pass
#
#     def close(self):
#         pass
#
#
# class MySQL(Database):
#     def connect(self):
#         print("mysql connect!!")
#
#
# class Postgres(Database):
#     def connect(self):
#         print("postgres connect")
#
#
# class DBFactory:
#     def create_connection(self, db_type):
#         match db_type.strip().lower():
#             case "mysql":
#                 return MySQL()
#             case "postgres":
#                 return Postgres()
#             case _:
#                 return None
#
#
# factory = DBFactory()
# database = factory.create_connection("mysql")
# database.connect()


import copy


class Prototype:
    def clone(self):
        return copy.deepcopy(self)


class Laptop(Prototype):
    def __init__(self, name, details):
        self.name = name
        self.details = details


laptop_1 = Laptop("Lenovo", ["Model - Legion HlK7812"])
laptop_2 = laptop_1.clone()

laptop_2.details.append("Processor - Intel i9")


print(laptop_1.details)
print(laptop_2.details)








