<!-- TOC -->
* [**SQLalchemy, Pydantic, Alembic**](#sqlalchemy-pydantic-alembic)
* [**Work with data**](#work-with-data-)
* [**query's object methods**](#querys-object-methods-)
* [**Pydantic**](#pydantic)
* [**Alembic**](#alembic-)
* [**Main Components of Alembic**](#main-components-of-alembic)
* [**Alembic Workflow**](#alembic-workflow)
* [**Home task**](#home-task)
<!-- TOC -->
# **SQLalchemy, Pydantic, Alembic**

Продолжаем разбираться с алхимией и прочим!                                                      

```python
import os
from urllib.parse import quote
from dotenv import load_dotenv

BASE_DIR = "/home/vladislav/Desktop/innoDom012"
env = load_dotenv(os.path.join(BASE_DIR, ".env"))
url_engine = f"postgresql://{os.getenv('DB_USER_POS')}:{quote(os.getenv('DB_PASSWORD_POS'))}\
@{os.getenv('DB_HOST_POS')}:{os.getenv('DB_PORT_POS')}/{os.getenv('DB_NAME_POS')}"
```


```python
from lesson_21_code.db_conn import DBConnector
from lesson_21_code.models import User, PhoneBook

from db_url import url_engine


front_user_form_data = [
    {"name": "Alex", "surname": "John", "age": 24, "email": "alex.john@icloud.com", "country": "USA", "city": "Oustin"},
    {"name": "Diana", "surname": "Julis", "age": 18, "email": "di.julis@icloud.com", "country": "USA",
     "city": "New York"},
    {"name": "Irina", "surname": None, "age": 26, "email": "irina97@gmail.com", "country": "USA", "city": "Oustin"},
    {"name": "Artsiom", "surname": "Rart", "age": 30, "email": "art.rart@gmail.com", "country": "USA",
     "city": "Minnesota"},
    {"name": "John", "surname": "Black", "age": 18, "email": "johnblack@icloud.com", "country": "USA",
     "city": "New York"},
    {"name": "Alex", "surname": "Grey", "age": 18, "email": "alex.g@gmail.com", "country": "USA", "city": "Ohio"},
    {"name": "Nika", "surname": None, "age": 16, "email": "nika08@icloud.com", "country": "USA", "city": "Oustin"},
    {"name": "Alexis", "surname": "Steall", "age": 22, "email": "a.steall@icloud.com", "country": "USA",
     "city": "Ohio"},
    {"name": "Vlad", "surname": "Novikov", "age": 23, "email": "novikov.vlad@gmail.com", "country": "Canada",
     "city": "Ontario"},
    {"name": "Diana", "surname": "Dubruch", "age": 25, "email": "dubrich.di@gmail.com", "country": "USA",
     "city": "Minnesota"},
    {"name": "Pavel", "surname": "Yakovlev", "age": 25, "email": "pavel.yakov@mail.ru", "country": "USA",
     "city": "New York"},
    {"name": "Sergey", "surname": "Vysocky", "age": 20, "email": "serg.vysocky@mail.ru", "country": "USA",
     "city": "Oustin"},
    {"name": "Sergey", "surname": None, "age": 32, "email": "sergey.anon@icloud.com", "country": "USA",
     "city": "Minnesota"},
    {"name": "Dima", "surname": None, "age": 24, "email": "dmitry99@gmail.com", "country": "USA", "city": "Minnesota"},
    {"name": "Valeriya", "surname": None, "age": 28, "email": "valeriya.a@icloud.com", "country": "Canada",
     "city": "Ontario"},
    {"name": "Kseniya", "surname": "Borod", "age": 28, "email": "borod.ksu@gmail.com", "country": "USA",
     "city": "Oustin"},
    {"name": "Ken", "surname": "Klark", "age": 24, "email": "klark.ken@icloud.com", "country": "USA",
     "city": "Minnesota"},
    {"name": "Isak", "surname": "Nuut", "age": 31, "email": "isek.nuut@icloud.com", "country": "USA",
     "city": "Minnesota"},
    {"name": "Julia", "surname": "Borsich", "age": 17, "email": "borsich.jul@icloud.com", "country": "Canada",
     "city": "Ontario"},
    {"name": "Nasty", "surname": "Golovach", "age": 18, "email": "nancy.golovach@icloud.com", "country": "USA",
     "city": "Ohio"},
    {"name": "Mariya", "surname": "Ambrazh", "age": 18, "email": "amb.masha@icloud.com", "country": "USA",
     "city": "Minnesota"},
    {"name": "Julia", "surname": None, "age": 18, "email": "julia05@gmail.com", "country": "USA", "city": "Oustin"},
    {"name": "Alex", "surname": None, "age": 24, "email": "alex.anon@mail.ru", "country": "USA", "city": "Minnesota"},
    {"name": "Vlad", "surname": "Kit", "age": 35, "email": "vlad.kit@gmail.com", "country": "USA", "city": "New York"},
    {"name": "Sergey", "surname": "Bereziovky", "age": 35, "email": "serg.berezovsky@mail.ru", "country": "Canada",
     "city": "Ontario"},
    {"name": "Agness", "surname": None, "age": 37, "email": "youragness@mail.ru", "country": "USA",
     "city": "Minnesota"},
    {"name": "Mila", "surname": None, "age": 18, "email": "mila05@mail.ru", "country": "USA", "city": "Oustin"},
    {"name": "Masha", "surname": "Shick", "age": 27, "email": "shick.masha@gmail.com", "country": "USA",
     "city": "New York"},
    {"name": "Dima", "surname": "Golubev", "age": 27, "email": "golubevdima@icloud.com", "country": "USA",
     "city": "Ohio"},
    {"name": "Vlad", "surname": "Grich", "age": 27, "email": "grichvlad@icloud.com", "country": "USA",
     "city": "Minnesota"},
]

front_phone_form_data = [
    {"user_id": 2, "number": "+1 787 55 41"},
    {"user_id": 2, "number": "+1 848 54 41"},
    {"user_id": 3, "number": "+1 112 12 84"},
    {"user_id": 4, "number": "+1 88 225 21"},
    {"user_id": 5, "number": "+1 77 121 223"},
    {"user_id": 6, "number": "+1 454 11 23"},
    {"user_id": 5, "number": "+1 888 55 55"},
    {"user_id": 7, "number": "+1 11 125 77"},
    {"user_id": 8, "number": "+1 555 98 99"},
    {"user_id": 9, "number": "+1 121 87 21"},
    {"user_id": 10, "number": "+1 887 332 11"},
    {"user_id": 11, "number": "+1 122 89 88"},
    {"user_id": 12, "number": "+1 777 112 25"},
    {"user_id": 13, "number": "+1 891 56 52"},
    {"user_id": 13, "number": "+1 358 74 12"},
    {"user_id": 14, "number": "+1 874 69 32"},
    {"user_id": 15, "number": "+1 528 27 74"},
    {"user_id": 16, "number": "+1 735 91 98"},
    {"user_id": 17, "number": "+1 537 95 16"},
    {"user_id": 18, "number": "+1 987 12 13"},
    {"user_id": 19, "number": "+1 144 55 88"},
    {"user_id": 20, "number": "+1 17 774 55"},
    {"user_id": 21, "number": "+1 159 54 365"},
    {"user_id": 22, "number": "+1 444 98 88"},
    {"user_id": 23, "number": "+1 12 774 655"},
    {"user_id": 24, "number": "+1 454 441 323"},
    {"user_id": 25, "number": "+1 445 55 31"},
    {"user_id": 26, "number": "+1 999 11 11"},
    {"user_id": 27, "number": "+1 40 151 131"},
    {"user_id": 28, "number": "+1 99 484 666"},
    {"user_id": 29, "number": "+1 666 66 66"},
    {"user_id": 30, "number": "+1 551 551 5"},
    {"user_id": 22, "number": "+1 121 198 73"},
    {"user_id": 17, "number": "+1 645 56 35"},
    {"user_id": 9, "number": "+1 25 73 745"},
]


def create_users(manager, form_data: list):
    try:
        for row in form_data:
            user = User(**row)
            manager.add(user)

        manager.commit()
    except:
        manager.rollback()


def write_users_numbers(manager, form_data: list):
    try:
        for row in form_data:
            phone_number_data = PhoneBook(**row)
            manager.add(phone_number_data)

        manager.commit()
    except:
        manager.rollback()


with DBConnector(db_url=url_engine) as session:
    create_users(manager=session, form_data=front_user_form_data)
    write_users_numbers(manager=session, form_data=front_phone_form_data)
```


# **Work with data**                                               

Определённая часть запросов будет происходить через объект `Query`                                               

Объект `Query` в `SQLAlchemy` является основным инструментом для создания и                                                      
выполнения запросов к базе данных в стиле `ORM` (**Object-Relational Mapping**).                                                      

Этот объект используется для формирования запросов `SQL` с использованием                                                      
**Python-объектов** и их атрибутов, а не сырых **SQL-запросов**.                                                     

```python
with DBConnector(db_url=url_engine) as session:
    users = session.query(User).all()
    for user in users:
        print(f"The user's '{user.name}' email is - {user.email}")
```

Объект `Query` создается через вызов метода `query()` на объекте сессии `SQLAlchemy`                                                     
Где `Model` - это класс, отображаемый на таблицу в базе данных.                                                     

# **query's object methods**                                                     

**Фильтрация (`Filtering`)**:                                                     

`filter()`: Принимает условия для фильтрации результатов, например,                                                      
`session.query(User).filter(User.name == 'Alice')`.                                                     

```python
with DBConnector(db_url=url_engine) as session:
    users = session.query(User).filter(
        User.email.like("%mail.ru")
    )
    for user in users:
        print(f"The user's '{user.name}' email is - {user.email}")
```
`filter_by()`: Предоставляет более простой способ фильтрации, используя                                                      
ключевые слова, например, `session.query(User).filter_by(name='Alice')`.                                                     


```python
with DBConnector(db_url=url_engine) as session:
    users = session.query(User).where(
        or_(User.name.like("J%"), User.name.like("M%"))
    )
    for user in users:
        print(f"The user's '{user.name}' email is - {user.email}")
```

**Сортировка (Ordering)**:                                                     

`order_by()`: Упорядочивает результаты запроса, например,                                                      
`session.query(User).order_by(User.name)`.                                                     
```python
with DBConnector(db_url=url_engine) as session:
    users = session.query(User).where(
        or_(User.name.like("J%"), User.name.like("M%"))
    ).order_by(User.age)
    for user in users:
        print(f"The user's ID - {user.id}. '{user.name}', {user.age}, email is - {user.email}")
```
**Ограничение результатов и срезы (Limiting and Slicing)**:                                                     

`limit()`: Ограничивает количество возвращаемых результатов,                                                      
например, `query.limit(10)`.                                                     
`Срезы Python`: Можно использовать синтаксис срезов, например, `query[1:3]`.                                                     

**Агрегация (Aggregation)**:                                                                                                          

Методы, такие как `count()`, `sum()`, `avg()`, используются для агрегации                                                      
данных, например, `session.query(User).filter(User.age > 18).count()`.                                                     
```python
with DBConnector(db_url=url_engine) as session:
    users = session.query(User).filter(
        User.age >= 18
    ).count()

    print(f"Кол-во совершеннолетних = {users}")
```

**Выполнение запроса:**                                                                                                          

`all()`: Возвращает список всех объектов, соответствующих запросу.                                                     
`first()`: Возвращает первый объект из результата или None.                                                     
`one()`: Возвращает ровно один объект или вызывает исключение.                                                     
`scalar()`: Возвращает одно значение (первый элемент первой строки результата).                                                     

```python
with DBConnector(db_url=url_engine) as session:
    user = session.query(User).filter(
        User.age >= 18
    ).first()
    print(f"The user's ID - {user.id}. '{user.name}', {user.age}, email is - {user.email}")
```

```python
with DBConnector(db_url=url_engine) as session:
    user = session.query(User).filter(
        User.id == 2
    ).one()
    print(f"The user's ID - {user.id}. '{user.name}', {user.age}, email is - {user.email}")
```

**Присоединение (Joining)**                                                                                                          
`join()`: Используется для соединения таблиц, например,                                                      
`session.query(User).join(Address)`.                                                     


```python
with DBConnector(db_url=url_engine) as session:
    user = session.query(User).options(
        joinedload(User.phone_numbers)
    ).filter(User.id == 15).one()

    user_data = {
        "id": user.id,
        "name": user.name,
        "surname": user.surname,
        "age": user.age,
        "email": user.email,
        "country": user.country,
        "phone_numbers": [pn.number for pn in user.phone_numbers]
    }

    user_json = json.dumps(user_data)  # Преобразование в JSON строку

print(user_json)
```


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

```python
# def get_user_data_by_email(manager, email):
#     user_data = manager.query(User).filter(
#         User.email == email
#     ).one()
#
#     user_id = user_data.id
#
#     return user_id


def update_user_data(manager, request):
    try:
        user = manager.query(User).filter(
            User.id == request.get("user_id")
        ).one()

        phone = manager.query(PhoneBook).filter(
            PhoneBook.user_id == user.id,
            PhoneBook.number == request.get("body").get("old_number")
        ).one()

        if user:
            user.surname = request.get("body").get("surname")
            user.age = request.get("body").get("age")
            user.updated_at = datetime.now()
            manager.commit()
        if phone:
            phone.number = request.get("body").get("new_number")
            phone.updated_at = datetime.now()
            manager.commit()
    except Exception as err:
        print(str(err))
        manager.rollback()


request_data = {
    "user_id": 21,
    "body": {
        "email": "nancy.golovach@icloud.com",
        "surname": "NEW SURNAME",
        "age": 19,
        "old_number": "+1 159 54 365",
        "new_number": '+ 1 563 45 951'

    }
}


with DBConnector(db_url=url_engine) as session:
    update_user_data(
        manager=session,
        request=request_data
    )
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

class PhoneBookSchema(BaseModel):
    id: int
    user_id: int
    number: str
    created_at: Optional[int]
    updated_at: Optional[int]


class UserSchema(BaseModel):
    id: int
    name: str
    surname: Optional[str]
    age: int
    email: str
    country: str
    city: Optional[str]
    created_at: Optional[int]
    updated_at: Optional[int]
    phone_numbers: List[PhoneBookSchema]


class UserWithPhoneNumbersSchema(BaseModel):
    phone_numbers: List[PhoneBookSchema]
```

**Использование Pydantic для валидации и сериализации**                                            

```python
def sqlalchemy_to_pydantic(db_obj, pydantic_model):
    # Создаем словарь `data`, содержащий все атрибуты объекта `db_obj` (который 
    # является экземпляром модели SQLAlchemy).
    # Пропускаем все атрибуты, начинающиеся с '_', так как они являются внутренними
    # атрибутами SQLAlchemy и не относятся к данным модели.
    data = {key: value for key, value in db_obj.__dict__.items() if not key.startswith('_')}

    # Получаем типы полей (аннотации типов) для pydantic модели. Это нужно для понимания 
    # того, какого типа должны быть поля в итоговой модели Pydantic.
    type_hints = get_type_hints(pydantic_model)

    # Перебираем ключи и значения в словаре `data`.
    for key, value in data.items():
        # Проверяем, является ли значение списком. Это важно для обработки вложенных 
        # отношений, например, когда один объект пользователя имеет множество телефонных номеров.
        if isinstance(value, list):
            # Для каждого ключа, соответствующего списку, получаем тип 
            # связанной модели из аннотаций типов.
            related_model = type_hints[key].__args__[0]
            # Рекурсивно применяем функцию `sqlalchemy_to_pydantic` к каждому 
            # объекту в списке, преобразуя их в модели Pydantic.
            data[key] = [sqlalchemy_to_pydantic(obj, related_model) for obj in value]
        # Проверяем, является ли значение экземпляром datetime.
        elif isinstance(value, datetime):
            # Преобразуем объект datetime в Unix timestamp (целое число).
            data[key] = int(value.timestamp())

    # Проверяем, существует ли ключ 'phone_numbers' в данных. Если нет, 
    # создаем его и присваиваем пустой список.
    # Это предотвращает ошибки при создании Pydantic модели, если 
    # ожидается наличие этого поля.
    if 'phone_numbers' not in data:
        data['phone_numbers'] = []

    # Создаем и возвращаем экземпляр Pydantic модели, используя распаковку словаря `data`.
    # Это преобразует словарь в аргументы, которые принимает конструктор Pydantic модели.
    return pydantic_model(**data)


with DBConnector(db_url=url_engine) as session:
    # Получение данных из базы данных и их сериализация
    db_user = session.query(User).options(
        joinedload(User.phone_numbers)
    ).filter(User.id == 17).first()
    if db_user:
        user_data = sqlalchemy_to_pydantic(db_user, UserSchema)
        print(user_data.model_dump_json())  # Вывод в формате JSON
```

**Интеграция с запросами SQLAlchemy**                                                

```python
def sqlalchemy_to_pydantic(db_obj, pydantic_model):
    data = {key: value for key, value in db_obj.__dict__.items() if not key.startswith('_')}

    # Получаем типы полей модели
    type_hints = get_type_hints(pydantic_model)

    for key, value in data.items():
        if isinstance(value, list):  # Обработка списка связанных объектов
            # Получаем тип поля из type_hints
            related_model = type_hints[key].__args__[0]
            data[key] = [sqlalchemy_to_pydantic(obj, related_model) for obj in value]
        elif isinstance(value, datetime):  # Преобразование datetime в timestamp
            data[key] = int(value.timestamp())

    if 'phone_numbers' not in data:
        data['phone_numbers'] = []

    return pydantic_model(**data)


with DBConnector(db_url=url_engine) as session:
    # Получение данных из базы данных и их сериализация
    db_user = session.query(User).options(
        joinedload(User.phone_numbers)
    ).filter(User.id == 5).first()
    if db_user:
        user_data = sqlalchemy_to_pydantic(db_user, UserWithPhoneNumbersSchema)
        print(user_data.model_dump_json())  # Вывод в формате JSON
```

```python
def sqlalchemy_to_pydantic(db_obj, pydantic_model):
    data = {key: value for key, value in db_obj.__dict__.items() if not key.startswith('_')}

    # Получаем типы полей модели
    type_hints = get_type_hints(pydantic_model)

    for key, value in data.items():
        if isinstance(value, list):  # Обработка списка связанных объектов
            # Получаем тип поля из type_hints
            related_model = type_hints[key].__args__[0]
            data[key] = [sqlalchemy_to_pydantic(obj, related_model) for obj in value]
        elif isinstance(value, datetime):  # Преобразование datetime в timestamp
            data[key] = int(value.timestamp())

    if 'phone_numbers' not in data:
        data['phone_numbers'] = []

    return pydantic_model(**data)


with DBConnector(db_url=url_engine) as session:
    # Получение данных из базы данных и их сериализация
    db_user = session.query(User).options(
        joinedload(User.phone_numbers)
    ).filter(User.id == 5).first()
    if db_user:
        user_data = sqlalchemy_to_pydantic(db_user, UserSchema)
        print(user_data.model_dump_json(indent=4))  # Вывод в формате JSON
```

---

# **Alembic**                                                        

**Alembic** — это легковесная, базирующаяся на миграциях библиотека для                                                                                             
`SQLAlchemy`. Она создана для **управления изменениями в схеме базы данных**,                                                                                                      
позволяя отслеживать, модифицировать и создавать схему базы данных.                                                                                                       

Использование `Alembic` особенно полезно в средах, где работают **несколько**                                                                                                       
**разработчиков** и/или когда приложения развертываются на разных                                                                                                      
стадиях или окружениях.                                                                                                      

---
# **Main Components of Alembic**                                              

**Миграции**: Это основная функциональность `Alembic`. Миграции позволяют                                                                                                      
вносить изменения в схему базы данных, такие как добавление/удаление                                                                                                      
таблиц или столбцов, изменение типов данных столбцов и т.д.                                                                                                      

**Ревизии**: Каждая миграция в `Alembic` представляет собой ревизию.                                                                                                       
Ревизии обычно состоят из двух методов: `upgrade()` и `downgrade()`.                                                                                                       
`upgrade()` используется для применения изменений схемы, а                                                                                                       
`downgrade()` — для отката этих изменений.                                                                                                      

**Скрипты Миграции**: `Alembic` позволяет писать скрипты миграции на                                                                                                       
`Python`, что дает большую гибкость и контроль над процессом миграции.                                                                                                      

---
# **Alembic Workflow**
**Инициализация**: Сначала необходимо инициализировать `Alembic` в проекте,                                                                                                       
что создаст каталог миграций и файл конфигурации.                                                                                                      

**Создание Ревизии**: Для создания новой миграции используется команда                                                                                                       
`alembic revision -m "описание"`. Это создаст новый скрипт миграции.                                                                                                      

**Редактирование Скрипта Миграции**: После создания скрипта, его                                                                                                      
необходимо отредактировать, добавив нужные изменения в методы                                                                                                       
`upgrade()` и `downgrade()`.                                                                                                      

**Применение Миграции**: Чтобы применить миграцию к базе данных,                                                                                                      
используется команда `alembic upgrade head`.                                                                                                      

**Откат Миграции**: Если нужно отменить последние изменения,                                                                                                       
используется команда `alembic downgrade -1`.                                                                                                      

---

**установка alembic**                                              

Сперва нужно установить доп библиотеку алембик (`pip install alembic`)                                              

После чего нужно сынициализировать эту махину:                                                                                           
`alembic init alembic`(Это создаст директорию "alembic" в вашем проекте                                                                                         
с файлами конфигурации.)                                              
Потом нужно будет определить инициализацию скриптов в файле `alembic.ini`:                                                                                     

```python
[alembic]
# path to migration scripts
script_location = lesson_22_code/alembic
...
...
...
# the output encoding used when revision files
# are written from script.py.mako
# output_encoding = utf-8

sqlalchemy.url =
```

В Файле `alembic/env.py` добавить строчки:                                                                                        

```python
import os
from dotenv import load_dotenv

load_dotenv()

url_engine = os.getenv('DB_POS_URL')

context.config.set_main_option("sqlalchemy.url", url_engine)
...
...
...
# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = Base.metadata
```

Создать первую миграцию:                                                                                             

`alembic revision --autogenerate -m "Initial migration"`                                              

Это создаст новый файл миграции в директории "alembic/versions"                                                                                       
соответствующий вашим изменениям в модели.                                                                                           

Откройте созданный файл миграции и троху поредачьте его.                                                                                             
Нас интересует именно функция `upgrade`                                                                                            

```python
def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
```

Применить миграцию к Базе Данных можно след командой:                                                                                                

`alembic upgrade head`                                              

Это применит миграцию и создаст то, шо вы там прописали в нужном                                                                                             
вам методе.                                                                                             

После выполнения всех шагов, у вас будет успешно выполнена                                                                                       
миграция, и ваша база данных будет обновлена\создана.                                                                                        

---

**upgrade():**                                              
Метод **upgrade()** используется для применения к базе данных изменений,                                              
заданных в файле миграции. При запуске миграции `Alembic` выполняет метод                                              
`upgrade()` для приведения схемы базы данных в актуальное состояние.                                              
Этот метод обычно содержит операции **SQL** или код манипулирования                                              
схемой `SQLAlchemy` для создания новых таблиц, изменения существующих                                              
таблиц, добавления столбцов, модификации данных и т.д. Этот метод                                              
должен содержать операции, необходимые для возврата изменений                                              
схемы, внесенных в соответствующем методе `upgrade()`.                                              


**downgrade():**                                              
Метод `downgrade()` используется для отмены изменений, сделанных соответствующим                                              
методом `upgrade()`. Если необходимо откатить изменения, внесенные в                                              
результате определенной миграции, `Alembic` выполнит метод `downgrade()`                                              
для отмены изменений. Этот метод должен содержать операции, необходимые                                              
для отмены изменений схемы, внесенных в соответствующем методе `upgrade()`.                                              

`Alembic` позволяет создавать более сложные миграции, включая изменение                                                                                        
структуры таблиц, добавление новых таблиц и другие операции с базой данных.                                                                                                  
Он предоставляет мощные средства для управления схемой базы данных в проекте.                                                                                    

---

# **Home task**                                              

Написать **НЕБОЛЬШУЮ** систему с переводами деняк)))))                                              

Продумать необходимые для этого модели                                              

Необходимые секретные данные должны **хэшироваться**                                              

Можно будет                                              
**создавать** пользователя,                                              
**обновлять** нужную инфу,                                              
**просматривать** нужную инфу                                                                                           
Иметь возможность **закидывать** деньги на счёт,                                              
**снимать** их                                              
и **переводить**                                              


Все операции должны быть реализованы через базы данных, никаких больше файлов.                                                                                           
Все операции должны быть с соблюдением `ACID` свойств.                                             

подключение к базе данных(или MySQL, или PostgreSQL)                                             

работа принимается ТОЛЬКО в виде PR на меня от другой ветки.                                             

Валидация полей через `pydantic`(*****)                                                                                           
работа с БД через `SQLalchemy`                                                                                           
