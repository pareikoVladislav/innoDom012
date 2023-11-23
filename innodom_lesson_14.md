<!-- TOC -->
* [**Inheritance, Polymorphism**](#inheritance-polymorphism-)
* [**The workings of encapsulation in inheritance:**](#the-workings-of-encapsulation-in-inheritance-)
* [**Static methods and class methods in inheritance:**](#static-methods-and-class-methods-in-inheritance-)
* [**Class hierarchy and descendant class**](#class-hierarchy-and-descendant-class-)
* [**The importance of class hierarchy**](#the-importance-of-class-hierarchy-)
* [**Advantages and disadvantages of inheritance**](#advantages-and-disadvantages-of-inheritance-)
* [**Polymorphism**](#polymorphism)
* [**Method Overriding**](#method-overriding-)
* [**Operator overloading**](#operator-overloading-)
* [**protected attributes and methods for polymorphism in inheritance**](#protected-attributes-and-methods-for-polymorphism-in-inheritance-)
<!-- TOC -->


# **Inheritance, Polymorphism**                        

**Наследование** - это механизм в объектно-ориентированных языках программирования,                            
таких как **Python**, который позволяет создавать новый класс на основе                            
существующего класса. Новый класс наследует атрибуты (переменные) и методы                           
(функции) из родительского класса и может дополнять, изменять                           
или переопределять их.                           

Подкласс может добавлять собственные атрибуты и методы, а также переопределять                         
методы родительского класса.                               

Поведение с переопределением логики уже существующего метода                            
называется **Полиморфизм**                             


Когда производный класс наследует свойства и методы от базового класса, он может                                
использовать их как свои собственные, добавлять новые или изменять существующие.                               
Это позволяет существенно упростить разработку и поддержку кода, так как                                 
можно переиспользовать уже существующую функциональность.                                        

```python
class Animal:
    def __init__(self):
        self.paws = 4
        self.tail = True
        self.ears = 2
        self.wool = True

class Cat(Animal):
    def __init__(self, name, age):
        super().__init__()
        self.name = name
        self.age = age

    def say_mew(self):
        print(f"Your pet {self.name} say 'Mew'!")


    def __str__(self):
        return f"""
        Cat's name: {self.name}
        Cat's age: {self.age}
        Cat's paws: {self.paws}
        Cat with tail? - {self.tail}
        Cat's ears: {self.ears}
        Cat have wool? - {self.wool}
        """
```

**На каких принципах основывается наследование?**

* **Повторное использование кода:** подклассы наследуют методы и переменные                                             
родительского класса, что позволяет переиспользовать код.                                                   
* **Иерархия:** наследование позволяет создавать иерархическую структуру классов.                                            
* **Расширяемость:** классы могут быть расширены новыми функциями и данными                                             
без изменения существующего кода.                                            


**Как применяется в программировании?**                                                                    

1) **Общие модели данных:** базовый класс может быть расширен для создания                                   
специализированных классов.           

```python
class Person:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

class Employee(Person):
    department = input("Enter your department: ")
    salary = float(input("Enter your salary: "))

```

2) **Плагины и расширения:** Создание плагинов, которые расширяют базовый                                                                    
функционал без изменения исходного кода приложения.                                                                    

3) **Компоненты пользовательского интерфейса:** Базовые классы для элементов                                                                     
интерфейса могут быть расширены для создания конкретных элементов управления.                                                                    

**Что не стоит делать:**                                                             

* Использовать наследование для создания очень тесно связанных классов,                                                            
что может усложнить поддержку и расширение кода.                                                            
* Наследовать классы только ради повторного использования кода, не учитывая                                                             
логическую связь между ними.                                                            
* Использовать наследование для доступа к защищенным данным класса,                                                             
нарушая принципы инкапсуляции.                                                     

# **The workings of encapsulation in inheritance:**                                                     

В **Python** инкапсуляция реализуется через использование публичных,                                                      
защищенных (`_`) и приватных (`__`) атрибутов и методов.                                                     

При наследовании подклассы имеют доступ к **публичным** и **защищенным**                                                      
методам родительского класса, но **НЕ имеют прямого доступа** к                                                      
приватным методам и переменным (которые начинаются с двойного                                                      
подчеркивания).                                                     


```python
class Vehicle:
    def __init__(self, name, speed):
        self.name = name  # Публичный атрибут
        self._speed = speed  # Защищённый атрибут
        self.__engine_number = "123XYZ"  # Приватный атрибут

    def drive(self):  # Публичный метод
        print(f"{self.name} is driving at {self._speed}km/h")

    def _update_speed(self, speed):  # Защищённый метод
        self._speed = speed

    def __start_engine(self):  # Приватный метод
        print("This is a private method, which starts the car's engine")

class Car(Vehicle):
    def __init__(self, name, speed, wheels):
        super().__init__(name, speed)
        self.wheels = wheels

    def display_info(self):
        self.drive()  # Доступ к публичному методу родителя
        print(f"It has {self.wheels} wheels and goes {self._speed}km/h")  # Доступ к защищенному атрибуту родителя
        
volvo = Car("turbo", 400, 800)
volvo.drive()
volvo.display_info()
volvo._update_speed(450)
volvo.__start_engine()  # Ошибка
```

Приватные атрибуты и методы используются для внутренней реализации класса,                                                     
и доступ к ним за пределами класса приведёт к ошибке.                                                     


# **Static methods and class methods in inheritance:**                                                     

**Статические методы** (`@staticmethod`) и **методы класса** (`@classmethod`) также                                                      
наследуются. **Статические методы** не имеют доступа к `cls` или `self` по                                                     
умолчанию и используются для функциональности, не зависящей от экземпляра                                                     
или класса. **Методы класса** имеют доступ к классу через `cls` и могут                                                     
использоваться для фабричных методов или других методов, которые не                                                      
требуют инициализации экземпляра.                                                     

```python
class Base:
    @staticmethod
    def base_static_method():
        print("Base static method")

    @classmethod
    def base_class_method(cls):
        print(f"Base class method in {cls}")

class Derived(Base):
    pass


test_d = Derived()
test_d_2 = Base()

test_d.base_static_method()
test_d.base_class_method()

test_d_2.base_static_method()
test_d_2.base_class_method()

print(test_d.base_static_method() is test_d_2.base_static_method())

print(test_d.base_class_method() is test_d_2.base_class_method())
```

В этом примере `Derived` наследует статический метод и метод класса от                                                      
`Base`, и мы можем вызвать их через `Derived`.                                                     


Метод `super()` в **Python** используется для вызова методов родительского класса                               
из дочернего класса. Он позволяет получить доступ к родительским методам и их                           
поведению. Этот метод полезен для выполнения специфических действий в дочерних                                
классах, при этом сохраняя и используя функциональность, предоставленную                              
родительским классом.                                 

Использование `super()` особенно полезно в тех случаях, когда дочерний класс                                
переопределяет методы родительского класса и нужно выполнить какую-то логику                              
из родительского метода в дополнение к собственной логике дочернего класса.                                                               

**super() может быть полезен по нескольким причинам:**                                                               

* **Доступ к методам родителя:** Когда ты переопределяешь методы в подклассе,                                                                
иногда нужно также выполнить оригинальную реализацию метода из                                                                
родительского класса. `super()` позволяет это сделать без прямого                                                                
обращения к родительскому классу.                                                               

* **Избежание дублирования кода:** Если подклассы должны выполнять некоторые                                                                
действия, которые уже реализованы в родительском классе, `super()`                                                                
позволяет повторно использовать эту логику, а не копировать её.                                                               

* **Порядок разрешения методов (`MRO`):** В сложных иерархиях наследования с                                                                
множественным наследованием `super()` используется для правильного и                                                                
предсказуемого вызова методов предков.                                                               

Метод `super()` не ограничивается только статическими атрибутами класса. Он                           
предназначен для вызова методов родительского класса и обращения как к                           
статическим, так и к динамическим атрибутам класса-родителя.                              

По сути, `super()` предоставляет доступ к всем атрибутам и методам родительского                             
класса, включая как статические, так и динамические атрибуты, внутренние и                           
внешние методы, и другие элементы класса.                               

Когда вызывается `super()`, это означает, что дочерний класс может получить                          
доступ к поведению и атрибутам родительского класса и использовать их, а                              
также расширить или изменить это поведение по своему усмотрению.                              


```python
class Shape:
    def __init__(self):
        print("Shape created")
    
    def draw(self):
        print("Drawing a shape")

    def area(self):
        print("Calc area")

    def perimeter(self):
        print("Calc perimeter")


class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__()
        self.base = base
        self.height = height
        
    def draw(self):
        print("Drawing a triangle")

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        return self.base + 2 * (self.height ** 2) ** 0.5

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        
    def draw(self):
        print("Drawing rectangle")

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

triangle = Triangle(4, 5)
rectangle = Rectangle(3, 6)

print(triangle.draw())
print(f"Area: {triangle.area()}, Perimeter: {triangle.perimeter()}")

print(rectangle.draw())
print(f"Area: {rectangle.area()}, Perimeter: {rectangle.perimeter()}")
```



# **Class hierarchy and descendant class**                                                                                           

Иерархия классов и понятие "класс-потомок" (**или подкласс**) являются ключевыми                                                                
элементами в объектно-ориентированном программировании (**ООП**), особенно когда                                                               
речь идёт о наследовании.                                                               

**Иерархия классов**                                                                                           

**Иерархия классов** — это способ структурирования классов и их отношений в                                                                                           
программе. В иерархии классов могут быть разные уровни:                                                                                           

* **Базовый класс (или** суперкласс**)**: На самом верхнем уровне иерархии находится                                                                                            
базовый класс. Этот класс определяет общие характеристики и поведение, которые                                                                                            
будут наследоваться подклассами. Обычно базовый класс более общий и абстрактный.                                                                                           

* **Подклассы (или классы-потомки)**: Это классы, которые наследуют от                                                                                            
базового класса. Они могут не только наследовать функциональность                                                                                            
родительского класса, но и добавлять свои уникальные характеристики и 
методы, а также переопределять унаследованные. Подклассы более                                                                                            
конкретны и специализированы.                                                                                           

```python
import time

# Определяем базовый класс Vehicle
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print(f"{self.brand} {self.model} is starting.")

    def stop(self):
        print(f"{self.brand} {self.model} is stopping.")

# Определяем подкласс Car, наследующий от Vehicle
class Car(Vehicle):
    def __init__(self, brand, model, car_type):
        super().__init__(brand, model)  # Вызываем конструктор родительского класса
        self.car_type = car_type

    def change_gear(self, gear):
        print(f"{self.brand} {self.model} is changing gear to {gear}.")

# Определяем подкласс Motorcycle, наследующий от Vehicle
class Motorcycle(Vehicle):
    def wheelie(self):
        print(f"{self.brand} {self.model} is doing a wheelie!")


class Truck(Vehicle):
    def __init__(self, brand, model, cargo_capacity):
        super().__init__(brand, model)
        self.cargo_capacity = cargo_capacity
        self.current_cargo = 0

    def truck_up(self, cargo_value):
        print("Loading the cargo into the truck.")

        if self.current_cargo <= self.cargo_capacity:
            time.sleep(5)
            self.current_cargo += cargo_value
            print("The cargo was succesfully loaded.")
        else:
            print("The truck is already fully loaded.")



# Создаем экземпляры наших классов
my_car = Car("Toyota", "Corolla", "Sedan")
my_motorcycle = Motorcycle("Harley-Davidson", "Street 750")

# Используем методы классов
my_car.start()
my_car.change_gear(3)
my_car.stop()

my_motorcycle.start()
my_motorcycle.wheelie()
my_motorcycle.stop()

```

В контексте уже написанного нами кода с транспортными средствами, мы можем                                             
провести следующую параллель:                                                                                           

* `Vehicle` (**Транспортное средство**) - базовый класс. Определяет общие                                                                                            
атрибуты и методы, такие как `start` и `stop`.                                                                                           

* `Car` (**Автомобиль**) - подкласс `Vehicle`. Добавляет атрибуты и методы,                                                                                           
специфичные для автомобилей, такие как `number_of_doors` и `drive`.                                                                                           

* `Motorcycle` (**Мотоцикл**) - еще один подкласс `Vehicle`. Имеет уникальные                                                                                            
характеристики и методы, например, `wheelie`.                                                                                           

* `Truck` (**Грузовик**) - подкласс `Vehicle`. Может добавлять такие атрибуты,                                                                                           
как `cargo_capacity`.                                                                                           


В этой иерархии `Vehicle` является базовым классом, а Car, `Motorcycle` и `Truck`                                                                                           
являются подклассами, которые наследуют общие свойства и поведение от                                                                                            
`Vehicle`, но также вводят свои уникальные особенности.                                                                                           

# **The importance of class hierarchy**                                                                                           

* **Повторное использование кода:** Подклассы наследуют функциональность                                                                                            
суперкласса, что уменьшает дублирование кода.                                                                                           

* **Расширяемость:** Легко добавлять новые классы в систему, расширяя существующие.                                                                                           

* **Модульность:** Иерархия классов способствует созданию модульного и                                                                                            
структурированного кода.                                                                                           

* **Полиморфизм:** Объекты разных классов могут быть обработаны единообразно,                                                                                           
если они являются подклассами одного базового класса.                                                                                           
                                                                                           
---                               

# **Advantages and disadvantages of inheritance**                                                               


**Преимущества**                           

1) `Повторное использование кода:`                                  
Наследование позволяет повторно использовать атрибуты и методы из                              
родительского класса в дочернем классе, что способствует                                  
уменьшению дублирования кода.                                

2) `Организация классов в иерархии:`                                
Наследование позволяет создавать иерархию классов, где классы могут                                 
быть логически сгруппированы и упорядочены.                                        

3) `Полиморфизм:`                                
Наследование часто сопровождается полиморфизмом. Это означает, что объекты                          
подклассов могут использоваться там, где ожидаются объекты базовых классов,                             
что упрощает код и делает его более гибким.                             

**Недостатки**                                 

1) `Сложность иерархии:`                                 
Слишком глубокая и сложная иерархия наследования может стать сложной                               
для понимания и обслуживания.                                

2) `Проблемы с переопределением:`                                             
Переопределение методов из родительского класса в дочернем классе может                                 
привести к трудностям, если не учтены все детали.                                                  

---

# **Polymorphism**

**Полиморфизм** — один из ключевых принципов объектно-ориентированного                                                  
программирования. Слово "**полиморфизм**" происходит от греческих слов                                                   
"**поли**" (много) и "**морфе**" (форма), и в контексте **ООП** оно означает                                                   
способность объектов с одинаковым интерфейсом предоставлять                                                   
различное поведение.                                                  


В Python полиморфизм может быть реализован двумя основными способами:                                                  
* **через переопределение методов**                                                   
* **через перегрузку операторов.**                                                                                    

# **Method Overriding**                                                                                    

Переопределение методов происходит, когда подкласс изменяет поведение                                                                                    
метода, унаследованного от родительского класса. Это позволяет                                                                                     
подклассам предоставлять специфичную реализацию метода, сохраняя                                                                                    
при этом одинаковый интерфейс.                                                                                    

На самом деле мы уже с вами использовали полиморфизм ещё на старте изучения **Python**                                                                                   
в рамках работы с такими операторами, как `+`, `*`, `in` и другими.                                               

В **Python**, полиморфизм проявляется в поведении математических операторов,                                                                                     
таких как `+` и `*`, когда они применяются к различным типам данных. Это                                                                                     
один из примеров перегрузки операторов, которая является частью                                                                                     
полиморфизма в программировании.                                                                                    

**Оператор +:**                                                                                    

* При использовании с числами (`int`, `float`) оператор + выполняет **математическое сложение**.                                                                                    
* При использовании со строками (`str`) он выполняет конкатенацию (**слияние строк**).                                                                                    
* При использовании со списками (`list`) он **объединяет списки**.                                                                                


**Оператор *:**                                                                                    

* При использовании с **числами** оператор `*` выполняет **математическое умножение**.                                                                                    
* При использовании **строкой** и **числом** он **повторяет строку указанное количество раз**.                                                                                    
* При использовании **со списком и числом** он **повторяет элементы списка                                                                                     
указанное количество раз.**                                                                                    



```python
class Bird:
    def fly(self):
        print("The bird can fly.")

class Ostrich(Bird):  # страус :3
    def fly(self):
        print("Ostriches cannot fly.")

# Создаем экземпляры
bird = Bird()
ostrich = Ostrich()

# Вызываем методы
bird.fly()  # Выводит: The bird can fly.
ostrich.fly()  # Выводит: Ostriches cannot fly.
```

```python
from datetime import datetime

class Logger:
    def log(self, message):
        raise NotImplementedError("Subclasses should implement this!")

class TextLogger(Logger):
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def log(self, message):
        with open(self.filename, self.mode) as log_data:
            log_data.write(f"[{datetime.now()}] {message}\n")

class CSVLogger(Logger):
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.ID = 0

    def log(self, message):
        import csv
        with open(self.filename, self.mode) as csv_log_data:
            headers = ["ID", "message"]
            writer = csv.DictWriter(csv_log_data, fieldnames=headers)

            writer.writeheader()

            message = f"[{datetime.now()}] {message}"
            self.ID += 1
            data = {
                "ID": self.ID,
                "message": message
            }

            writer.writerow(data)

# Создаем экземпляры логгеров
text_logger = TextLogger("test_text.txt", "w")
json_logger = CSVLogger("test_csv.csv", "w")

# Логгируем сообщения
text_logger.log("Something happened")
json_logger.log("Something else happened")
```

# **Operator overloading**                                                                                    

В реальных проектах перегрузка операторов может быть полезна для создания                                                                                     
классов с интуитивно понятным интерфейсом.                                                                                    

```python
from datetime import datetime
import csv


class Logger:
    def log(self, message):
        raise NotImplementedError("Subclasses should implement this!")

    def delete(self, message):
        message = f"Base delete logic for '{message}' data"
        return message


class TextLogger(Logger):
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def log(self, message):
        timestamped_message = f"[{datetime.now()}] {message}\n"
        with open(self.filename, self.mode) as log_file:
            log_file.write(timestamped_message)

    def delete(self, message):
        print(super().delete(message))
        with open(self.filename, "r") as log_file:
            lines = log_file.readlines()
        
        deleted = False
        with open(self.filename, "w") as log_file:
            for line in lines:
                if message not in line:
                    log_file.write(line)
                else:
                    deleted = True

        if deleted:
            print(f"Deleted all occurrences of '{message}'")
        else:
            print(f"The message '{message}' not found.")


class CSVLogger(Logger):
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.ID = 0

    def file_exists_checker(self):
        try:
            with open(self.filename, "r", newline="") as csv_log_data:
                reader = csv.reader(csv_log_data)
                return len(list(reader)) > 0
        except FileNotFoundError:
            return False

    def log(self, message):
        headers = ["ID", "message"]
        file_exists = self.file_exists_checker()

        with open(self.filename, self.mode, newline="") as csv_log_data:
            writer = csv.DictWriter(csv_log_data, fieldnames=headers)

            if not file_exists:
                writer.writeheader()

            self.ID += 1
            data = {
                "ID": self.ID,
                "message": f"[{datetime.now()}] {message}"
            }

            writer.writerow(data)

    def delete(self, ID):
        with open(self.filename, "r", newline="") as source_data:
            logs = list(csv.DictReader(source_data))

            message = list(filter(lambda x: x["ID"] == ID, logs))[0]["message"]
            print(super().delete(message))
        if any(log["ID"] == str(ID) for log in logs):
            logs = [log for log in logs if log["ID"] != str(ID)]

            with open(self.filename, "w", newline="") as target_file:
                writer = csv.DictWriter(target_file, fieldnames=logs[0].keys())
                writer.writeheader()
                writer.writerows(logs)

            print(f"Deleted log with ID {ID}")
        else:
            print(f"Log with ID {ID} not found.")


# Создаем экземпляры логгеров
text_logger = TextLogger("test_text.txt", "a")
csv_logger = CSVLogger("test_csv.csv", "a")

# Логгируем сообщения
text_logger.log("Something happened")
text_logger.log("Something happened_1")
text_logger.log("Something happened_2")
text_logger.log("Something happened_3")
text_logger.log("Something happened_4")

text_logger.delete("Something happened_3")

csv_logger.log("Something else happened")
csv_logger.log("Something else happened_1")
csv_logger.log("Something else happened_2")
csv_logger.log("Something else happened_3")
csv_logger.log("Something else happened_4")
csv_logger.log("Something else happened_5")
csv_logger.log("Something else happened_6")

csv_logger.delete("5")
```

# **protected attributes and methods for polymorphism in inheritance**                                                                                    

Защищённые (`protected`) атрибуты и методы в **Python** обычно обозначаются одним                                                                                     
нижним подчеркиванием (`_`) перед именем. Хотя **Python** не обеспечивает строгую                                                                                     
инкапсуляцию на уровне синтаксиса, существует конвенция, согласно которой                                                                                    
защищённые атрибуты и методы не должны использоваться за пределами класса                                                                                     
и его подклассов. В контексте наследования и полиморфизма это имеет                                                                                     
несколько важных последствий:                                                                                    


* **Доступность в подклассах:** Защищённые атрибуты и методы доступны в подклассах                                                                                     
и могут быть переопределены или использованы для добавления                                                                                     
дополнительной функциональности.                                                                                    

* **Соблюдение конвенции:** Хотя технически защищённые атрибуты и методы доступны                                                                                     
вне класса, соблюдение конвенции предполагает, что они используются только                                                                                     
внутри класса и его подклассов. Это помогает поддерживать структурированность                                                                                    
и читаемость кода.                                                                                    

* **Переопределение методов:** Подклассы могут свободно переопределять защищённые                                                                                    
методы, обеспечивая полиморфное поведение. При этом они также могут                                                                                    
расширять или изменять логику базового класса.                                                                                    

* **Доступ к защищённым атрибутам:** Подклассы могут использовать защищённые                                                                                    
атрибуты базового класса напрямую. Это может быть полезно для сохранения                                                                                     
внутреннего состояния объекта или для реализации более сложной логики.                                                                                    


```python
class BaseClass:
    def __init__(self):
        self._protected_attribute = "Protected"

    def _protected_method(self):
        print("This is a protected method")

class SubClass(BaseClass):
    def use_protected(self):
        print(f"Using protected attribute: {self._protected_attribute}")
        self._protected_method()

# Создание экземпляра подкласса и использование защищённых атрибутов/методов
sub = SubClass()
sub.use_protected()
```

В этом примере `SubClass` наследует `BaseClass` и имеет доступ к защищённым                                                                                     
атрибутам и методам. `SubClass` использует их в своем методе `use_protected`,                                                                                    
что является нормальной практикой в рамках **ООП** и **полиморфизма**.                                                                                    
