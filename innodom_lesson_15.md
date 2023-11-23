<!-- TOC -->
* [**Multiple Inheritance, Mixins**](#multiple-inheritance-mixins-)
* [**Advantages of Multiple Inheritance**](#advantages-of-multiple-inheritance-)
* [**Disadvantages of Multiple Inheritance**](#disadvantages-of-multiple-inheritance-)
* [**How to fix a diamond problem?**](#how-to-fix-a-diamond-problem-)
* [**Mixins**](#mixins-)
* [**Mixins Advantages**](#mixins-advantages-)
* [**Important points while using mixins**](#important-points-while-using-mixins-)
<!-- TOC -->

# **Multiple Inheritance, Mixins**                                                                                 

**Множественное наследование** в программировании — это возможность                                                        
класса наследовать свойства и методы **БОЛЕЕ** чем от одного родительского                                                                                  
класса. Эта возможность существует в некоторых объектно-ориентированных                                                                                    
языках программирования, включая **Python**.                                                                                 


**Множественное наследование** предоставляет возможность создавать новый класс                                                                                  
на основе нескольких существующих классов. Этот новый класс будет содержать                                                                              
совокупность атрибутов и методов всех его родительских классов.                                                                                             

```python
class A:
    def method_A(self):
        return "Method of class A"

class B:
    def method_B(self):
        return "Method of class B"

# Класс C наследует свойства и методы и от A, и от B
class C(A, B):
    pass

c = C()
print(c.method_A())
print(c.method_B())
```

# **Advantages of Multiple Inheritance**                                                                                      

* `Повторное использование кода:`                                                                                          
Вместо копирования и вставки кода из одного класса в другой, вы можете просто                                                                                      
наследовать необходимые свойства и методы от нескольких классов, обеспечивая                                                                                      
тем самым более чистую и организованную структуру кода.                                                                                       

* `Увеличение гибкости программы:`                                                                                                  
Позволяет создавать более специализированные и адаптированные объекты,                                                                                       
объединяя различные свойства и методы в одном классе.                                                                                              

* `Увеличение производительности:`                                                                                       
Позволяет избежать дублирования кода, что может привести к уменьшению                                                
размера программы и увеличению производительности.                                                                     

* `Увеличение читаемости кода:`                                                                       
Позволяет создавать более чистый и организованный код, что делает его более                                            
читабельным и понятным.                                                             

* `Увеличение масштабируемости:`                                                           
Позволяет создавать более гибкие и адаптируемые программы, которые могут быть                                                         
легко изменены в будущем.                                                                               



# **Disadvantages of Multiple Inheritance**                                                                                               

* `Diamond Problem" (или проблема ромба):`                                                                                          
Проблема алмаза в ООП возникает в множественном наследовании, когда класс                                                                                               
наследуется от двух классов, которые имеют общего родителя. Если метод вызывается                                                                                              
у объекта подкласса, то возникает вопрос: какой метод следует вызвать – из                                                                                               
одного суперкласса или из другого?                                                                                                                         


Python использует алгоритм C3 для определения порядка разрешения методов                                                                                                             
(Method Resolution Order, MRO), который гарантирует, что метод будет вызван                                                                                                            
только один раз и что порядок вызова методов будет сохранять локальную                                                                                                             
предпочтительность. Это значит, что если класс D наследуется от B и C, а оба эти                                                                                                             
класса наследуются от A, то при вызове метода у D он сначала будет искаться                                                                                                             
в D, затем в B, затем в C, и только потом в A.                                                                                                            

Проблема алмаза (Diamond Problem) - это термин, используемый в контексте                                                                                                    
множественного наследования в объектно-ориентированном программировании. Она                                                                                                   
возникает, когда один класс наследуется от двух классов, которые, в свою очередь,                                                                                                    
наследуются от одного и того же базового класса. На диаграмме классов это                                                                                                   
выглядит как ромб (или алмаз), отсюда и название.                                                                                                   

```
      A
     / \
    B   C
     \ /
      D
```

Проблема возникает, когда метод вызывается на экземпляре класса D. Если этот метод                                                                                              
определен и в классе B, и в классе C, то не всегда очевидно, какой из них                                                                                              
следует использовать.                                                                                             

Python решает проблему алмаза при помощи MRO (Method Resolution Order), или "порядка                                                                                             
разрешения методов". MRO определяет порядок, в котором Python будет искать                                                                                              
методы при их вызове.                                                                                             

В Python используется алгоритм C3 линеаризации для определения MRO.                                                                                              
Этот алгоритм обеспечивает два свойства:                                                                                             

1) Если класс C наследуется от класса C1 и класса C2, то C1 всегда будет                                                                                              
искаться перед C2.                                                                                             
2) Если класс C1 наследуется от класса C2, то C1 всегда будет искаться перед C2.                                                                                             

Таким образом, в Python проблема алмаза решается путем четкого                                                                                              
определения порядка, в котором следует искать методы.                                                                                             

```python
class A:
    def foo(self):
        print("A's foo()")

class B(A):
    def foo(self):
        print("B's foo()")

class C(A):
    def foo(self):
        print("C's foo()")

class D(B, C):
    pass

d = D()
d.foo()
```

В этом примере класс D наследуется от классов B и C, которые оба наследуются от                                                                             
класса A. Каждый из классов A, B и C имеет метод foo(). Когда мы вызываем foo()                                                                              
на объекте класса D, Python сначала ищет этот метод в классе B, так как он                                                                             
указан первым в списке базовых классов класса D.                                                                             

**другой пример:**                                                                            

```python
class Transistor:
    def signal(self):
        print('Transistor signal')


class Screen(Transistor):
    def display(self):
        print('Screen display')


class Processor(Transistor):
    def signal(self):
        print('Processor signal')


class Phone(Screen, Processor):
    def switch_on(self):
        self.signal()


phone = Phone()
phone.switch_on()
```

**Здесь можно увидеть в каком порядке Python ищет методы с классе:**                                                                            

```python
Phone.mro()

# [__main__.Phone,
#  __main__.Screen,
#  __main__.Processor,
#  __main__.Transistor,
#  object]
```

```python
class O:
    pass

class A(O):
    pass

class B(O):
    pass

class C(A):
    pass

class D(B):
    pass

class E(C, D):
    pass

E.mro()

# [__main__.E,
#  __main__.C,
#  __main__.A,
#  __main__.D,
#  __main__.B,
#  __main__.O,
#  object]
```

```
        O
       / \
      A   B
      |   |
      C   D
       \ /
        E
```

При этом любой из классов такой иерархии так же может нуждаться в вызове метода(ов) из                                                                                  
базового класса(класса-родителя). Что можно сделать, если каждый из классов                                                                                     
в иерархии хочет вызвать в себе какой-то метод из родительского?                                                                                      

В теории, мы можем прописать похожую логику в каждом из классов:                                                                                      

```python
class Animal:
    def set_health(self, health):
        print('set in animal')

class Carnivour(Animal):
    def set_health(self, health):
        Animal.set_health(self, health)
        print("set in carnivour")
        
class Mammal(Animal):
    def set_health(self, health):
        Animal.set_health(self, health)
        print("set in mammal")

class Dog(Mammal, Carnivour):
    def set_health(self, health):
        Mammal.set_health(self, health)
        Carnivour.set_health(self, health)
        print("set in dog")
```

От тут мы можем столкнуться с проблемой того, что наш базовый класс будет                                                                                   
вызван два раза. А это уже такое себе с точки зрения багов и в целом не                                                                                       
особо понятно зачем, собственно, нам инициализировать базовый класс дважды.                                                                                    

# **How to fix a diamond problem?**                                                                          

Начиная с `Python3` эта проблема решается при помощи функции `super()`                                                                              


```python
class Animal:
    def set_health(self, health):
        print('set in animal')

class Carnivour(Animal):
    def set_health(self, health):
        super().set_health(health)
        print("set in carnivour")
        
class Mammal(Animal):
    def set_health(self, health):
        super().set_health(health)
        print("set in mammal")

class Dog(Mammal, Carnivour):
    def set_health(self, health):
        super().set_health(health)
        print("set in dog")
```

Эта функция даёт нам с вами гарантии последовательности вызовов.                                                                                      
Как правило чаще всего этот метод вы будете встречать именно при                                                                                   
написания метода `__init__(self)`, так как зачастую класс-наследник зависит от                                                                               
базового класса, опираясь на какие-то его методы. Прежде чем использовать                                                                              
функционал базового класса класс-наследник "хотел бы" проиницилизировать                                                                                 
этот класс.                                                                                          

* `Сложность отслеживания зависимостей:`                                                                                            
В сложных системах с множественным наследованием может быть трудно определить,                                                                                       
откуда происходит определенное поведение или свойство, особенно если                                                                                          
родительские классы изменяются в разное время или разными                                                                                      
командами разработчиков.                                                                                           


```python
class Person:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Name: {self.name}")


class ContactDetails:
    def __init__(self, phone):
        self.phone = phone

    def display(self):
        print(f"Phone: {self.phone}")


class FinancialDetails:
    def __init__(self, balance):
        self.balance = balance

    def display(self):
        print(f"Balance: ${self.balance}")


class Employee(Person, ContactDetails):
    def __init__(self, name, phone, position):
        Person.__init__(self, name)
        ContactDetails.__init__(self, phone)
        self.position = position


class Investor(Person, FinancialDetails):
    def __init__(self, name, balance, investment):
        Person.__init__(self, name)
        FinancialDetails.__init__(self, balance)
        self.investment = investment


class Partner(Person, ContactDetails, FinancialDetails):
    def __init__(self, name, phone, balance, partnership_share):
        Person.__init__(self, name)
        ContactDetails.__init__(self, phone)
        FinancialDetails.__init__(self, balance)
        self.partnership_share = partnership_share


class Manager(Employee, Partner):
    pass


class MajorInvestor(Investor, Partner):
    pass
```


Множественное наследование в таком стиле, что мы рассматривали с вами,                                                                                    
применяется не так часто, как можно было бы подумать.                                                                        

Дело в том, что в реальной практике классы в себе могут содержать                                                                          
Достаточно сложную логику, разного рода атрибуты и методы, сложные методы.                                                                                  

Такой код становится труднее читать, когда у нас может быть потенциально `n`                                                                                       
зависимостей, он подвежен большему количеству багов и т.д.                                                                               


# **Mixins**                                                       

В большей процентной вероятности множественное наследование мы можем с вами                                                                                 
использовать в виде **"примесей"**(mixins).                                                                                      

`Миксины` — это способ добавления функциональности к классам, не используя                                                                                    
при этом традиционное наследование. **Миксины** представляют собой наборы                                                                                   
методов, которые класс может использовать, но они не предназначены для                                                                                    
самостоятельного использования. Миксины предоставляют "смешиваемые"                                                                                    
функциональные возможности, которые можно комбинировать с основными                                                                                  
классами, чтобы добавлять дополнительное поведение или свойства без                                                                                   
изменения иерархии наследования.                                                                                         


# **Mixins Advantages**                                                                                 

* `Повторное использование кода:`                                                                                        
Миксины позволяют реализовывать поведение один раз и добавлять его                                                                                 
в несколько классов.                                                                                     

* `Чистота и модульность:`                                                                                            
Поскольку миксины предоставляют специализированное поведение,                                                                                   
ваш код становится более модульным и легко читаемым.                                                                                              

* `Избегание проблем с множественным наследованием:`                                                                                         
Когда вы используете миксины правильно, вы можете избежать проблем,                                                                                           
связанных с множественным наследованием, таких как `Diamond Problem`.                                                                                            


```python
class LoggerMixin:
    def log_action(self, action):
        print(f"{self.__class__.__name__}: {action}")


class Employee(LoggerMixin):
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def promote(self):
        self.log_action(f"{self.name} was promoted to a higher position!")


class Customer(LoggerMixin):
    def __init__(self, name):
        self.name = name

    def make_purchase(self, item):
        self.log_action(f"{self.name} purchased {item}.")


e = Employee("John Doe", "Developer")
e.promote()

c = Customer("Jane Smith")
c.make_purchase("laptop")
```

# **Important points while using mixins**                                                                                    


* `Миксины не должны иметь своих атрибутов:`                                                                                     
Хотя технически миксины могут иметь свои атрибуты, это может                                                                               
внести путаницу и неоднозначность в классы, которые их используют.                                                                                       

* `Миксины не должны наследоваться от других классов:`                                                                                    
Это может привести к неожиданному и непредсказуемому поведению.                                                        

* `Используйте ясные имена для миксинов:`                                                                                    
Название должно отражать предоставляемую функциональность                                                                                  
(например, `LoggerMixin`, `DatabaseMixin`).                                                                                      

---

Создать базовый класс `Transport`, который представляет собой                                                                                     
транспортное средство, и добавить к нему несколько миксин, чтобы                                                                                      
"обогатить" его функциональность.                                                                                   

* `EngineMixin` - добавляет методы для работы с двигателем.                                                                                        
* `SafetyMixin` - добавляет функциональность по безопасности                                                                                 
(например, ремни безопасности).                                                                                        
* `EntertainmentMixin` - добавляет функциональность мультимедийной системы.                                                                                    
* `ClimateMixin` - добавляет функциональность управления климат-контролем.                                                                                     


---

**Задача: Система управления контентом (CMS)**                                                                               

Создать простую систему управления контентом (CMS), которая                                                                              
позволяет пользователям публиковать статьи и комментировать их.                                                                                

1) **Миксины:**                                                       

* `AuthorMixin`: Добавляет функциональность, связанную с автором контента.                                                                                     
    * **Методы:**                                                                                 
    * `set_author(name)`: Устанавливает автора контента.                                                                                
    * `get_author()`: Возвращает имя автора.                                                                                     

* `TimestampMixin`: Добавляет функциональность временных меток.                                                                               
    * **Методы:**                                                                                  
    * `set_timestamp()`: Устанавливает текущее время как временную метку.                                                                                   
    * `get_timestamp()`: Возвращает временную метку.                                                                                    

* `ContentMixin`: Добавляет функциональность для хранения и извлечения                                                                                   
    содержимого.                                                        
    * **Методы:**                                                                                   
    * `set_content(content)`: Устанавливает содержимое.                                                                                           
    * `get_content()`: Возвращает содержимое.                                                                                       

2) **Классы:**                                                                                      

* `Article`: Представляет статью в CMS. **Должен использовать все три миксина**.                                                       
* `Comment`: Представляет комментарий к статье в CMS. Должен                                                                                
использовать `AuthorMixin` и `TimestampMixin`.                                                                                      

3) **Требования:**                                                                                 

1) Создайте статью, установите для нее автора, содержимое и временную метку.                                                                                     
2) Создайте комментарий к этой статье, установите для него автора и временную метку.                                                                                    
3) Выведите всю информацию о статье и комментарии, используя методы из миксинов.                                                                                     
