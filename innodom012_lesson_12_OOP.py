from array import array

# a = 5
#
# print(a.__add__(5))  # a + 5
import time


# class TestClass:
#     new_number = 7
#     is_positive = True
#
#     def __init__(self, name: str):
#         self.name = name
#
#     def some_func(self):
#         return f"Hello, {self.name}!"  # TestClass.name
#
#
# test_obj = TestClass("Vladislav")
# new_obj = TestClass("Eugeniy")
#
# # test_obj.name = "Dmitriy"
#
# print(test_obj.name)
# print(test_obj.some_func())


# class Test:
#     def __init__(self):
#         print(f"Объект по классу '{self.__class__.__name__}' был успешно создан.")
#
#     def show_self(self):
#         return self


class Cat:
    paws = 4
    ears = 2
    eyes = 2
    tail = True

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.wool = True
        self.energy = 100
        self.sleep = False
        self.eyes = 4

    def say_meaw(self):
        print(f"your pet '{self.name}' say 'Mew'!!")

    def play(self, action):
        if self.energy > 20:
            match action:
                case "play_with_hand":
                    self.energy -= 15
                    return "Котяра расцарапал вам всю руку, троху устал, но он доволен."
                case "play_with_eat":
                    self.energy -= 10
                    return "Котеич нашёл шкурку от сосиски и устроил погром"
                case "night_nightmare":
                    return "У пушистой шавермы сново режим 'ТЫГЫДЫГ'"
                case _:
                    return "Котик не понимает во что играть"
        else:
            answer = "Пушистик устал и пшёл спать"
            print(answer)
            self.sleep = True
            time.sleep(7)
            self.sleep = False
            self.energy = 100
            full_charge = "Этот демонюка снова проснулся и готов к бою"
            return full_charge


class MyAwesomeClass(object):
    def __init__(self, name, age, status):
        self.name = name
        self.age = age
        self.status = status
        print("Я сделяль")

    def __str__(self):
        return str({
            "name": self.name,
            "age": self.age,
            "greeting": "Hello from the magic method 'str'",
            "status": self.status
        })

    def __repr__(self):
        return f"Привет из класса '{self.__class__.__name__}'"


# class MyClass:
#     def __init__(self, *args):
#         self.items = list(args)
#
#     def __len__(self):
#         return len(self.items)
#
#     def __getitem__(self, index):
#         return f"у кортежа элементов {self.items} по индексу {index} получено значение {self.items[index]}"
#
#     def __setitem__(self, key, value):
#         self.items[key] = value

# class StaticTest:
#     x = 1
#
#     @staticmethod
#     def static_method(name, surname):
#         return f"{name}.{surname}"
#
#
# test_1 = StaticTest()
#
# print(test_1.static_method("Vlad", "Black"))
# print(StaticTest.static_method("Andrew", "Green"))

# print(f"Via class instance - {test_1.x}")
# print(f"Via class - {StaticTest.x}")
# StaticTest.x = 3
# print("-" * 100)
# print(f"Via class instance - {test_1.x}")
# print(f"Via class - {StaticTest.x}")
# test_1.x = 15
# print("-" * 100)
# print(f"Via class instance - {test_1.x}")
# print(f"Via class - {StaticTest.x}")
# my_class = MyClass(2, 4, 6, "Hello", 7, 8, 9)
# print(my_class.items[3])
# print(my_class[3])
# my_class[1] = "NEW VALUE"
# print(my_class[1])

# test = Test()
# print(test.show_self())

# test_obj = MyAwesomeClass("Dima", 25, 201)
# print(test_obj)
# print("+" * 100)
# print(repr(test_obj))

# fluffy = Cat("Fluffy", 1)
# print(fluffy.eyes)
# print(Cat.eyes)
# fluffy.say_meaw()
# print(fluffy.energy)
# print(fluffy.sleep)
# print("=" * 100)
# print(fluffy.play(input("Enter some action for the cat: ")))


class SquareValues:
    def __init__(self, val_1: int, val_2: int):
        self.val_1 = val_1
        self.val_2 = val_2

    @staticmethod
    def calculate_norm(a, b):
        return a * a + b * b

    @staticmethod
    def number_validator(arg):
        return isinstance(arg, int)
        # if type(arg) == int:
        #     return True
        # return False

    def print_calculate_norm(self):
        print(self.calculate_norm(self.val_1, self.val_2))

    def process(self):
        if self.number_validator(self.val_1) and self.number_validator(self.val_2):
            self.print_calculate_norm()
        else:
            print("Что-то не так с одним из переданных аргументов")


sq_values = SquareValues(4, 6)

wrong_values = SquareValues(18, 5.3)
sq_values.print_calculate_norm()
print("-" * 100)

sq_values.process()

wrong_values.process()
