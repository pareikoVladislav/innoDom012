<!-- TOC -->
* [**FUNCTIONS**](#functions)
* [**Function methodology principles**](#function-methodology-principles)
* [**Named, and anonymous functions**](#named-and-anonymous-functions)
* [**Named Functions**](#named-functions)
* [**Anonymous functions**](#anonymous-functions)
* [**Lambda rules!**](#lambda-rules-)
* [**Function Arguments**](#function-arguments)
* [**Functions documentation**](#functions-documentation-)
* [**Built-in powerful python functions**](#built-in-powerful-python-functions)
* [**Practice**](#practice)
<!-- TOC -->

# **FUNCTIONS**

В целом программирование делиться на Функциональный (всё через             
~~жопу~~ функции) и Объектно-ориентированный (всё через классы) принципы                 
разработки.                                


**Функциональное программирование (Functional Programming)** - это                               
парадигма программирования, основанная на использовании функций в                              
качестве основных строительных блоков и ограничении изменяемого                         
состояния и изменяемости данных.                           


В наших парадимгах программирования есть свои принципы, своего                 
рода правила.                                 


# **Function methodology principles**


**Что за принципы функциональной разработки:**                                    

* **Неизменяемость данных:** Данные в функциональном программировании обычно                              
являются неизменяемыми (**immutable**), то есть их нельзя изменять после                         
создания. Вместо этого операции создают новые данные, основываясь                          
на существующих.                                 

Это устраняет проблемы с параллельным выполнением и побочными эффектами,                         
такими как гонки данных (**race conditions**) или неопределенное поведение.                          


* **Чистота функций:** Функции в функциональном программировании не должны                        
зависеть от состояния программы или изменяемых данных. Они принимают                      
входные значения и возвращают результаты, не изменяя состояние внешнего                    
окружения. Это делает функции предсказуемыми и легко тестируемыми.                               

  
Функция может считаться чистой, если при вводе одних и тех же параметрах будет                          
выдавать один и тот же результат, не вызывая побочных эффектов                              

**Пример чистой функции:**                             

```python
def my_clear_function(a, b):
    return a + b
```


А вот как может выглядеть **"грязная"** функция:                            

```python
total = 0

def my_dirty_function(a, b):
    global total
    total += a + b

    return total
```


* **Применение функций высшего порядка:** Функции в функциональном                            
программировании могут принимать другие функции в качестве аргументов                             
или возвращать их в качестве результатов. Это позволяет строить                           
абстракции и комбинировать функции для решения сложных задач.                            


---

**Плюсы написания чистых функций:**                                 


1) **Тестируемость**                        
Так как на функцию не будет влиять что-то извне и она всегда будет                      
выдавать один и тот же **"ожидаемый"** результат (функция зависит только                         
от аргументов) - эту функцию будет достаточно легко протестировать.                       

2) **Модульность**                          
Чистые функции являются модульными, что означает, что мы можем повторно                         
использовать их в различных частях файлов внутри проекта, не беспокоясь                      
при этом о побочных эффектах, или неожиданных взаимодействиях                             
с другим кодом.                            

3) **Парраллелизм**                             
Поскольку чистые функции не зависят от внешнего состояния и производят                                
один и тот же вывод для одних и тех же входных данных - их можно                                
безопасно выполнять парраллельно без риска возникновения **RaceConditions**,                              
или других проблем с синхронизацией                              

4) **Кэширование**                              
Благодаря тому, что чистые функции всегда выдают одни и теже выходные                             
данные для одних и тех же входных данных - мы можем кэшировать                            
результаты выполнения для повышения производительности.                               

5) **Лёгкость в понимании**                          
Такие функции банально проще понимать, когда в них нет ничего лишнего.                       


**Но не всё так сладко, у чистых функций так же есть и минусы:**                            


1) **Могут привести к более сложному коду**                                      
Чрезмерное использование чистых функций может привести к усложнению                        
кода (часто требуют большого количества параметров и создания                        
большого количества переменных)                            

2) **Не могут иметь побочных эффектов**                                  
Они не могут изменять переменных за пределами своей области видимости.                               
Это может привести к затруднению выполнения некоторых операций                             
( операции ввода-вывода )                                 

3) **Могут требовать больше памяти**                                    
Из-за того, что они могут создавать дополнительные структуры данных                        
для хранения промежуточных результатов.                                  

4) **Могут работать медленнее, особенно с большими объёмами данных**                                                        


---

# **Named, and anonymous functions**

**Именованная функция** – это функция, которая заключает в себе код                    
под именем для выполнения какого-то действия.                           

Функция может принимать аргументы, а может не принимать их                           


**Функции, с которыми вы уже знакомы и которые уже использовали в работе:**                          

```python
# приведение типов
# (int(), str(), float(), bool()...)
print()
input()
range()
type()
```

# **Named Functions**

```python
def sum_two_values(value_1: int, value_2: int) -> int:
  return value_1 + value_2
```

Функция должна возвращать результат своего выполнения, если она                      
ничего не возвращает, то такие функции называют **процедурами**.                                 

Обычно **процедуры** используются, когда нужно сделать вывод какой-либо                     
структуры либо запуск программ основных функций, чаще всего их                     
называют **main**


```python
def greeting():
  print("Hello, World!")
```

```python
import json


def write_data_in_file(file, data):
    with open(file, "w") as target_file:
        json.dump(target_file, data)
```

# **Anonymous functions**

Так же наши функции могут быть неименованными. В том же **JS** такие                              
функции называются **стрелочными**. В языке **Python** такие функции                          
называются **анонимными**.                                  

Для того, чтобы написать такую функцию существует ключевое слово                               
`lambda`.                                  

**Каков синтаксис?**                                 

`lambda <ваши аргументы через запятую, или без аргументов>: результат с этими аргументами`

```python
a = lambda x, y: x ** y
```

Такая запись будет полностью аналогичной записи обычной именованной функции:                         
```python
def sqrt_vals(x, y):
    return x ** y
```

Лямбды помогают нам сократить код выполнения обычной функции. Они крайне хорошо                    
показывают себя внутри очень мощных, встроенных функций в Питоне, о которых                            
поговорим троху позже.                       

# **Lambda rules!**                        
Если ваша лямбда становится слишком "тяжёлой", слишком сложной для понимания,                            
а логика выполнения представляется более, чем в одну строчку - откажитесь                               
от такой реализации и лучше напишите обычную, именованную функцию.                   


Лямбды хороши, когда логику выполнения функции можно представить в одну                           
строчку, без каких-то сложных структурных действий.                                

---


# **Function Arguments**


Функция может принимать в себя **аргументы** (**параметры**), это те                 
элементы с которыми функция будет работать. В Python у функций                
существует 2 типа аргументов: **args** и **kwargs**.

**Args** - это обычные порядковые аргументы, которые мы                     
передаем в функцию.

```python
def sum_list_values(values: list) -> int:
  result = sum(values)

  return result

sum_list_values([2, 4, 6, 8, 10])
```


Если вы не знаете, как много порядковых аргументов будет приходить              
в функцию - можно указать в аргументах просто `*args`

```python
def sum_mean_of_values(*args):
  print(type(args))
  result = sum(args) // len(args)

  return result

sum_mean_of_values(2, 8, 4)
```

такие аргументы обязательно записываются в строгом порядке                   


**Kwargs** - это именнованные аргументы которые мы передаем в функцию
именнованные аргументы могут указываться в любом порядке

```python
def calculate_three_values(arg_1: int, arg_2: int, arg_3: int) -> int:
  return arg_1 + arg_2 - arg_3


calculate_three_values(arg_3=8, arg_1=5, arg_2=10)
```

Если вы не знаете, как много именных аргументов будет приходить в вашу                       
функцию - можно воспользоваться аргументом `**kwargs`
При этом всём доступ к значениям мы можем получать через обращение к этому                    
аргументу через метод `.get()`

```python
def calculate_three_values_2(**kwargs) -> int:
  print(type(kwargs))
  result = kwargs.get("a") + \
  kwargs.get("b") + kwargs.get("c") + kwargs.get("d")

  return result


calculate_three_values_2(a=2, b=4, c=6, d=8)
```

Можно передавать и те, и те аргументы одновременно.

Когда указываем разные по характеру аргументы, то сначала передаем                   
args-аргументы(порядковые), а только потом kwargs(именнованные)


Аргументы могут быть заданы по умолчанию, в случае, если такой параметр не                       
будет передан в функцию, она возьмет значение по умолчанию этого аргумента.                  

Всегда, с самого начала, указываются аргументы без, а потом с                         
значениями по умолчанию, иначе исключение                        

```python
def multiply_list_values(list_: list, value: int=4) -> list:
  new_list = []

  for i in list_:
    new_list.append(i * value)

  return new_list


multiply_list_values([1, 2, 3, 4, 5], value=5)
```

**Args** и **kwargs** позволяют забрать незарезервированные аргументы,                      
передаваемые в функцию.                          
**args** поедставляют ваши аргументы виде кортежа, позволяют при этом                              
передавать сколько угодно позиционных аргументов.                                    

**Kwargs** позволяют передавать сколько угодно именованных аргументов                                
**kwargs** представляют ваши аргументы в виде словаря                          

```python
def show_args_kwargs_work(*args, **kwargs):
  args_list = []
  kwargs_list = []

  for arg in args:
    args_list.append(arg ** 2)

  for key, value in kwargs.items():
    kwargs_list.append(value ** .5)

  return args_list, kwargs_list


show_args_kwargs_work(6, 8, a=5, b=15)
```

Когда функция возвращает какие-либо данные, она завершает своё выполнение.                             
В зависимости от условия, функция может возвращать разные данные.                      

```python
def return_any_value(a, b):
  if a > b:
    return a // b
  return a * b

return_any_value(9, 84)
```

Также **return** может возвращать несколько значений в виде кортежа,                      
все значения перечисляются через запятую.

```python
def return_two_values(a, b):
  return a, b


first_val, second_val = return_two_values(
    input("Enter some value: "),
    int(input("Enter new value: "))
)
```

---

# **Functions documentation**                                             

Python позволяет для функций создавать строки документации.                     
Они позволяют быстро и просто документировать ваши функции

```python
def return_many_values(value_1: int, value_2: int) -> tuple:
    """
    Calculate the summary and exponentiation of two integers.

    Args:
        value_1 (int): The first integer value.
        value_2 (int): The second integer value.

    Returns:
        tuple: A tuple containing two values:
            - summary (int): The sum of value_1 and value_2.
            - exponentiation (int): The result of value_1 raised                      
            to the power of value_2.
    """
    summary = value_1 + value_2
    exponentation = value_1 ** value_2

    return summary, exponentation
```

---

# **Built-in powerful python functions**

Так же есть встроенные функции, которые помогают в разы сократить                   
ваш код. Эти функции частенько спрашивают на собеседованиях                  
для проверки знаний и понимания языка:

1) `map(function, iterable)` - применяет указанную функцию **function**                      
к каждому элементу итерируемого объекта **iterable** и возвращает                   
итератор с результатами.

**Arguments**:

* `function`: Функция, которая будет применяться к парам элементов.
* `iterable`: Итерируемый объект, например, список или кортеж

```python
numbers = [2, 4, 6, 8, 10]

def square(x):
  return x ** 2


squared_numbers = map(square, numbers)
squared_numbers_2 = map(lambda x: x ** 2, numbers)
print(list(squared_numbers))
print(list(squared_numbers_2))
```

```python
user_numbers = input()

string_to_int = list(map(int, user_numbers.split(", ")))
```

2) `filter(function, iterable)` - применяет указанную функцию **function**                            
к каждому элементу итерируемого объекта **iterable** и возвращает итератор                       
с элементами, для которых функция возвращает **True**


**Arguments**:

`function`: Функция, которая будет применяться к парам элементов.
`iterable`: Итерируемый объект, например, список или кортеж.


```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def is_even(x):
  return x % 2 == 0

even_numbers = filter(is_even, numbers)

even_numbers_ = filter(lambda x: x % 2 == 0, numbers)

print(list(even_numbers))
print(list(even_numbers_))
```

```python
user_text = input()

filtered_text = filter(lambda x: x.isdigit(), user_text)

print(list(filtered_text))
```


3) `reduce(function, iterable, initializer)` - применяет указанную                    
функцию **function** к парам элементов из итерируемого объекта **iterable**                    
и последовательно сворачивает их в одно значение. Она требует                   
модуля **functools** для использования.


**Arguments**:

* `function`: Функция, которая будет применяться к парам элементов.                 
* `iterable`: Итерируемый объект, например, список или кортеж.                      
* `initializer` (**необязательный**): Начальное значение для свертки.                      
Если не указано, то первая пара элементов будет использоваться                     
в качестве начального значения.

```python
from functools import reduce
numbers_ = [1, 2, 3, 4, 5]
numbers_3 = [2, 4, 6, 8, 10]
letters = ["h", "e", "l", "l", "o"]


def multiply_(x, y):
  return x * y


def concatinate(x, y):
  return x + y


res_1 = reduce(multiply_, numbers_)
res_2 = reduce(multiply_, numbers_3, 4)
res_3 = reduce(concatinate, letters)

print(res_1)
print(res_2)
print(res_3)
print("-" * 45)
print(1 * 2 * 3 * 4 * 5)
print("-" * 45)
print(4 * 2 * 4 * 6 * 8 * 10)
print("-" * 45)
```

4) `zip(*iterables)` - объединяет элементы из нескольких итерируемых                     
объектов и создает итератор с кортежами, содержащими элементы из                 
каждого итерируемого объекта.                 

**Arguments**:

`iterables`: Один или более итерируемых объектов, например,                   
списки или кортежи.                  


```python
letters = ["a", "b", "c"]
numbers_ = [1, 2, 3]

my_zip_1 = zip(letters, numbers_)
my_zip_2 = zip(letters)
my_zip_3 = zip(numbers_)

print(list(my_zip_1))
print(dict(zip(letters, numbers_)))
print(tuple(my_zip_2))
print(set(my_zip_3))
```

5) `sorted(iterable, key=None, reverse=False)` - сортирует элементы                    
итерируемого объекта и возвращает новый отсортированный список.

**Arguments**:

* `iterable`: Итерируемый объект, например, список или кортеж.                 
* `key` (**необязательный**): Функция, по которой производится                     
сортировка элементов.
* `reverse` (**необязательный**): Если установлено значение **True**,                  
элементы сортируются в обратном порядке.

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
new_list = ["Mother", "Adutant", "Motor", 4, 7, "Banana", "Pineaple", "Qiwi"] # будет алярма, так как должен быть объект с каким-то конкрэтным типом данных
new_list_2 = ["Mother", "Adutant", "Motor", "Banana", "Pineaple", "Qiwi"] # всё оке

sorted_list = sorted(new_list, reverse=True)

print(list(sorted_list))
```

6) `enumerate(iterable, start=0)` - возвращает объект-перечислитель,                      
который генерирует пары индекс-элемент для элементов                        
итерируемого объекта

**Arguments**:

* `iterable`: Итерируемый объект, например, список или кортеж.                     
* `start` (необязательный): Начальное значение индекса.                     
По умолчанию равно 0.                      

```python
some_list = ["Alex", "Dan", "Anya", "Olya", "Irina", "Vladislav"]

for index, name in enumerate(some_list, start=1):
  print(f"Индекс: {index}. Элемент индекса: {name}")
```

Старайтесь удерживать в голове, при работе с этими мощными функциями,                    
что они возвращают вам объект, класса функции, а не как можно по началу                    
ожидать, сразу результат. Если вам нужно отпринтить результат -                     
приводите его к нужному вам типу (с учётом того, к какому типу                    
его можно привести, само собой)

---

# **Practice**

1) Написать функцию, которая принимает произвольное количество                      
аргументов и возвращает их среднее значение.

2) Написать функцию, которая принимает строку с паролем и возвращает                   
**True**, если пароль соответствует определенным критериям безопасности,                
и **False** в противном случае.

**Критерии безопасности включают следующее:**

**Длина пароля должна быть не менее 8 символов.**
**Пароль должен содержать как минимум одну заглавную и одну строчную букву.**
**Пароль должен содержать как минимум одну цифру и один символ.**

Для упрощения задачи - что может входить в пароль
```python
  is_alnum_reg = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)"
  symbol_reg = r"[!@#$%^&*?_|<>{}]"
```

3) Есть список словарей, где каждый словарь представляет один                    
продукт со следующими полями: `name`, `price` и `available`.

Написать функцию, которая принимает этот список продуктов и возвращает                     
новый список, содержащий только те продукты, которые есть в наличии                  
и их цена не превышает 1000 рублей.

```python
products = [
    {"name": "Smart TV", "price": 130, "available": True,},
    {"name": "Wireless Bluetooth Headphones", "price": 220, "available": False,},
    {"name": "Laptop", "price": 14, "available": True,},
    {"name": "Digital Camera", "price": 432, "available": False,},
    {"name": "Gaming Console", "price": 556, "available": True,},
    {"name": "Smartwatch", "price": 170, "available": False,},
    {"name": "Portable Bluetooth Speaker", "price": 130, "available": False,},
    {"name": "Drone", "price": 854, "available": True,},
    {"name": "Virtual Reality Headset", "price": 945, "available": False,},
    {"name": "Wireless Earbuds", "price": 1500, "available": True,},
    {"name": "Tablet", "price": 894, "available": True,},
    {"name": "Smart Home Security System", "price": 135, "available": False,},
    {"name": "Fitness Tracker", "price": 25, "available": True,},
    {"name": "External Hard Drive", "price": 659, "available": False,},
    {"name": "Bluetooth Keyboard", "price": 2654, "available": False,},
    {"name": "Noise-Canceling Headphones", "price": 819, "available": True,},
    {"name": "Action Camera", "price": 9511, "available": True,},
    {"name": "Wi-Fi Router", "price": 9156, "available": True,},
    {"name": "Gaming Mouse", "price": 123, "available": True,},
    {"name": "Wireless Charging Pad", "price": 10125, "available": False,},
    {"name": "Sofa bed", "price": 945, "available": True,},
    {"name": "Dining table", "price": 12, "available": False,},
    {"name": "Wardrobe", "price": 85, "available": False,},
    {"name": "Coffee table", "price": 73, "available": True,},
    {"name": "Recliner chair", "price": 856, "available": False,},
    {"name": "Bookcase", "price": 1500, "available": True,},
    {"name": "Bed frame", "price": 999, "available": True,},
    {"name": "Dressing table", "price": 12, "available": False,},
    {"name": "TV stand", "price": 3, "available": False,},
    {"name": "Ottoman", "price": 84, "available": True,},
]
```

4) Есть список словарей, где каждый словарь представляет                    
один заказ со следующими полями: '`id`', '`table_number`' и '`bill`'.

Написать функцию, которая принимает этот список заказов и                    
возвращает новый список заказов, отсортированный по                
возрастанию суммы заказа.                    

```python
orders = [
    {'id': 1, 'table_number': 5, 'bill': 25.50},
    {'id': 2, 'table_number': 10, 'bill': 42.75},
    {'id': 3, 'table_number': 3, 'bill': 15.20},
    {'id': 4, 'table_number': 8, 'bill': 37.90},
    {'id': 5, 'table_number': 2, 'bill': 10.50},
    {'id': 6, 'table_number': 12, 'bill': 55.80},
    {'id': 7, 'table_number': 6, 'bill': 29.95},
    {'id': 8, 'table_number': 9, 'bill': 41.10},
    {'id': 9, 'table_number': 4, 'bill': 19.75},
    {'id': 10, 'table_number': 7, 'bill': 34.60},
    {'id': 11, 'table_number': 1, 'bill': 8.25},
    {'id': 12, 'table_number': 11, 'bill': 50.40},
    {'id': 13, 'table_number': 5, 'bill': 25.00},
    {'id': 14, 'table_number': 10, 'bill': 43.25},
    {'id': 15, 'table_number': 3, 'bill': 16.80},
    {'id': 16, 'table_number': 8, 'bill': 38.50},
    {'id': 17, 'table_number': 2, 'bill': 11.75},
    {'id': 18, 'table_number': 12, 'bill': 56.20},
    {'id': 19, 'table_number': 6, 'bill': 30.50},
    {'id': 20, 'table_number': 9, 'bill': 42.90},
    {'id': 21, 'table_number': 4, 'bill': 20.25},
    {'id': 22, 'table_number': 7, 'bill': 35.10},
    {'id': 23, 'table_number': 1, 'bill': 9.75},
    {'id': 24, 'table_number': 11, 'bill': 51.60},
    {'id': 25, 'table_number': 5, 'bill': 25.50},
    {'id': 26, 'table_number': 10, 'bill': 42.75},
    {'id': 27, 'table_number': 3, 'bill': 15.20},
    {'id': 28, 'table_number': 8, 'bill': 37.90},
    {'id': 29, 'table_number': 2, 'bill': 10.50},
    {'id': 30, 'table_number': 12, 'bill': 55.80}
]
```

5) Есть список словарей, где каждый словарь представляет                
одного клиента со следующими полями: '`id`', '`name`', '`age`' и '`sex`'.                       

Написать функцию, которая принимает этот список клиентов и                 
возвращает количество женщин в списке.                   

```python
clients = [
    {'id': 1, 'name': 'Alice', 'age': 32, 'sex': 'Female'},
    {'id': 2, 'name': 'Bob', 'age': 45, 'sex': 'Male'},
    {'id': 3, 'name': 'Charlie', 'age': 28, 'sex': 'Male'},
    {'id': 4, 'name': 'David', 'age': 54, 'sex': 'Male'},
    {'id': 5, 'name': 'Eva', 'age': 39, 'sex': 'Female'},
    {'id': 6, 'name': 'Frank', 'age': 42, 'sex': 'Male'},
    {'id': 7, 'name': 'Grace', 'age': 61, 'sex': 'Female'},
    {'id': 8, 'name': 'Henry', 'age': 50, 'sex': 'Male'},
    {'id': 9, 'name': 'Isabella', 'age': 26, 'sex': 'Female'},
    {'id': 10, 'name': 'Jack', 'age': 33, 'sex': 'Male'},
    {'id': 11, 'name': 'Kate', 'age': 49, 'sex': 'Female'},
    {'id': 12, 'name': 'Liam', 'age': 23, 'sex': 'Male'},
    {'id': 13, 'name': 'Mia', 'age': 37, 'sex': 'Female'},
    {'id': 14, 'name': 'Noah', 'age': 58, 'sex': 'Male'},
    {'id': 15, 'name': 'Olivia', 'age': 41, 'sex': 'Female'},
    {'id': 16, 'name': 'Peter', 'age': 31, 'sex': 'Male'},
    {'id': 17, 'name': 'Quinn', 'age': 56, 'sex': 'Female'},
    {'id': 18, 'name': 'Ryan', 'age': 35, 'sex': 'Male'},
    {'id': 19, 'name': 'Sophia', 'age': 47, 'sex': 'Female'},
    {'id': 20, 'name': 'Thomas', 'age': 29, 'sex': 'Male'},
    {'id': 21, 'name': 'Uma', 'age': 60, 'sex': 'Female'},
    {'id': 22, 'name': 'Victoria', 'age': 44, 'sex': 'Female'},
    {'id': 23, 'name': 'William', 'age': 52, 'sex': 'Male'},
    {'id': 24, 'name': 'Xavier', 'age': 36, 'sex': 'Male'},
    {'id': 25, 'name': 'Yara', 'age': 30, 'sex': 'Female'},
    {'id': 26, 'name': 'Zoe', 'age': 43, 'sex': 'Female'},
    {'id': 27, 'name': 'Alex', 'age': 27, 'sex': 'Male'},
    {'id': 28, 'name': 'Benjamin', 'age': 48, 'sex': 'Male'},
    {'id': 29, 'name': 'Chloe', 'age': 38, 'sex': 'Female'},
    {'id': 30, 'name': 'Daniel', 'age': 55, 'sex': 'Male'}
]
```

`**`
6) Работаем над системой анализа текста.
Написать функцию, которая принимает текстовую строку и список                     
стоп-слов (слов, которые не несут смысловой нагрузки \ оскорбления \ "нежелательные"),                    
и возвращает новую строку, в которой удалены все стоп-слова                           
из исходного текста
