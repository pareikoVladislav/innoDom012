# class Animal:
#     def __init__(self):
#         self.paws = 4
#         self.tail = True
#         self.wool = True
#         self.eyes = 2
#         self.ears = 2
#
#
# class Cat(Animal):
#     def __init__(self, name, age):
#         super().__init__()
#         self.name = name
#         self.age = age
#
#     def say_mew(self):
#         print(f"Your pet '{self.name}' says mew")
#
#     def __str__(self):
#         return f"""
#         Cat's name: {self.name}
#         Cat's age: {self.age}
#         Cat's paws: {self.paws}
#         Cat's tail: {self.tail}
#         Cat's wool: {self.wool}
#         Cat's eyes: {self.eyes}
#         Cat's ears: {self.ears}
#         """
#
#
# kitty = Cat("Fluffy", 2)
#
# kitty.say_mew()
# print(kitty)
import os
import time


# class Person:
#     name = input("Enter your name: ")
#     age = int(input("Enter your age: "))
#     __deals = "nothing"
#
#
# class Employee(Person):
#     """
#     Some technical documentations.
#     """
#     department = input("Enter your department: ")
#     salary = float(input("Enter your salary: "))
#
#
# johan = Employee()


# class Vehicle:
#     def __init__(self, name, speed):
#         self.name = name
#         self._speed = speed
#         self.__engine_number = "123XYZ"
#
#     def drive(self):
#         print(f"{self.name} is driving at {self._speed}km/h")
#
#     def _update_speed(self, speed):
#         self._speed = speed
#
#     def __start_engine(self):
#         print("This is a private method, which starts the car's engine")
#
#
# class Car(Vehicle):
#     def __init__(self, name, speed, wheels):
#         super().__init__(name, speed)
#         self.wheels = wheels
#
#     def display_info(self):
#         self.drive()
#         print(f"It has {self.wheels} wheels, and goes {self._speed}km/h")
#
#
# car_name = input("Enter the car's name: ")
# car_speed = int(input("Enter the car's speed: "))
# car_wheels = int(input("Enter the car's wheels: "))
#
# # volvo = Car(car_wheels)
# # volvo = Car(car_wheels)
# volvo = Car(car_name, car_speed, car_wheels)
#
# volvo.drive()
# volvo.display_info()


# class Base:
#     @staticmethod
#     def base_static_method():
#         print("Base static method")
#
#     @classmethod
#     def base_class_method(cls):
#         print(f"Base class method in {cls}")
#
#
# class Derived(Base):
#     pass
#
#
# test_d = Derived()
# test_d_2 = Base()
#
# test_d.base_static_method()
# test_d.base_class_method()
#
# test_d_2.base_static_method()
# test_d_2.base_class_method()
#
# print(test_d.base_static_method() is test_d_2.base_static_method())
#
# print(test_d.base_class_method() is test_d_2.base_class_method())


# class Shape:
#     def __init__(self):
#         print("Shape created")
#
#     def draw(self):
#         print("Drawing a shape")
#
#     def area(self):
#         print("Calc area")
#
#     def perimeter(self):
#         print("Calc perimeter")
#
#
# class Triangle(Shape):
#     def __init__(self, base, height):
#         super().__init__()
#         self.base = base
#         self.height = height
#
#     def draw(self):
#         super().draw()
#         print("Drawing a triangle")
#
#     def area(self):
#         print("Calc triangle area...")
#         time.sleep(3)
#         triangle_area = 0.5 * self.base * self.height
#         super().area()
#         print(f"Triangle area is: {triangle_area}")
#         return triangle_area
#
#     def perimeter(self):
#         super().perimeter()
#         return self.base + 2 * (self.height ** 2) ** 0.5
#
#
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         super().__init__()
#         self.width = width
#         self.height = height
#
#     def draw(self):
#         super().draw()
#         print("Drawing rectangle")
#
#     def area(self):
#         super().area()
#         return self.width * self.height
#
#     def perimeter(self):
#         super().perimeter()
#         return 2 * (self.width + self.height)


# triangle = Triangle(4, 5)
# rectangle = Rectangle(3, 6)

# print(triangle.draw())
# print(f"Area: {triangle.area()}, Perimeter: {triangle.perimeter()}")

# print(triangle.area())

# print(rectangle.draw())
# print(f"Area: {rectangle.area()}, Perimeter: {rectangle.perimeter()}")


# print(5 + 5)
# print("he" + "llo")
# print([2, 4, 6] + [8, 10, 12])

# print(5 * 5)
# print("he-" * 3)
# print([2, 4, 6] * 3)

# print("=" * 100)


# class Bird:
#     def fly(self):
#         print("The bird can fly.")
#
#
# class Ostrich(Bird):  # страус :3
#     def fly(self):
#         print("Ostriches cannot fly =(")
#
#
# # Создаем экземпляры
# bird = Bird()
# ostrich = Ostrich()
#
# # Вызываем методы
# bird.fly()  # Выводит: The bird can fly.
# ostrich.fly()  # Выводит: Ostriches cannot fly.


# from datetime import datetime
#
#
# class Logger:
#     def log(self, message):
#         raise NotImplementedError("Subclasses should implement this!")
#
#
# class TextLogger(Logger):
#     def __init__(self, filename, mode):
#         self.filename = filename
#         self.mode = mode
#
#     def log(self, message):
#         with open(self.filename, self.mode) as log_data:
#             log_data.write(f"[{datetime.now()}] {message}\n")
#
#
# class CSVLogger(Logger):
#     def __init__(self, filename, mode):
#         self.filename = filename
#         self.mode = mode
#         self.ID = 0
#
#     def log(self, message):
#         import csv
#         with open(self.filename, self.mode) as csv_log_data:
#             headers = ["ID", "message"]
#             writer = csv.DictWriter(csv_log_data, fieldnames=headers)
#
#             writer.writeheader()
#
#             message = f"[{datetime.now()}] {message}"
#             self.ID += 1
#             data = {
#                 "ID": self.ID,
#                 "message": message
#             }
#
#             writer.writerow(data)


# Создаем экземпляры логгеров
# text_logger = TextLogger("test_text.txt", "w")
# csv_logger = CSVLogger("test_csv.csv", "w")
# logger = Logger()

# Логгируем сообщения
# text_logger.log("Something happened")
# csv_logger.log("Something else happened")

# logger.log("Something happened")


from datetime import datetime
import csv


class Logger:
    def log(self, message):
        raise NotImplementedError("Subclasses should implement this!")

    def delete(self, message):
        mess = f"Base delete logic for {message} data"
        return mess


class TextLogger(Logger):
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def log(self, message):
        timestamped_message = f"[{datetime.now()}] [FROM] '{self.__class__.__name__}' data: {message}"
        with open(self.filename, self.mode) as txt_log:
            txt_log.write(f"{timestamped_message}\n")

    def delete(self, message):
        with open(self.filename, "r") as log_data:
            lines = log_data.readlines()

        deleted = False

        with open(self.filename, self.mode) as log_data:
            for line in lines:
                if message not in line:
                    log_data.write(line)
                else:
                    deleted = True

        if deleted:
            print(f"Deleted all accurrences of {message}")
        else:
            print(f"The message '{message}' not found.")

        print(super().delete(message))


class CSVLogger(Logger):
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.ID = 0

    def log(self, message):
        headers = ["ID", "message"]

        file_exists = os.path.isfile(self.filename)

        with open(self.filename, self.mode) as csv_log:
            writer = csv.DictWriter(csv_log, fieldnames=headers)

            if not file_exists:
                writer.writeheader()

            self.ID += 1

            data = {
                "ID": self.ID,
                "message": message
            }

            writer.writerow(data)

    def delete(self, mess_id):
        with open(self.filename, "r") as source_data:
            logs = list(csv.DictReader(source_data))

            message = list(filter(lambda x: x["ID"] == str(mess_id), logs))[0]["message"]

            print(super().delete(message))

        if any(log["ID"] == str(mess_id) for log in logs):
            logs = [log for log in logs if log["ID"] != str(mess_id)]

            with open(self.filename, "w") as target_data:
                writer = csv.DictWriter(target_data, fieldnames=logs[0].keys())
                writer.writeheader()
                writer.writerows(logs)

            print(f"The log with ID '{mess_id}' was deleted successfully")
        else:
            print(f"The log with ID '{mess_id}' was not found")


text_logger = TextLogger("new_text_log.txt", "a")
csv_logger = CSVLogger("new_csv_log.csv", "a")

text_logger.log("Some test data_1")
text_logger.log("Some test data_2")
text_logger.log("Some test data_3")
text_logger.log("Some test data_4")
text_logger.log("Some test data_5")
text_logger.log("Some test data_6")
text_logger.log("Some test data_7")

text_logger.delete("Some test data_5")


csv_logger.log("Some test data for csv file 1")
csv_logger.log("Some test data for csv file 2")
csv_logger.log("Some test data for csv file 3")
csv_logger.log("Some test data for csv file 4")
csv_logger.log("Some test data for csv file 5")
csv_logger.log("Some test data for csv file 6")
csv_logger.log("Some test data for csv file 7")
csv_logger.log("Some test data for csv file 8")
csv_logger.log("Some test data for csv file 9")
csv_logger.log("Some test data for csv file 10")
csv_logger.log("Some test data for csv file 11")

csv_logger.delete(8)
