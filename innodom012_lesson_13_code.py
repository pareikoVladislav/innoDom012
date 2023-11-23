# class Test:
#     x = 10
#
#     def __init__(self):
#         self.dynamic_attr = "Hello"
#
#     def dynamic_method(self):
#         # self.static_method()
#         pass
#
#     @staticmethod
#     def static_method(arg):
#         return Test.x
#         # return arg.dynamic_attr
#
#
# test = Test()
#
# test.static_method(test)


# class SuperClass:
#     some_static_arg = "HELLO FROM THE CLASS"
#
#     @classmethod
#     def get_static_argument_val(cls):
#         return cls.some_static_arg
#
#
# sup_class = SuperClass()
#
# print(f"Via class instance {sup_class.get_static_argument_val()}")
# print(f"Via class {SuperClass.get_static_argument_val()}")

# margherita_ingredients = {
#     "dought": 450,
#     "tomatoes sause": 150,
#     "mozzarella": 150,
#     "tomatoes": 140,
#     "oregano": 3,
#     "olive_oil": 10
# }
# prosciutto_ingredients = {
#     "dought": 400,
#     "tomatoes sause": 120,
#     "parmedjano": 100,
#     "olives": 30,
#     "oregano": 3,
#     "basil": 10,
#     "prosciutto": 250,
#     "olive_oil": 15
# }
#
#
# class Pizza:
#     def __init__(self, ingredients):
#         self.ingredients = ingredients
#
#     @classmethod
#     def margherita(cls):
#         return cls(margherita_ingredients)
#
#     @classmethod
#     def prosciutto(cls):
#         return cls(prosciutto_ingredients)
#
#     def show_ingredients(self):
#         for key, value in self.ingredients.items():
#             print(f"Ингредиент '{key}' - {value} граммов")
#
#         print(f"Общий вес = {sum(self.ingredients.values())}")
#
#
# margherita = Pizza.margherita()
# margherita.show_ingredients()
#
# print("=" * 100)
#
# prosciutto = Pizza.prosciutto()
# prosciutto.show_ingredients()


# class User:
#     active_users = 0
#
#     @classmethod
#     def display_active_users(cls):
#         return f"Active users: {cls.active_users}"
#
#     @classmethod
#     def from_sting(cls, string_data):
#         first_name, last_name, age = string_data.split(", ")
#         return cls(first_name, last_name, int(age))
#
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         User.active_users += 1
#
#     @staticmethod
#     def logout():
#         User.active_users -= 1
#
#
# user_data_from_string = input("Enter your, name, surname, age: ")
#
# User.from_sting(user_data_from_string)
# print(User.display_active_users())

# User() # -> __new__(), __init__()

# second_way_normal = User(
#     input("Enter your name: "),
#     input("Enter your surname: "),
#     int(input("Enter your age: "))
# )

# print(second_way_normal.display_active_users())

# first_way_from_string.logout()

# print(User.display_active_users())


# class Test:
#     x = 5
#
#
# test = Test()
#
# print(f"via class - {Test.x}")
# print(f"via class instance - {test.x}")
#
# Test.x = 15
#
# print(f"via class - {Test.x}")
# print(f"via class instance - {test.x}")
#
# test.x = 45
#
# print(f"via class - {Test.x}")
# print(f"via class instance - {test.x}")


# class Person:
#     class_obj_count = 0
#
#     def __init__(self, username):
#         self.name = username
#         Person.class_obj_count += 1
#         self.obj_creating_logger()
#
#     @classmethod
#     def obj_creating_logger(cls):
#         print(f"Created {cls.class_obj_count} instance(s) of {cls.__name__}")
#
#
# for i in range(1, 11):
#     Person(f"user_{i}")


# class DatabaseConnection:
#     instance = None
#
#     @classmethod
#     def get_instance(cls, db_name):
#         if cls.instance is None:
#             cls.instance = cls(db_name)
#         return cls.instance
#
#     def __init__(self, db_name):
#         self.db_name = db_name
#
#
# db_connection = DatabaseConnection.get_instance("my_database")
# db_connection_2 = DatabaseConnection.get_instance("my_database")
#
# print(db_connection is db_connection_2)
# print(id(db_connection))
# print(id(db_connection_2))

import sqlite3


# class Database:
#     _instance = None
#
#     def __init__(self):
#         self.connection = sqlite3.connect(':memory:')
#         self.cursor = self.connection.cursor()
#         # Инициализация базы данных, например, создание таблиц.
#
#     @classmethod
#     def get_instance(cls):
#         if cls._instance is None:
#             cls._instance = cls()
#         return cls._instance
#
#     def execute(self, query, params=None):
#         if params is None:
#             self.cursor.execute(query)
#         else:
#             self.cursor.execute(query, params)
#         return self.cursor
#
#     def commit(self):
#         self.connection.commit()
#
#     def close(self):
#         self.connection.close()
#
#
# db_instance1 = Database.get_instance()
# db_instance2 = Database.get_instance()
#
# print(f"Обе переменные ссылаются на один и тот же объект класса? - {db_instance1 is db_instance2}")
#
#
# def create_table_if_not_exists(table_name):
#     return f"CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY, data TEXT)"
#
#
# def insert_data_in_table(table_name, user_text):
#     return f"INSERT INTO {table_name} (data) VALUES (?)", (user_text,)
#
#
# def get_all_data_from_the_table(table_name):
#     return f"SELECT * FROM {table_name}"
#
#
# user_text = input("Enter some text: ")
#
# db_instance1.execute(create_table_if_not_exists("example"))
#
# query, params = insert_data_in_table("example", user_text)
# db_instance1.execute(query, params)
# db_instance1.commit()
#
# for row in db_instance2.execute(get_all_data_from_the_table("example")):
#     print(row)
# # HELLO FROM THE DATABASE IN MEMORY


# class Account:
#     def __init__(self, name, balance):
#         self._name = name  # Protected attribute
#         self.__balance = balance  # Private attribute
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             self.__update_balance()
#
#     def withdraw(self, amount):
#         if amount > 0 and amount <= self.__balance:
#             self.__balance -= amount
#             self.__update_balance()
#         else:
#             print("Недостаточно средств на счету")
#
#     def __update_balance(self):  # Private method
#         print(f"Баланс обновлен. Новый баланс: {self.__balance}")
#
#
# account = Account("VLad", 1000)
#
# account.deposit(550)
#
# account.withdraw(950)
#
# print(account._name)  # нельзя так делать
# print(account._Account__balance)  #  ВООБЩЕ НЕЛЬЗЯ!!!!!


# class User:
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password  # Здесь происходит вызов сеттера
#
#     @property
#     def password(self):
#         raise AttributeError("Password is not readable")  # делаем пароль недоступным для чтения
#
#     @password.setter
#     def password(self, value):
#         self._password = self._encrypt_password(value)  # Здесь шифруем пароль перед сохранением
#
#     def _encrypt_password(self, password):
#         return password[::-1]  # Простая "шифровка" путем реверса строки
#
#     def verify_password(self, password):
#         return self._password == self._encrypt_password(password)
#
#
# user = User("Dima", "k@kAsh8Chk@097")
#
# print(user.password)


class Publication:
    def __init__(self, title, rating):
        self.title = title
        self.rating = rating


class Author:
    def __init__(self, name):
        self.name = name
        self.publications = []

    def add_publication(self, publication):
        self.publications.append(publication)

    @property
    def rating(self):
        total_score = sum(pub.rating for pub in self.publications)
        result = round(total_score / len(self.publications) if self.publications else 0, 2)
        return result


author = Author("Daniel Kiz")

# print(author.rating)

author.add_publication(Publication("Some example Test_1", 4))
author.add_publication(Publication("Some example Test_2", 3))
author.add_publication(Publication("Some example Test_3", 5.5))
author.add_publication(Publication("Some example Test_4", 8))

print(author.rating)
# print(*author.publications)

for publication in author.publications:
    print(publication.title)
