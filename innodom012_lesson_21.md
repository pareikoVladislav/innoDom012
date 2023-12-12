<!-- TOC -->
* [**Virtualenv**](#virtualenv)
* [**How Virtualenv works**](#how-virtualenv-works)
* [**Installing Virtualenv**](#installing-virtualenv)
* [**Creating a new virtual environment**:](#creating-a-new-virtual-environment-)
* [**Activation and deactivation of the medium**:](#activation-and-deactivation-of-the-medium-)
* [**Best Practices**](#best-practices-)
* [**Work with databases in Python**](#work-with-databases-in-python)
* [**Installing required lib**](#installing-required-lib)
      * [**Connecting to PostgreSQL via Python**](#connecting-to-postgresql-via-python)
      * [**Important Moments**](#important-moments)
* [**SQLAlchemy**](#sqlalchemy)
* [**ACID database properties and transactions**](#acid-database-properties-and-transactions)
* [**Updating existing records**](#updating-existing-records-)
* [**query's object methods**](#querys-object-methods-)
* [**Pydantic**](#pydantic)
* [**Home task**](#home-task)
<!-- TOC -->

# **Virtualenv**

`Virtualenv` — это инструмент для создания изолированных сред **Python**. Представьте,                                                                       
что у нас есть свой собственный, отдельный кабинет для каждого проекта, где мы можем                                                               
хранить все необходимые инструменты и материалы, и они не будут мешать другим проектам.                                                                  

В мире программирования, **Virtualenv** именно так и работает — он позволяет разработчикам                                                                
создавать отдельные, изолированные среды для разных проектов на **Python**.                                                                             


Исторически, в **Python** всегда была проблема управления зависимостями и версиями библиотек.                                                                              
Раньше разработчики сталкивались с конфликтами между разными проектами, которые требовали                                                                              
разных версий одних и тех же библиотек. **Virtualenv** появился как решение этой проблемы,                                                                              
позволяя создавать отдельные среды с разными версиями библиотек для каждого проекта.                                                                             


**Виртуальная среда** — это как бы "песочница", в которой можно работать с определенными версиями                                                                        
библиотек и **Python**, не затрагивая другие проекты и систему в целом. Это помогает избежать                                                                        
ситуации, когда изменения, необходимые для одного проекта, мешают работе других проектов.                                                                       

В стандартной установке **Python** все библиотеки устанавливаются глобально, и все проекты                                                                        
используют одни и те же версии библиотек. Это может привести к конфликтам, если разные                                                                        
проекты требуют разных версий одной библиотеки. **Virtualenv** решает эту проблему, создавая                                                                        
изолированные среды, где каждый проект может иметь свои собственные версии библиотек.                                                                       

---
# **How Virtualenv works**

Когда мы создаем новую виртуальную среду с помощью **Virtualenv**, он создает папку, которая                                                                      
содержит все необходимое для работы **Python**: интерпретатор, библиотеки, скрипты. Эта                                                                      
среда полностью независима от других сред и нашей основной системы.                                                                     


В каждой виртуальной среде мы можем устанавливать и управлять библиотеками независимо от                                                                     
других сред. Это означает, что мы можем иметь разные версии одной библиотеки в разных                                                                      
проектах, не беспокоясь о конфликтах.                                                                     


Используя **Virtualenv**, мы защищаем свою системную установку **Python** от изменений.                                                                      
Все изменения, которые будут делаться - будут делаться в виртуальной среде, не затрагивая                                                                      
глобальную установку **Python** и системные библиотеки. Это делает работу более                                                                      
безопасной и предсказуемой.                                                                     
---

# **Installing Virtualenv**

**Убедитесь, что Python установлен**: 
**Virtualenv** работает с **Python**, поэтому первым шагом                                                                      
является установка **Python**, если он еще не установлен. Можно проверить это, введя в                                                                      
командной строке `python --version` или `python3 --version`.                                                                     


Установка **Virtualenv** через `pip`: 
Используйте менеджер пакетов **Python**, **pip**, для установки                                                                      
**Virtualenv**. Введите в командной строке `pip install virtualenv` или `pip3 install virtualenv`                                                                      
(в зависимости от того, как называется **pip** для **Python 3**).                                                                     

**Проверка установки**:
После установки проверьте, что **Virtualenv** установлен правильно,                                                                      
введя `virtualenv --version`.                                                                     


**Virtualenv** совместим с большинством операционных систем, включая **Windows**, **macOS** и **Linux**.                                                                     
Главное требование — наличие установленного **Python**.                                                 


# **Creating a new virtual environment**:                                                                                                              

**Создание среды:**                                                                 
Открыть командную строку и перейти в директорию, где нужно создать                                                                      
виртуальную среду. Затем ввести `virtualenv название_среды`, например, `virtualenv myenv`.                                                                      

Это создаст новую папку с именем **myenv**, которая содержит **Python** интерпретатор и                                                                      
скрипты для активации среды.                                                                     

Структура среды:                                                               
В папке `myenv` будут лежать подпапки **bin** (или **Scripts** на **Windows**),                                                                      
**include** и **lib**, где хранятся скрипты, заголовочные файлы и библиотеки соответственно.                                                                     

# **Activation and deactivation of the medium**:                                                                    
**Активация среды**: Чтобы активировать виртуальную среду, нужно ввести `source myenv/bin/activate`                                                                      
(на **macOS**/**Linux**) или `myenv\Scripts\activate` (на **Windows**). В командной                                                                      
строке появится имя виртуальной среды.                                                                     

**Деактивация среды**: Чтобы выйти из виртуальной среды, просто введите `deactivate`.                                                                      
Это вернет вас в глобальную среду.                                                                     

**Управление зависимостями**: Установка и удаление пакетов внутри виртуальной среды                                                                                  

**Установка пакетов**: В активированной виртуальной среде мы можем устанавливать пакеты,                                                                     
используя `pip`, как обычно. Например, `pip install requests` установит пакет `requests`                                                                      
только внутри текущей виртуальной среды.                                                                     

**Удаление пакетов**:                                                        
Аналогично, мы можем удалять пакеты, используя `pip uninstall имя_пакета`.                                                                     

# **Best Practices**                                                                   

Советы по эффективному использованию **Virtualenv**                                                                     

**Отдельная среда для каждого проекта**: Создавайте новую виртуальную среду для каждого проекта,                                                                     
чтобы избежать конфликтов между зависимостями.
Использование `requirements.txt`: Для удобства управления зависимостями используйте файл                                                                     
`requirements.txt`, где перечислены все необходимые пакеты. Так вы сможете установить                                                                     
все зависимости одной командой — `pip install -r requirements.txt`.                                                                     

**Игнорирование папки среды в системе контроля версий**: Обычно папку виртуальной среды не                                                                      
включают в систему контроля версий (например, Git). Добавьте папку среды в `.gitignore`,                                                                      
чтобы исключить ее из репозитория.                                                                     


---

# **Work with databases in Python**

До этого момента мы с вами разбирали то, как мы можем взаимодействовать                                                 
с базами данных напрямую, используя специальный язык структурированных                                                  
запросов (`SQL`).                                                 

Начнем с того, что до появления современных инструментов и библиотек,                                                  
основным способом работы с базами данных был прямой доступ к ним с                                                  
использованием языка структурированных запросов – `SQL`. `SQL` позволял **напрямую**                                                  
взаимодействовать с данными, задавать сложные запросы, управлять базами данных                                                 
и манипулировать информацией в них.                                                 

Однако, для эффективного использования `SQL` требовалось не только знание его                                                  
синтаксиса, но и **глубокое понимание структуры конкретной базы данных**. Это                                                  
могло стать серьезным вызовом, особенно при работе со **сложными запросами**                                                  
и **большими объемами данных**.                                                 

Не стоит забывать и про безопастность, при работе с базами данных                                                      
Неправильно составленные `SQL-запросы` могли открыть дверь для                                                  
различных видов **атак**, в частности, для `SQL-инъекций`. Это требовало от                                                  
разработчиков особого внимания к безопасности запросов и данных.                                                 

Именно эти трудности и потребность в упрощении процесса работы с базами                                                 
данных привели к разработке специализированных библиотек и фреймворков в                                                 
языках программирования. Примерами таких инструментов являются `ORM-фреймворки`                                                  
(`Object-Relational Mapping`), такие как `Hibernate` для `Java`, `SQLAlchemy` для                                                 
`Python` и `ActiveRecord` для `Ruby on Rails`. Эти фреймворки позволяют программистам                                                  
работать с базами данных, используя **конструкции своего языка** программирования,                                                 
что существенно упрощает процесс. Например, вместо написания **сложных**                                                 
**SQL-запросов**, разработчики могут использовать более интуитивные и понятные                                                 
**методы и функции, предоставляемые их языками программирования**.                                                 

Кроме того, использование таких библиотек и фреймворков значительно повышает                                                  
безопасность работы с базами данных. Они обычно **включают** механизмы **защиты от**                                                 
**SQL-инъекций**, автоматически обрабатывая и экранируя входные данные.                                                 

Еще одним важным преимуществом является переносимость и сопровождение кода.                                                 
Благодаря унифицированному интерфейсу, предоставляемому многими библиотеками,                                                  
код, написанный для одной системы управления базами данных, может быть легче                                                  
адаптирован для работы с другой. Это значительно упрощает поддержку и                                                  
развитие программных продуктов.                                                 

В заключение, переход от прямого использования SQL к использованию                                                  
специализированных библиотек в языках программирования ознаменовал собой                                                  
значительный шаг вперед в области разработки программного обеспечения.                                                  
Это сделало процесс разработки более безопасным, гибким и удобным для                                                 
программистов, а также открыло новые возможности для оптимизации и улучшения                                                 
работы с базами данных.                                                 

---

# **Installing required lib**

Прежде всего, нам нужно установить библиотеку `psycopg2`. Это можно сделать                                                  
с помощью менеджера пакетов pip. В командной строке или терминале                                                  
достаточно выполнить команду:                                                 
```commandline
pip install psycopg2
```
Иногда может потребоваться использовать `psycopg2-binary` для установки уже                                                  
скомпилированной версии библиотеки.                                                 

Убедитесь, что у вас есть доступ к серверу PostgreSQL и что у вас есть                                                  
необходимые учетные данные (имя пользователя, пароль, адрес сервера,                                                  
порт, название базы данных).                                                 

#### **Connecting to PostgreSQL via Python**

Сначала нужно импортировать `psycopg2` в ваш **Python** код:                                                   
```python
import psycopg2
```


Для подключения к базе данных используем функцию `connect()` из библиотеки                                                  
`psycopg2`. В эту функцию передаются параметры подключения, такие как имя                                                  
пользователя, пароль, хост, порт и название базы данных.                                                  

```python
conn = psycopg2.connect(
    dbname="your_dbname", 
    user="your_username", 
    password="your_password", 
    host="your_host",
    port="your_port"
)
```

Для выполнения `SQL-запросов` необходимо создать **курсор** с помощью метода                                                   
`cursor()` объекта подключения.                                                  

```python
cursor = conn.cursor()
```

Теперь можно использовать курсор для выполнения `SQL-запросов`. Например,                                                   
для создания таблицы в базе данных:                                                  

```python
cursor.execute("""CREATE TABLE IF NOT EXISTS "user" (
                    id INT PRIMARY KEY,
                    name VARCHAR(25) NOT NULL,
                    surname VARCHAR(30),
                    age FLOAT NOT NULL,
                    email VARCHAR(100) UNIQUE NOT NULL,
                    country VARCHAR(25) NOT NULL,
                    city VARCHAR(35),
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT NULL
                )"""
)

cursor.execute("""CREATE TABLE IF NOT EXISTS Phone_book (
                    id INT PRIMARY KEY,
                    user_id INT,
                    number VARCHAR(45),
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT NULL,
                    FOREIGN KEY (user_id) REFERENCES "user"(id)
                )"""
)
```

Так же мы можем и создавать данные через этот метод:                                          

```python
cursor.execute(
    """
    INSERT INTO "user" (id, name, surname, age, email, country, city)
    VALUES
    (1, 'Alex', 'Storm', 24, 'a.storm99@gmail.com', 'USA', 'Texas'),
    (2, 'Julia', 'Morrow', 29, 'jull.morrow94@gmail.com', 'Canada', 'Ottawa'),
    (3, 'Kseniya', 'Michurik', 21, 'ksu.michurik02@mail.ru', 'Russia', 'Moscow'),
    (4, 'Dmitry', 'Schypak', 32, 'dmitry.schypak89@mail.ru', 'Belarus', 'Minsk')
    """
)

cursor.execute(
    """
    INSERT INTO Phone_book (id, user_id, number)
    VALUES
    (1, 2, '+1 (252) 789-21-11'),
    (2, 3, '+17 646-123-78'),
    (3, 1, '+7 931 656-78-89'),
    (4, 4, '+375 29 878-45-22')
    """
)

conn.commit() # обязательно при любых действиях, связанных с изменением состояния базы данных
```

Теперь можно использовать курсор для получения данных из таблицы:                                         

```python
cursor.execute("SELECT * FROM Phone_book")
rows = cursor.fetchall()
for row in rows:
    print(row)
```

После выполнения всех необходимых операций, важно закрыть курсор                                                       
и соединение с базой данных.                                                      

```python
cursor.close()
conn.close()
```

#### **Important Moments**

**Обработка Исключений**: Важно обрабатывать возможные исключения                                                       
при работе с базой данных, такие как **ошибки подключения** или                                                       
**выполнения запросов**.                                                      


**Управление Транзакциями**: `psycopg2` управляет транзакциями **автоматически**,                                                       
но иногда может потребоваться **явное управление транзакциями**, особенно                                                       
при работе с **изменениями данных**.                                              


---

# **SQLAlchemy**

Всё это здорово конечно, но в современной разработке                                                
мы не работаем с `sql` запросами напрямую (если дело касается работы                                                 
с приложениями и прочим. Есть сферы, где наоборот вы как раз                                           
работаете с `SQL` напрямую)                                                  

Один из самых популярных способов работы с Базами данных в языках                                         
программирования - работа с `ORM`.                                          

`ORM` - `Object Relational Model` (**Объектно-реляционное отображение**)                                      
`ORM` - такая технология, которая позволяет нам, как разработчикам,                                      
работать с базой данных посредством **написания обычных объектов** в                                        
языке программирования и вызова необходимых методов.                                        
Это избавляет наз от необходимости писать чистые `SQL` запросы,                                               
вместо этого мы будем с вами обращаться к разным объектам и их                                           
методам.                                    

**SQLAlchemy** - мощный **ORM** инструмент, который позволяет
разработчикам работать с различными СУБД, такими как `SQLite`, `PostgreSQL`,
`MySQL`, `Oracle` и другими, используя **единый интерфейс**.                                                   
Он предоставляет уровень абстракции, позволяя вам работать с                                                    
базой данных через **объекты и SQL-выражения**.

**Применение:**

* Большие проекты, требующие поддержки различных **СУБД** без изменения кода.                                                    
* Отображение данных из базы данных на объекты **Python** и обратно.                                                
* Управление сложными **SQL-запросами**.                                            

**Пример создания подключения:**

Создадим подключение к базе данных через подход использования контекст менеджера.                                               
Это даст нам более грамотное, чёткое управления ресурсами базы данных, так же мы будем                                     
всегда уверены на 100%, что по завершению работы наше подключение не останется                                         
"висеть", оно всегда будет закрываться благодаря методу `__exit__()`                                                 

Так же создадим один метод, который будет отвечать за инициализацию всех наших моделей                                     
в базе данных.                                                                        

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConnector:
    def __init__(self, db_url):
        self.db_url = db_url
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)

    def __enter__(self):
        self.session = self.Session()
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()

    def create_tables(self, base):
        base.metadata.create_all(self.engine)
```

И уже отдельно создадим логику для самих таблиц. Отныне называть их будем **модели**                                            
При написании и инициализации **моделей** и будут создаваться наши с вами таблицы                                        
в базе данных.                                                                    


```python
from sqlalchemy import Column, Integer, String, Float, TIMESTAMP, ForeignKey, func
from sqlalchemy.orm import relationship, declarative_base

import environ
import os
from urllib.parse import quote

from lesson_21_code.db_conn import DBConnector


BASE_DIR = "/home/vladislav/Desktop/innoDom012"
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))
db_url = f"postgresql://{env('DB_USER_POS')}:{quote(env('DB_PASSWORD_POS'))}@{env('DB_HOST_POS')}:{env('DB_PORT_POS')}/{env('DB_NAME_POS')}"

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False)
    surname = Column(String(30))
    age = Column(Float, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    country = Column(String(25), nullable=False)
    city = Column(String(35))
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())
    updated_at = Column(TIMESTAMP)

    # Relationship to PhoneBook
    phone_numbers = relationship("PhoneBook", back_populates="user")


class PhoneBook(Base):
    __tablename__ = 'phonebook'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    number = Column(String(45))
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())
    updated_at = Column(TIMESTAMP)

    # Relationship to User
    user = relationship("User", back_populates="phone_numbers")


if __name__ == "__main__":
    db_connector = DBConnector(db_url=db_url)
    db_connector.create_tables(Base)
```

Здесь мы испортируем необходимые для работы методы и классы (да, всё будет писаться                                        
через методы и классы, больше нет сырых SQL запросов), так же, для подключения к                                         
базе данных нам потребуются наши с вами креды. Эта штука должна быть **ВСЕГДА** в                                        
безопасном, надёжном месте. Обычно это `.env` файл. Для работы с ним нам понадобятся                                        
отдельная библиотека и её методы.                                                        

Сперва мы устанавливаем инстанс класса `Env`, после чего читаем содержимое этого файла,                                      
для получения доступа к нужным переменным.                                               

Дальше мы создаём объект базовой модели от нашей `SQLalchemy` `ORM`, от которого будем                                          
наследоваться. Он понадобится нам при создании наших моделей.                                                        

Все модели будут создаваться посредством написания питоновских классов.                                             
Как видите, мы можем задать спец имя для модели, и именно по этому созданному                                           
имени мы будем обращаться к таблице в самой базе данных, если будет такая необходимость.                                     

Все поля вашей модели декларируются, как обычные статические методы класса, которым мы                                   
и задаём нужные нам параметры. Параметры для полей же задаются прямо в скобках у                                           
определённых вами же полей(классов из `ORM`).                                                   

---

# **ACID database properties and transactions**


`ACID` – это аббревиатура, описывающая четыре ключевых принципа для                                                          
обеспечения надежности транзакций в базах данных. Эти принципы                                                          
критически важны для поддержания целостности данных и обеспечения                                                          
надежной работы базы данных.                                                         

**ACID Principles**                                                         

* **Атомарность** (`Atomicity`): Этот принцип гарантирует, что транзакция либо                                                          
**полностью выполняется**, либо **не выполняется вовсе**. Если какая-либо часть                                                          
транзакции не может быть завершена, вся транзакция **откатывается** (**отменяется**),                                                          
и база данных **возвращается в состояние**, которое было **до начала транзакции**.                                                         

* **Согласованность** (`Consistency`): Согласованность означает, что транзакция                                                         
переводит базу данных из **одного согласованного состояния в другое**. После                                                         
транзакции все правила целостности данных сохраняются.                                                         
Обеспечивает, что все данные будут соответствовать всем правилам и ограничениям                                             
базы данных.

* **Изолированность** (`Isolation`): Принцип изолированности гарантирует, что                                                         
транзакции, **выполняемые одновременно**, **не влияют друг на друга**. Каждая                                                          
транзакция должна быть **изолирована от других**, чтобы предотвратить                                                          
**смешивание данных** между транзакциями.                                                         

* **Долговечность** (`Durability`): Этот принцип обеспечивает **сохранение**                                                          
**результатов успешно выполненной транзакции**. После завершения транзакции                                                          
её результаты **остаются в базе данных даже в случае сбоев системы**.                                                         


Для **PostgreSQL** и **SQLAlchemy**, эти принципы обычно управляются на уровне базы данных,                                                          
но вот как можно учитывать ACID свойства на уровне кода:                                                         

**Без учета Атомарности:**                                                   

```python
import os
from urllib.parse import quote
import environ

from sqlalchemy.exc import DisconnectionError

from lesson_21_code.db_conn import DBConnector
from lesson_21_code.models import User, PhoneBook

BASE_DIR = "/home/vladislav/Desktop/innoDom012"
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))
db_url = f"postgresql://{env('DB_USER_POS')}:{quote(env('DB_PASSWORD_POS'))}@{env('DB_HOST_POS')}:{env('DB_PORT_POS')}/{env('DB_NAME_POS')}"


front_user_form_data = {
    "name": "Alex",
    "surname": "John",
    "age": 24,
    "email": "alex.john@icloud.com",
    "country": "USA",
    "city": "Minnesota",
}

front_phone_form_data = {
    "user_id": 1,
    "number": "+1 787 55 41",
}


def create_new_user(manager, form_data: dict):
    user = User(**form_data)

    manager.add(user)

    manager.commit()


def write_user_number(manager, form_data: dict):
    phone_number_data = PhoneBook(**form_data)

    manager.add(phone_number_data)

    manager.commit()


with DBConnector(db_url=db_url) as session:
    create_new_user(manager=session, form_data=front_user_form_data)  # добавление нового пользователя
    raise DisconnectionError("Something went wrong")
    write_user_number(manager=session, form_data=front_phone_form_data)  # добавление номера телефона для этого пользователя
```

**С учётом атомарности:**                                         
```python
import os
from urllib.parse import quote
import environ

from sqlalchemy.exc import DisconnectionError

from lesson_21_code.db_conn import DBConnector
from lesson_21_code.models import User, PhoneBook

BASE_DIR = "/home/vladislav/Desktop/innoDom012"
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))
db_url = f"postgresql://{env('DB_USER_POS')}:{quote(env('DB_PASSWORD_POS'))}@{env('DB_HOST_POS')}:{env('DB_PORT_POS')}/{env('DB_NAME_POS')}"


# front_user_form_data = {
#     "name": "Alex",
#     "surname": "John",
#     "age": 24,
#     "email": "alex.john@icloud.com",
#     "country": "USA",
#     "city": "Minnesota",
# }
#
# front_phone_form_data = {
#     "user_id": 1,
#     "number": "+1 787 55 41",
# }

front_user_form_data = {
    "name": "Andrew",
    "age": 30,
    "email": "andrew93@gmail.com",
    "country": "Belarus",
    "city": "Minsk",
}

front_phone_form_data = {
    "user_id": 2,
    "number": "+375 44 737 02 01",
}


def create_new_user(manager, form_data: dict):
    user = User(**form_data)

    manager.add(user)
    raise DisconnectionError("Something went wrong")

    manager.commit()


def write_user_number(manager, form_data: dict):
    phone_number_data = PhoneBook(**form_data)

    manager.add(phone_number_data)

    manager.commit()


with DBConnector(db_url=db_url) as session:
    try:
        create_new_user(manager=session, form_data=front_user_form_data)  # добавление нового пользователя
        write_user_number(manager=session,form_data=front_phone_form_data)  # добавление номера телефона для этого пользователя
    except DisconnectionError:
        session.rollback()
```

если обе операции выполнены успешно, транзакция подтверждается с                                                     
помощью `commit()`, что обеспечивает атомарность и согласованность.                                                     


**Без учета Согласованности**                                                  
```python
with DBConnector(db_url=db_url) as session:
    new_user = User(
        name="Test User",
        age=-5,
        email="test.email@test.com",
        country="Test country"
    )

    session.add(new_user)
    session.commit()
```

**С учетом Согласованности:**                                                        
```python
with DBConnector(db_url=db_url) as session:
    new_user = User(
        name="Test User",
        age=-5,
        email="test.email@test.com",
        country="Test country"
    )

    if new_user.age > 0:
        session.add(new_user)
        session.commit()
```


Соблюдение принципов `ACID` в базах данных играет ключевую роль в                                                      
обеспечении надежности и целостности данных, что особенно важно                                                      
в системах, где важна точность и сохранность информации.                                                     

---

# **Updating existing records**                                               

Объект `Query` в `SQLAlchemy` является основным инструментом для создания и                                                      
выполнения запросов к базе данных в стиле `ORM` (**Object-Relational Mapping**).                                                      

Этот объект используется для формирования запросов `SQL` с использованием                                                      
**Python-объектов** и их атрибутов, а не сырых **SQL-запросов**.                                                     


Объект `Query` создается через вызов метода `query()` на объекте сессии `SQLAlchemy`                                                     
Где `Model` - это класс, отображаемый на таблицу в базе данных.                                                     

# **query's object methods**                                                     

**Фильтрация (`Filtering`)**:                                                     

`filter()`: Принимает условия для фильтрации результатов, например,                                                      
`session.query(User).filter(User.name == 'Alice')`.                                                     
`filter_by()`: Предоставляет более простой способ фильтрации, используя                                                      
ключевые слова, например, `session.query(User).filter_by(name='Alice')`.                                                     

**Сортировка (Ordering)**:                                                     

`order_by()`: Упорядочивает результаты запроса, например,                                                      
`session.query(User).order_by(User.name)`.                                                     

**Ограничение результатов и срезы (Limiting and Slicing)**:                                                     

`limit()`: Ограничивает количество возвращаемых результатов,                                                      
например, `query.limit(10)`.                                                     
`Срезы Python`: Можно использовать синтаксис срезов, например, `query[1:3]`.                                                     

**Агрегация (Aggregation)**:                                                                                                          

Методы, такие как `count()`, `sum()`, `avg()`, используются для агрегации                                                      
данных, например, `session.query(User).filter(User.age > 18).count()`.                                                     


**Выполнение запроса:**                                                                                                          

`all()`: Возвращает список всех объектов, соответствующих запросу.                                                     
`first()`: Возвращает первый объект из результата или None.                                                     
`one()`: Возвращает ровно один объект или вызывает исключение.                                                     
`scalar()`: Возвращает одно значение (первый элемент первой строки результата).                                                     


**Присоединение (Joining)**                                                                                                          
`join()`: Используется для соединения таблиц, например,                                                      
`session.query(User).join(Address)`.                                                     


**Группировка (Grouping)**                                                                                                          
`group_by()`: Используется для группировки результатов по                                                      
определенным критериям.                                                     

**Дополнительные функции**                                                     
`having()`: Применяется **после** `group_by()` для фильтрации                                                      
группированных результатов.                                                     
`distinct()`: Возвращает уникальные результаты.                                                     


**Обновление существующих записей**                                                  

```python
with DBConnector(db_url=db_url) as session:
    user_to_update = session.query(User).filter(
        User.id == 1).first()  # предполагается, что пользователь с id=1 существует
    user_to_update.age = 25
    user_to_update.updated_at = datetime.datetime.now()
    session.commit()
```

**Забор данных из базы данных и преобразование их в JSON строки**                                                  

```python
with DBConnector(db_url=db_url) as session:
    # Запрос данных пользователя
    user = session.query(User).options(
        joinedload(User.phone_numbers)
    ).filter(User.id == 1).first()

    user_data = {
        "id": user.id,
        "name": user.name,
        "surname": user.surname,
        "age": user.age,
        "email": user.email,
        "country": user.country,
        "phone_numbers": [{"number": pn.number} for pn in user.phone_numbers]
    }

    user_json = json.dumps(user_data)  # Преобразование в JSON строку


print(user_json)
```

**Фильтрация данных**                                                             
```python
with DBConnector(db_url=db_url) as session:
    # Фильтрация пользователей по стране и возрасту
    filtered_users = session.query(User).filter(User.country == "USA", User.age > 25).all()
    if filtered_users:
        for user in filtered_users:
            print(user.name, user.age)
    else:
        print("Nothing match")
```

---

# **Pydantic**

`Pydantic` - это библиотека для **валидации данных** и **управления настройками** в **Python**,                                                              
использующая аннотации типов **Python**. Она позволяет создавать классы моделей данных,                                                              
которые **автоматически проверяют типы и форматы данных при создании**                                                              
экземпляров этих классов.                                                             


`Pydantic` проверяет, что входные данные **соответствуют ожидаемым типам и ограничениям**.                                                             
**Автоматически преобразует** входные данные в нужные типы.                                                             
**Хорошо интегрируется** с инструментами для создания документации `API`, такими как `Swagger`.                                                             
**Генерирует понятные ошибки**, что упрощает отладку.                                                             

В `Pydantic` вы определяете модели данных с использованием **Python** классов, где поля                                                              
класса аннотированы типами данных. `Pydantic` затем использует эти аннотации                                                              
для валидации данных.                                                             

```python
from pydantic import BaseModel
from typing import Optional, List
import datetime

class UserSchema(BaseModel):
    id: int
    name: str
    surname: Optional[str]
    age: int
    email: str
    country: str
    city: Optional[str]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    

class PhoneBookSchema(BaseModel):
    id: int
    user_id: int
    number: str
    created_at: Optional[datetime]
    updated_at: Optional[datetime]


class UserWithPhoneNumbersSchema(BaseModel):
    phone_numbers: List[PhoneBookSchema]
```

**Использование Pydantic для валидации и сериализации**                                            

```python
# Валидация данных пользователя
user_data = {
    "name": "Ivan",
    "age": 30,
    "email": "ivan@example.com",
    "country": "Russia"
}
user = UserSchema(**user_data)

# Сериализация SQLAlchemy объекта в Pydantic
def sqlalchemy_to_pydantic(db_obj, pydantic_model):
    return pydantic_model(**db_obj.__dict__)

# Предположим, у нас есть объект SQLAlchemy user_obj
pydantic_user = sqlalchemy_to_pydantic(user_obj, UserSchema)
```

**Интеграция с запросами SQLAlchemy**                                                

```python
# Получение данных из базы данных и их сериализация
db_user = session.query(User).filter(User.id == 1).first()
if db_user:
    user_data = sqlalchemy_to_pydantic(db_user, UserWithPhoneNumbersSchema)
    print(user_data.json())  # Вывод в формате JSON
```

---

# **Home task**

Написать **НЕБОЛЬШУЮ** систему с переводами деняк)))))

Продумать необходимые для этого модели

Необходимые секретные данные должны **хэшироваться**

Можно будет **создавать** пользователя, **обновлять** нужную инфу, **просматривать** нужную инфу
Иметь возможность **закидывать** деньги на счёт, **снимать** их и **переводить**


Все операции должны быть реализованы через базы данных, никаких больше файлов.
Все операции должны быть с соблюдением `ACID` свойств.

Валидация полей через `pydantic`
работа с БД через `SQLalchemy`
