<!-- TOC -->
* [**In-depth OOP, themes from interviews**](#in-depth-oop-themes-from-interviews-)
* [**Classes context manager's magic methods**](#classes-context-managers-magic-methods)
* [**Slots**](#slots-)
* [**What's the SLOTS?**](#whats-the-slots-)
* [**How to use SLOTS?**](#how-to-use-slots-)
* [**When I can use the SLOTS?**](#when-i-can-use-the-slots-)
* [**SLOTS conclusion**](#slots-conclusion-)
* [**Iterators, Generators**](#iterators-generators-)
* [**Iterators...? WHAT IS IT?**](#iterators-what-is-it-)
* [**Built-in functions iter(), and next()**](#built-in-functions-iter-and-next-)
* [**Generators**](#generators-)
* [**Why the iterators are important?**](#why-the-iterators-are-important-)
* [**Iterators & Generators Conclusion**](#iterators--generators-conclusion-)
* [**Design patterns in Python**](#design-patterns-in-python-)
* [**Descriptors**](#descriptors-)
* [**Descriptor's methods**](#descriptors-methods-)
* [**Problems with Descriptors**](#problems-with-descriptors-)
* [**The Descriptor's Conclusion**](#the-descriptors-conclusion-)
* [**META-classes**](#meta-classes-)
* [**What's the META-classes????**](#whats-the-meta-classes-)
* [**Imperative and declarative approach**](#imperative-and-declarative-approach-)
* [**Imperative approach**](#imperative-approach-)
* [**Declarative VS Imperative**](#declarative-vs-imperative-)
* [**Imperative, and Declarative approach conclusion**](#imperative-and-declarative-approach-conclusion-)
<!-- TOC -->

# **In-depth OOP, themes from interviews**                                                                   

# **Classes context manager's magic methods**

Python контекстные менеджеры реализуются при помощи "магических" методов __enter__()                                                                   
и __exit__(). Когда вы используете контекстный менеджер с оператором with,                                                                    
__enter__() вызывается при входе в блок with, а __exit__() вызывается при                                                                    
выходе из него. Например:                                                                                           

```python
class ManagedResource:
    def __enter__(self):
        print("Resource is being opened.")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Resource is being closed.")
```
В этом случае вы можете использовать ManagedResource в качестве контекстного                                                                                           
менеджера следующим образом:                                                                                           

```python

with ManagedResource():
    print("I am using the managed resource!")
```

Магические методы `__enter__()` и `__exit__()` связаны с контекстным                                                               
управлением (context management) в Python и используются для создания                                                             
и управления контекстами с помощью оператора `with`.                                                                

* `__enter__(self):` Этот метод вызывается при входе в блок кода `with`.                                                                  
Он выполняет предварительные настройки или ресурсные выделения, которые                                                                    
необходимы для контекста. `__enter__()` может возвращать какое-либо значение,                                                                
которое будет доступно в блоке `with` через ключевое слово `as`.                                                                    

* `__exit__(self, exc_type, exc_value, traceback):` Этот метод вызывается при                                                                   
выходе из блока кода `with`. Он обычно используется для выполнения завершающих                                                              
действий, таких как закрытие файлов, освобождение ресурсов и обработка                                                                
исключений. `exc_type`, `exc_value` и `traceback` представляют информацию об                                          
исключении, если оно произошло внутри блока `with`.                                                                 

Если __exit__() возвращает True, исключение будет подавлено. Если __exit__()                                
не возвращает ничего или возвращает False, исключение будет повторно вызвано                                                                 
после выхода из __exit__().                                                                   

```python
class ManagedResource:
    def __enter__(self):
        print("Resource is being opened.")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Resource is being closed.")
        if exc_type:
            print(f"Exception found: {exc_type}, {exc_value}")
            return True  # suppress exception

with ManagedResource():
    print("I am using the managed resource!")
    raise ValueError("Something has gone wrong!")
```

Как видите, исключение было обработано и подавлено внутри __exit__().                                                      


**примерно так** выглядит процесс работы оператора `with` под капотом:                                                                 

```python
class FileContextManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

# Использование контекстного менеджера
with FileContextManager("example.txt", "w") as file:
    file.write("Hello, World!")

# Файл будет автоматически закрыт при выходе из блока with
```

Преимущество использования магических методов `__enter__()` и `__exit__()`                                
заключается в том, что они позволяют автоматически управлять ресурсами и                              
обрабатывать исключения в контексте. Это делает код более чистым и безопасным,                          
особенно при работе с файлами, сетевыми соединениями, базами данных и другими                            
ресурсами, требующими явного освобождения или очистки.                              


```python
import sqlite3

class DatabaseConnection:
    def __init__(self, database):
        self.database = database
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.database)
        return self.connection

    def __exit__(self, exc_type, exc_value, traceback):
        if self.connection:
            self.connection.close()

def create_table(connection):
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS employees (
                      id INTEGER PRIMARY KEY,
                      name TEXT,
                      position TEXT)''')

def insert_data(connection, data):
    cursor = connection.cursor()
    cursor.executemany("INSERT INTO employees (name, position) VALUES (?, ?)", data)
    connection.commit()

def display_data(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM employees")
    result = cursor.fetchall()
    for row in result:
        print(row)

# Использование контекстного менеджера для работы с SQLite базой данных
db_filename = "mydb.sqlite"

with DatabaseConnection(db_filename) as conn:
    create_table(conn)
    data_to_insert = [("John Doe", "Manager"), ("Alice Johnson", "Engineer")]
    insert_data(conn, data_to_insert)
    display_data(conn)

# Соединение будет автоматически закрыто при выходе из блока with
```

Помимо этого есть ещё один интересный метод `__call__()`, который позволяет                        
нам писать использовать наши классы, как декораторы:                          

```python
import time

class TimingDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        result = self.func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
        return result

@TimingDecorator
def some_function():
    time.sleep(2)
    print("Function executed")

some_function()
```

```python
import time

class TimingDecorator:
    def __init__(self, message):
        self.message = message

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"{self.message}: {end_time - start_time} seconds")
            return result
        return wrapper

@TimingDecorator("Execution time")
def some_function():
    time.sleep(2)
    print("Function executed")

some_function()
```

# **Slots**                                                                                             

В **Python** каждый объект имеет встроенный словарь (`__dict__`), в котором хранятся                                                                                             
все его атрибуты. Однако это может быть неэффективным с точки зрения памяти,                                                                                              
особенно когда у вас множество маленьких объектов. Именно тут на помощь                                                                                              
приходит магический атрибут `__slots__`.                                                                                             


# **What's the SLOTS?**                                                                                             

`__slots__` — это магический атрибут класса, который указывает, какие атрибуты                                                                                             
экземпляра могут существовать в объекте. Если вы задаете `__slots__`, то для хранения                                                                                             
атрибутов будет использоваться не обычный словарь, а более компактная структура,                                                                                             
что может сэкономить память.                                                                                            


# **How to use SLOTS?**                                                                            

Для использования `__slots__` в классе достаточно задать его в виде кортежа или                                                                             
списка с именами атрибутов:                                                                            

```python
class MyClass:
    __slots__ = ('name', 'age')

    def __init__(self, name, age):
        self.name = name
        self.age = age
```

**Какие есть преимущества использования `__slots__`?**                                                                                              

* **Экономия памяти:** Объекты классов, использующих `__slots__`, обычно занимают                                                                                              
меньше памяти, чем без `__slots__`.                                                                                              

* **Быстродействие:** Доступ к атрибутам может быть немного быстрее                                                                                                                                                                                             
благодаря оптимизированной структуре.                                                                                              


**Ограничения и особенности `__slots__`:**                                                                                      

* **Жесткость**: Вы не сможете добавлять новые атрибуты к экземплярам класса,                                                                                       
которые не указаны в `__slots__`.                                                                                      

* **Отсутствие `__dict__`**: Объекты с `__slots__` обычно не имеют `__dict__`, что                                                                                      
делает невозможным некоторые операции (например, динамическое                                                                                      
добавление атрибутов).                                                                                      

* **Наследование**: Если вы наследуете класс с `__slots__`, дочерний класс также                                                                                      
наследует `__slots__`. Если дочерний класс также имеет свои `__slots__`,                                                                                       
атрибуты из обоих классов комбинируются.                                                                                      

* **Дескрипторы**: `__slots__` создает дескрипторы для переменных экземпляра                                                                                      


# **When I can use the SLOTS?**                                                                                  

* Когда у вас множество маленьких объектов, и вам нужно оптимизировать                                                                                  
использование памяти.                                                                                  

* Когда вы точно знаете, какие атрибуты будут у объекта, и эта                                                                                   
структура не будет меняться.                                                                                  


# **SLOTS conclusion**                                                                                  

Использование `__slots__` — это способ оптимизации, который может быть полезен                                                                                   
в определенных ситуациях. Однако перед его применением следует хорошо подумать,                                                                                   
подходит ли он для вашего конкретного случая, учитывая и преимущества,                                                                                  
и ограничения.                                                                                  

**Могу ли я использовать и `__slots__`, и `__dict__` одновременно?**                                                                                  
Да, можно, добавив "`__dict__`" в `__slots__`. Однако это уменьшит                                                                                  
преимущества `__slots__` в плане экономии памяти.                                                                                  


**Что произойдет, если я попытаюсь добавить атрибут, которого нет в `__slots__`?**                                                                                  
Вы получите ошибку `AttributeError`.                                                                                  

---

# **Iterators, Generators**                                                                                  

**Итераторы** — ключевая концепция в **Python**, которая позволяет перебирать элементы                                                                                  
коллекции (например, списка или словаря) последовательно, не                                                                                  
зная заранее, сколько их там.                                                                                  


# **Iterators...? WHAT IS IT?**                                                                                  

**Итератор** — это объект, который реализует два метода: `__iter__()` и `__next__()`.                                                                                  
Метод `__iter__()` возвращает сам итератор, а `__next__()` возвращает следующий                                                                                  
элемент из итератора. Когда элементы заканчиваются, `__next__()` выбрасывает                                                                                   
исключение `StopIteration`.                                                                                  

**Простой пример:**                                                                  

```python
class SimpleRange:
    def __init__(self, end):
        self.end = end
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            value = self.current
            self.current += 1
            return value
        raise StopIteration

numbers = SimpleRange(3)

for num in numbers:
    print(num)
```

# **Built-in functions iter(), and next()**                                                                         

Python предоставляет функции `iter()` и `next()`, чтобы работать с итераторами:                                                                         

* `iter(obj)` превращает объект в итератор (если это возможно).                                                                         

* `next(iterator)` возвращает следующий элемент итератора или выбрасывает                                                                          
исключение `StopIteration`, если элементы закончились.                                                                         


**Итерируемые объекты**                                                                         

Не каждый объект в **Python** является итератором, но многие являются итерируемыми.                                                                          
Итерируемый объект — это объект, у которого есть метод `__iter__()`, возвращающий                                                                         
итератор. Примеры включают списки, кортежи, словари и многие другие.                                                                         



# **Generators**                                                                         

Генераторы — это специальный вид итераторов, которые можно создать с помощью функций                                                                         
и ключевого слова `yield`. Генераторы ленивы: они генерируют значения                                                                          
по мере необходимости.                                                                         

**Пример генератора:**                                                                         

```python
def simple_range(end):
    current = 0
    while current < end:
        yield current
        current += 1

for num in simple_range(3):
    print(num)
```

# **Why the iterators are important?**                                                                         

* **Эффективность:** Итераторы не требуют загрузки всех элементов в память сразу.                                                                          
Это особенно полезно при работе с большими данными.                                                                         

* **Универсальность:** Многие встроенные структуры данных в **Python** (такие как                                                                          
списки или словари) и библиотеки поддерживают итераторы.                                                                         

* **Создание пользовательских коллекций:** Вы можете создать свою коллекцию                                                                          
объектов, которая поддерживает итерацию.                                                                         


# **Iterators & Generators Conclusion**                                                                         

**Итераторы** — это мощный инструмент в **Python**, позволяющий эффективно и удобно                                                                          
работать с коллекциями данных. Благодаря итераторам вы можете создавать                                                                          
ленивые вычисления, экономить память и делать ваш код более читаемым.                                                                         


**Чем отличается итератор от итерируемого объекта?**                                                                         
**Итератор** — это объект, который реализует методы `__iter__()` и `__next__()`.                                                                          
Итерируемый объект — это объект, который может возвращать итератор с                                                                          
помощью метода `__iter__()`, но сам по себе итератором не является.                                                                         


**Что делать, если я хочу перебрать итератор несколько раз?**                                                                         
Вы можете создать новый итератор или, если это возможно, переиспользовать                                                                          
исходный объект для создания нового итератора.                                                                         

---

# **Design patterns in Python**                                                                         

**Шаблоны проектирования** — это проверенные временем решения, применяемые для решения                                                                          
часто встречающихся проблем программирования. Они представляют собой наборы из                                                                          
принципов и методик, которые могут быть адаптированы под конкретную задачу.                                                                         
Шаблоны не привязаны к конкретному языку программирования, но они могут                                                                          
быть реализованы по-разному в зависимости от особенностей языка.                                                                         

В **Python** многие шаблоны проектирования реализуются проще и элегантнее                                                                         
благодаря динамической типизации и другим возможностям языка.                                                                         

Рассмотрим некоторые основные шаблоны проектирования, часто                                                                         
используемые в **Python**:                                                                         


1) **Одиночка (Singleton)**                                                                        
* `Цель:` Гарантировать, что класс имеет только один экземпляр, и предоставить                                                                         
к нему глобальную точку доступа.                                                                        

* `Пример в Python:` Использование модулей (так как модули импортируются только                                                                         
один раз) или класса с приватным конструктором и специальным                                                                         
методом для получения экземпляра.                                                                        

```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# Пример использования:
first_instance = Singleton()
second_instance = Singleton()
print(first_instance is second_instance)  # True
```

2) **Фабрика (Factory)**                                                                        
* `Цель:` Определить интерфейс для создания объекта, но позволить подклассам                                                                         
решить, какой класс инстанцировать.                                                                        

* `Пример в Python:` Определение метода в базовом классе, который возвращает                                                                         
экземпляр одного из производных классов на основе переданных параметров.                                                                        

```python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class AnimalFactory:
    def create_animal(self, animal_type):
        if animal_type == "Dog":
            return Dog()
        elif animal_type == "Cat":
            return Cat()
        else:
            return None

# Пример использования:
factory = AnimalFactory()
animal = factory.create_animal("Dog")
print(animal.speak())  # Woof!
```

3) **Строитель (Builder)**                                                                        
* `Цель:` Отделить конструирование сложного объекта от его представления, так                                                                         
что в результате одного и того же процесса конструирования могут получаться                                                                         
разные представления.                                                                        
* `Пример в Python:` Использование отдельного класса строителя, который шаг за                                                                        
шагом создает сложный объект, а затем возвращает его.                                                                        

```python
class House:
    def __init__(self, walls=0, doors=0, windows=0):
        self.walls = walls
        self.doors = doors
        self.windows = windows

class HouseBuilder:
    def __init__(self):
        self.house = House()

    def add_wall(self):
        self.house.walls += 1
        return self

    def add_door(self):
        self.house.doors += 1
        return self

    def add_window(self):
        self.house.windows += 1
        return self

    def build(self):
        return self.house

# Пример использования:
builder = HouseBuilder()
house = builder.add_wall().add_door().add_window().add_window().build()
print(house.windows)  # 2
```

4) **Прототип (Prototype)**                                                                                    
* `Цель:` Создать объект на основе уже существующего объекта через клонирование.                                                                                    

* `Пример в Python:` Метод **copy()** для создания поверхностной копии объекта                                                                                     
или **deepcopy()** для полного клонирования.                                                                                    

```python
import copy

class Prototype:
    def clone(self):
        return copy.deepcopy(self)

class Item(Prototype):
    def __init__(self, name, details):
        self.name = name
        self.details = details

# Пример использования:
item1 = Item("Book", ["Title: The Great Gatsby", "Author: F. Scott Fitzgerald"])
item2 = item1.clone()
item2.details.append("Publisher: Scribner")

print(item1.details)  # ['Title: The Great Gatsby', 'Author: F. Scott Fitzgerald']
print(item2.details)  # ['Title: The Great Gatsby', 'Author: F. Scott Fitzgerald', 'Publisher: Scribner']
```

5) **Адаптер (Adapter)**                                                                                    
* `Цель:` Преобразовать интерфейс одного класса в интерфейс другого. Адаптеры                                                                                    
позволяют программам работать с классами, которые иначе                                                                                     
были бы несовместимыми.                                                                                    

* `Пример в Python:` Создание класса, который реализует требуемый интерфейс                                                                                    
и использует экземпляр другого класса, чей интерфейс нужно "адаптировать".                                                                                    

```python
class OldSystem:
    def old_method(self):
        return "old method data"

class Adapter:
    def __init__(self, old_system):
        self.old_system = old_system

    def new_method(self):
        return self.old_system.old_method()

# Пример использования:
old = OldSystem()
adapter = Adapter(old)
print(adapter.new_method())  # old method data
```

---

# **Descriptors**                                                                                    

**Дескрипторы** — это мощный инструмент в **Python**, позволяющий управлять                                                                                     
поведением атрибутов объекта. Если кратко, дескриптор — это экземпляр                                                                                     
класса, реализующего один или несколько из специальных методов:                                                                                     
`__get__`, `__set__` и `__delete__`

**Как это работает?**                                                                                    

Допустим, у вас есть класс `A`, и в нём атрибут `x`, который является                                                                                     
экземпляром другого класса `B`. Если `B` реализует метод `__get__`,                                                                                     
`__set__` или `__delete__`, то `x` становится дескриптором.                                                                                    

# **Descriptor's methods**                                                                                    

* `__get__(self, instance, owner)`: Возвращает значение атрибута.                                                                                     
`instance` — это экземпляр класса, `owner` — сам класс.                                                                                    

* `__set__(self, instance, value)`: Устанавливает значение атрибута.                                                                                    

* `__delete__(self, instance)`: Удаляет атрибут.                                                                                    

```python
class Descriptor:
    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Value cannot be negative")
        self._value = value

class MyClass:
    x = Descriptor()

obj = MyClass()
obj.x = 10
print(obj.x)  # Выведет: 10
```

```python
obj.x = -2 # Вызовет исключение ValueError
```

**Зачем они нужны?**                                                                                    

Дескрипторы позволяют инкапсулировать логику управления атрибутами,                                                                                     
делая ваш код более чистым и управляемым. Например, они могут                                                                                     
использоваться для:                                                                                    

* Валидации данных при присваивании значения атрибуту.                                                                                    
* Ленивой (**отложенной**) инициализации атрибута.                                                                                    
* Журналирования или кеширования.                                                                                    

# **Problems with Descriptors**                                                                                    

**Если вы решите использовать дескрипторы, вам следует знать**                                                                                    
**о нескольких особенностях:**                                                                                    

* `Память`: Если дескрипторы хранят данные в себе, как в примере выше                                                                                     
с `_value`, это может привести к неожиданному поведению, когда у вас                                                                                    
есть несколько экземпляров `MyClass`. Каждый экземпляр будет разделять                                                                                     
одно и то же значение `_value`.                                                                                    
* `Порядок`: Дескрипторы работают только для новых стилей классов                                                                                     
(которые являются подклассами `object` в `Python 2`)                                                                                    

**Когда использовать?**
**Используйте дескрипторы, когда:**

* Вам нужно повторно использовать логику управления атрибутами в разных классах.                                                                                    
* Вы хотите разделить код, отвечающий за управление атрибутом, и код самого класса.                                                                                    


# **The Descriptor's Conclusion**                                                                                    

**Дескрипторы** — это продвинутая функция языка Python, которая может быть полезна                                                                                    
в определенных ситуациях для создания чистого и эффективного кода. Однако они                                                                                    
могут добавить сложности, если их использовать без необходимости.                                                                                    


---

# **META-classes**                                                                                    

# **What's the META-classes????**                                                                                    

В самом простом понимании, **метаклассы** — это "**классы классов**". Если класс                                                                                     
определяет, как создавать объекты и каким образом они должны вести себя,                                                                                     
то метакласс определяет, как создавать классы и как они должны вести себя.                                                                                    

**Зачем они нужны?**                                                                                    
Метаклассы позволяют контролировать процесс создания класса. Это может                                                                                    
быть полезно, например, для автоматического добавления атрибутов в                                                                                     
класс или изменения атрибутов класса при его создании.                                                                                    

**Пример:**                                                                                    
Давайте создадим метакласс, который гарантирует, что все атрибуты в                                                                                     
создаваемом классе будут в верхнем регистре.                                                                                    

```python
class UppercaseAttributesMeta(type):
    def __new__(cls, name, bases, class_dict):
        uppercase_attributes = {
            key.upper(): value for key, value in class_dict.items()
        }
        return super().__new__(cls, name, bases, uppercase_attributes)

class MyClass(metaclass=UppercaseAttributesMeta):
    lowercase_attribute = "I should be uppercase"

print(hasattr(MyClass, "lowercase_attribute"))  # False
print(hasattr(MyClass, "LOWERCASE_ATTRIBUTE"))  # True
```

В примере выше `UppercaseAttributesMeta` — это **метакласс**. При создании                                                                                     
нового класса MyClass, метакласс переопределяет все атрибуты класса так,                                                                                    
чтобы они были в верхнем регистре.                                                                                    

**Как это работает?**                                                                                    

Когда вы создаете класс с указанием метакласса, метод `__new__` метакласса                                                                                    
вызывается для создания нового класса.                                                                                    
В этом методе мы можем модифицировать атрибуты создаваемого класса                                                                                     
(в нашем примере преобразуем все ключи в верхний регистр).                                                                                    

**Важное замечание:** Несмотря на то что метаклассы могут быть мощным                                                                                     
инструментом, они также могут усложнить код и сделать его менее понятным.                                                                                    

Используйте метаклассы обдуманно и только тогда, когда они действительно необходимы.                                                                                    


**Когда метакласс создает новый класс, он использует следующие аргументы:**

* `name`: Это строка, представляющая имя создаваемого класса.                                                                                    

* `bases`: Это кортеж родительских классов. Он определяет иерархию наследования                                                                                    
создаваемого класса. Например, если создается класс, который наследуется от                                                                                     
двух других классов `Parent1` и `Parent2`, то `bases`                                                                                     
будет выглядеть так: (`Parent1`, `Parent2`).                                                                                    

* `class_dict`: Это словарь, содержащий атрибуты и методы создаваемого класса.                                                                                     
Ключами этого словаря являются имена атрибутов и методов, а                                                                                     
значениями — их соответствующие значения или функции.                                                                                    

Эти параметры позволяют метаклассу полностью                                                                                     
управлять процессом создания нового класса.                                                                                    

---

# **Imperative and declarative approach**                                                                                    

# **Imperative approach**                                                                                    

**Определение**:                                                                                     
Императивное программирование фокусируется на том, как достичь желаемого                                                                                     
результата, описывая последовательность шагов, которые должны быть выполнены.                                                                                    

**Императивный подход** — это как когда вы даёте кому-то детальные инструкции                                                                                     
по приготовлению чая шаг за шагом:                                                                                    

1) Возьми чайник.                                                                                    
2) Наполни его водой.                                                                                    
3) Поставь его на плиту.                                                                                    
4) Включи плиту.                                                                                    
5) Подожди, пока вода закипит.                                                                                    
6) Налей воду в чашку.                                                                                    
7) Положи чайный пакетик в чашку.                                                                                    

8) Пример на **Python**: Написать программу, которая инвертирует список.                                                                                    

```python
def reverse_list(input_list):
    result = []
    for item in input_list:
        result.insert(0, item)
    return result

print(reverse_list([1, 2, 3]))  # Вывод: [3, 2, 1]
```

**Здесь мы даем явные инструкции:** 

1) начните с пустого списка                                                                                    
2) затем, перебрав каждый элемент входного списка                                                                                    
3) добавьте его в начало результата.                                                                                    

**Декларативный подход**

**Декларативный стиль** — это как когда вы просто говорите: "**Сделай мне чай"**.                                                                                     
Вы не заботитесь о деталях; вы просто говорите, что хотите в итоге.                                                                                    

**Пример на Python**: Используя срезы для инвертирования списка.                                                                                    

```python
def reverse_list(input_list):
    return input_list[::-1]

print(reverse_list([1, 2, 3]))  # Вывод: [3, 2, 1]
```

Здесь мы не говорим, как именно инвертировать список. Мы просто говорим                                                                                     
**Python**, что хотим получить элементы в обратном порядке.                                                                                    

**Другие примеры:**                                                                                    


**Императивно:**                                                                                    

**Найти все числа от 1 до 100, которые делятся на 7.**                                                                                    

```python
result = []
for i in range(1, 101):
    if i % 7 == 0:
        result.append(i)
print(result)
```

**Декларативно:**                                                                                    

**Используя генератор списков.**                                                                                    

```python
result = [i for i in range(1, 101) if i % 7 == 0]
print(result)
```

**Императивно**:                                                                                    

**Преобразовать все слова в списке к верхнему регистру.**                                                                                    

```python
words = ["apple", "banana", "cherry"]
for i in range(len(words)):
    words[i] = words[i].upper()
print(words)
```

**Декларативно:**                                                                                    

**Используя map() и lambda.**                                                                                    

```python
words = ["apple", "banana", "cherry"]
words = list(map(lambda word: word.upper(), words))
print(words)
```

# **Declarative VS Imperative**                                                                                    

* `Читаемость`: Декларативный код часто короче и легче для чтения, особенно                                                                                     
когда используются хорошо известные структуры или функции.                                                                                    

* `Контроль`: Императивный подход даёт больше контроля над тем, как                                                                                     
выполняется каждый шаг, что может быть полезно в определённых ситуациях.                                                                                    

* `Эффективность`: Императивный код может быть более эффективным в некоторых                                                                                     
случаях, так как программист имеет полный контроль над алгоритмом.                                                                                    
В то время как декларативный код полагается на внутренние реализации,                                                                                     
которые могут быть неоптимальными.                                                                                    

* `Написание`: Декларативный код может быть быстрее и проще для                                                                                     
написания, особенно для стандартных задач.                                                                                    

---

**В каких ситуациях мы сталкиваемся с этим?**                                                                                    

**Базы данных**: `SQL` — это хороший пример декларативного языка. Когда вы                                                                                    
запрашиваете `SELECT * FROM table WHERE condition`, вы не указываете, как                                                                                    
база данных должна извлекать данные, вы просто указываете,                                                                                    
какие данные вам нужны.                                                                                    

**Frontend разработка**: Когда вы используете `CSS` для стилизации веб-страниц,                                                                                     
вы декларативно описываете, как элементы должны выглядеть, а не то,                                                                                     
как браузер должен это рисовать.                                                                                    

**Функциональное программирование**: Многие функциональные языки имеют                                                                                     
декларативное уклон. `Haskell` или `Erlang` — хорошие примеры.                                                                                    

**Скриптовые языки**: `Bash` и другие скриптовые языки часто                                                                                     
используют декларативный стиль.                                                                                    

---

**Зачем придумали эти подходы?**

* `Читаемость`: Декларативный код часто короче и легче читается,                                                                                     
что упрощает обслуживание.                                                                                    

* `Переиспользуемость`: Императивный код иногда проще адаптировать к                                                                                     
новым условиям или переиспользовать в другом контексте.                                                                                    

* `Оптимизация`: Когда система знает, чего вы хотите (декларативный стиль),                                                                                    
а не то, как вы этого достигаете (императивный стиль), она может                                                                                     
автоматически оптимизировать процесс.                                                                                    

---

**Как это помогает в работе?**
* `Быстродействие`: В некоторых случаях декларативный подход позволяет                                                                                     
системам автоматически оптимизировать выполнение задач.                                                                                    

* `Меньше ошибок`: Меньше шагов часто означает меньше возможностей для ошибок.                                                                                    

* `Сотрудничество`: Простой и понятный код легче обсуждать с коллегами.                                                                                    

---

**Как принимать решение, какие подходы где использовать?**                                                                                    

* `Задача`: Если задача стандартная и хорошо определена (например, обработка                                                                                     
данных), декларативный подход может быть более уместным. Если требуется                                                                                     
тонкая настройка или специфические шаги, императивный подход может быть лучше.                                                                                    

* `Инструменты`: Используйте инструменты или языки, которые вы знаете. Например,                                                                                    
если вы знаете SQL, вы будете использовать декларативный подход для                                                                                     
работы с базами данных.                                                                                    

* `Производительность`: Если производительность критична и вы знаете, что                                                                                    
можете написать более быстрый код, выберите императивный стиль.                                                                                    

* `Команда`: Ваш выбор может зависеть от предпочтений вашей команды                                                                                     
и используемых инструментов.                                                                                    

# **Imperative, and Declarative approach conclusion**                                                                                    

`Императивный подход`: как рецепт с пошаговыми инструкциями.                                                                                    

`Декларативный подход`: как заказ в ресторане. Вы говорите, что                                                                                     
хотите, и ожидаете получить это, не заботясь о деталях процесса.                                                                                    


Оба стиля имеют свои преимущества. Иногда важно контролировать                                                                                     
каждый шаг (**императивный**), а иногда проще и понятнее просто указать,                                                                                    
что вы хотите получить на выходе (**декларативный**).                                                                                    

Выбор между императивным и декларативным подходами зависит от конкретной                                                                                    
задачи, контекста и личных предпочтений программиста. Важно понимать                                                                                     
разницу между этими подходами, чтобы выбирать наиболее подходящий                                                                                    
стиль для каждой ситуации.                                                                                    
