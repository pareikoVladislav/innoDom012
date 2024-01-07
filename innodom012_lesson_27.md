<!-- TOC -->
* [**Django Views**](#django-views)
* [**HTML**](#html)
* [**HTML Structure**](#html-structure)
* [**Templates**](#templates)
* [**Django ORM Queryset**](#django-orm-queryset)
* [**StaticFiles**](#staticfiles)
* [**FORMS**](#forms)
<!-- TOC -->

# **Django Views**

**Views (представления)** – ключевой компонент в создании веб-приложений,       
они позволяют обрабатывать HTTP-запросы и возвращать HTTP-ответы.     
Они отвечают за 3 основные функции: 
* как данные будут получены
* как данные будут обработаны
* как данные будут представлены пользователю


Все представления на сервере доступны от маршрутизатора, **url-адресов**       
которые он хранит, они содержатся в файле `urls.py`. Все представления      
приложения хранятся в файле `views.py`.      

Создадим первое представление и определим его маршрут:

```python
from django.http import HttpResponse


def hello_world(request):
    return HttpResponse('Hello, World!')
```

Представление описывается как функция, которая принимает в себя     
запрос **request** и возвращает ответ(**response**). В данном случае ответ - это      
**HttpResponse**, он в свою очередь хранит сообщение, которое будет        
передано в виде ответа         

Для определения маршрута в каждом приложении требуется создать       
дополнительный файл `urls.py` **(он не создается автоматически)**, для        
правильной композиции приложения там должны храниться `url-адреса`,        
принадлежащие приложению        


Далее в файле `urls.py` проекта (или же в отдельном файле router)                                                 
требуется зарегистрировать файл `urls.py` приложения, и так для                                             
каждого приложения при необходимости                                            


```python
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # ...
    path('', include('<app_name>.urls')),
]
```

Изначально файл `urls.py` приложения уже имеет один `route` (маршрут), который        
ссылается на админ панель сайта. Для регистрации `urls` приложения       
используется функция `include`, которая хранит строку - ссылку на `urls.py`-файл      
в приложении. Далее определим маршрут представления:       

```python
from django.urls import path
from .views import hello_world

urlpatterns = [
    path('hello/', hello_world),
]
```

Теперь представление доступно по адресу
`http://localhost:8000/home/hello`

---

# **HTML**

За клиентскую часть веб-приложения отвечают frontend-разработчики,          
однако Django позволяет создавать несложную клиентскую часть вебприложений         
без особых усилий, достаточно знать `HTML`.       


**HTML** – это язык разметки, он позволяет создавать структуру страницы          
приложения. Язык состоит из набора тегов, которые определяют        
определенный тип содержимого на странице (изображения, параграфы,         
заголовки, ссылки и др.).           


Для форматирования структур используется язык `CSS`. А для закладывания        
пользовательской логики (например, клик на кнопку) в эти структуры        
используется язык программирования `JavaScript`.          


Для создания HTML-разметки требуется создать файл с расширением `.html`,            
прописать скелет приложения и вписать в него теги для вашей страницы.         
Теги могут содержать в себе атрибуты, а также могут быть вложенными         
друг в друга. Большинство тегов открываются и закрываются.              


---

# **HTML Structure**

* `<!DOCTYPE html>` - объявление типа документа (Document Type Declaration),           
которое указывает на то, что документ является HTML5-документом          

* `<html lang="en">` - открывающий тег, который обозначает начало HTML-документа.         
Атрибут `lang="en"` указывает на язык, используемый в документе            
(в данном случае, английский).      


* `<head>` - открывающий тег, который содержит метаинформацию о документе     
и его свойствах. Внутри тега `<head>` располагаются элементы, такие как         
`<meta>`, `<title>`, `<link>`


* `<meta charset="UTF-8">` - используется для указания кодировки символов       
документа. Атрибут `charset="UTF-8"` указывает на использование кодировки       
`UTF-8`, которая поддерживает широкий спектр символов и языков          


* `<title>Title</title>` - определяет заголовок документа, который         
отображается в заголовке окна браузера или на вкладке      


* `<body>` - открывающий тег, который обозначает начало основного        
содержимого HTML-документа.          


**Основные(но не все) HTML теги:**


| Tag                                                 | Description                                                                                                        |
|-----------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| <html>                                              | Определяет начало и конец HTML-документа                                                                           |
| <head>                                              | КОнтейнер для метаинформации о документе и его свойствах                                                           |
| <title>                                             | Определяет заголовок документа, отображаемый в браузере                                                            |
| <meta>                                              | Устанавливает метаданные о документе, такие как кодировка                                                          |
| <body>                                              | Определяет основное содержимое HTML-документа                                                                      |
| <h1>, <h2>, <h3>,<br/><h4>, <h5>, <h6>              | Заголовки разных уровней. Чем меньше цифра, тем больше шрифт.<br/>Заголовой первого уровня может быть только один. |
| <p>                                                 | Параграф текста(обычно туда улетают разные небольшие абзацы и прочее)                                              |
| <a>                                                 | Создаёт гиперссылку на другую страницу, или сторонний адрес                                                        |
| <img>                                               | Вставляет изображение. Можно так же указывать значение по умолчанию, если картинка не может быть вставлена         |
| <ul>, <ol>, <li>                                    | СОздание неупорядоченного(маркированного) и упорялоченного (нумерованного)<br/>списков                             |
| <table>, <tr>, <th>, <td>                           | Создание таблицы и её элементов. (Строки(tr), столбцы(th) и ячейки(td))                                            |
| <form>, <input>, <textarea>,<br/><select>, <button> | Создание формы и её элементов (поля ввода, поле текста, выбор из списка, кнопки)                                   |
| <div>, <span>                                       | Контейнерные элементы для группировки и стилизации содержимого                                                     |
| <strong>, <b>                                       | Выделение текста жирным шрифтом                                                                                    |
| <em>, <i>                                           | Курсивное выделение текста                                                                                         |
| <br>                                                | Перенос строки                                                                                                     |
| <hr>                                                | Горизонтальная линия                                                                                               |


---

# **Templates**

**Шаблоны (templates)** – это страницы приложения, они позволяют отделять и           
манипулировать логикой отображения информации на странице.          

Шаблоны пишутся с помощью Django-шаблонизатора. Шаблонизатор позволяет        
совмещать HTML и Python-код для манипулирования вашей страницей. Все         
шаблоны хранятся в папке templates, которая создаётся в каталоге вашего       
проекта. Для того, чтобы Django проект видел ваши шаблоны, требуется в        
список ключа DIRS добавить название папки с шаблонами.


Давайте создадим представление, которое позволит рендерить шаблон(HTML) и
выводить данные из представления:

```python
# apps.todo.views
from django.shortcuts import render


def hello_page(request):
    context = {
      "welcome_message": "Hello from the first View!!!",
    }
    
    return render(request, "home.html", context=context)
```

С помощью функции `render` мы можем выбрать шаблон из каталога       
`templates` и данные в виде словаря, которые получает шаблон. Функция        
`render` принимает `request` для того, чтобы выстроить ответ от пришедшего          
запроса. Запрос высылается при переходе на маршрут к нашему представлению             


Далее получим данные в шаблоне:

```html
<!--templates.main.html-->
<!DOCTYPE html>
<html lang="en">
<head>
    {% load static %}
    <meta charset="UTF-8">
    <link rel="stylesheet" href="{% static 'todo/css/styles.css' %}">
    <link rel="stylesheet" href="{% static 'todo/css/tasks.css' %}">
    <link rel="stylesheet" href="{% static 'todo/css/task_form.css' %}">
    <link rel="stylesheet" href="{% static 'todo/css/task_info.css' %}">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet"
          integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"
            integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM"
            crossorigin="anonymous"></script>
    <title>{% block title %}{% endblock %}</title>
</head>
<body>
<div class="container">
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">MyApp</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
                    data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent"
                    aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    <li class="nav-item">
                        <a class="nav-link active" aria-current="page" href="#">Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Profile</a>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button"
                           data-bs-toggle="dropdown" aria-expanded="false">
                            Tasks
                        </a>
                        <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                            <li><a class="dropdown-item" href="#">All</a></li>
                            <li><a class="dropdown-item" href="#">Subtasks</a></li>
                            <li>
                                <hr class="dropdown-divider">
                            </li>
                            <li><a class="dropdown-item" href="#">Board</a></li>
                        </ul>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#" tabindex="-1">Add Task</a>
                    </li>
                </ul>
                <form class="d-flex">
                    <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
                    <button class="btn btn-outline-success" type="submit">Search</button>
                </form>
            </div>
        </div>
    </nav>
    {% block content %}
    {% endblock %}
</div>
</body>
</html>
```

Если вдруг вопросы о том, а шо за тэги у нас есть вообще? Вот:

| Tag           | Description                                                                                       |
|---------------|---------------------------------------------------------------------------------------------------|
| {% for %}     | Итерация по элементам списка, или QuerySet                                                        |
| {% endfor %}  | Завершение блока цикла                                                                            |
| {% if %}      | Условное выполнение блока кода                                                                    |
| {% else %}    | Альтернативный блок кода, выполняющийся<br/>при отрицательном условии в {% if %}                  |
| {% elif %}    | Альтернативное условие проверки в блоке {% if %}                                                  |
| {% endif %}   | Завершение блока {% if %}                                                                         |
| {% include %} | Включение другого шаблона в текущий                                                               |
| {% block %}   | Определение блока кода, который может быть выполнен<br/>и так же переопределён в дочернем шаблоне |
| {% extends %} | Наследование одного, или нескольких шаблонов от другого, родительского                            |
| {% load %}    | Загрузка и использование других, доп фильтров и тегов                                             |
| {% url %}     | Создание url-адреса на основе имени маршрута                                                      |
| {% with %}    | Создание переменной с ограниченной областью видимости                                             |
| {% comment %} | Коммент                                                                                           |

---

# **Django ORM Queryset**

Django ORM предоставляет с помощью атрибута `objects` (менеджера моделей)           
удобную выборку объектов из вашей БД, он содержит несколько основных методов:        

```python
all_objects = YourModel.objects.all()  # выборка всех записей из таблицы
```

```python
filtered_objects = YourModel.objects.filter(field=value)  # выборка записей с определённым значением поля
```

```python
one_object = YourModel.objects.get(field=value)  # используется для выборки одной записи с
# определённым значением поля, если записей с
# таким условием несколько, будет получена первая
# лучше использовать метод get_object_or_404
```

```python
excluded_objects = YourModel.objects.exclude(field=value)  # позволяет исключить
# определенные записи по значению
# поля
```

```python
sorted_objects = YourModel.objects.order_by('field')  # позволяет отсортировать выборку
# из таблицы
```

```python
from django.db.models import Q
from your_app.models import YourModel


objects = YourModel.objects.filter(Q(field=value) | Q(field=value))

# Q позволяет добавить оператор или (|), и (&)
```


Помимо выборки, с помощью `.save()` можно сохранить запись, `.delete()` -
удалить, `create()` - создать.         


Попробуем вывести все новости из таблицы на сайт:

```python
# apps.todo.views
from django.shortcuts import render


def get_all_tasks(request):
    tasks = Task.objects.all()

    content = {
        "tasks": tasks,
    }

    return render(
        request=request,
        template_name='todo/all_todos.html',
        context=content
    )
```

```html
<!--templates/todo/all_todos.html-->
{% extends 'main.html' %}

{% block title %}
    All Tasks
{% endblock %}

{% block content %}
    <div class="todos">
        {% for task in tasks %}
            <div class="task">
                <h2>title: {{ task.title }}</h2>
                <h4>category: {{ task.category }}</h4>
                <h4>status: <b>{{ task.status }}</b></h4>
                <p><b>description: </b>{{ task.description }}</p>
                <h4>creator: {{ task.creator }}</h4>
                <h4>date started: {{ task.date_started }}</h4>
                <h4>deadline: {{ task.deadline }}</h4>
            </div>
        {% endfor %}
    </div>
{% endblock %}

```

```python
# apps.todo.urls
from django.urls import path

from apps.todo.views import get_all_tasks

app_name = 'todos'


urlpatterns = [
    path("", get_all_tasks, name='all-tasks'),
]
```
И наш `router`:
```python
# apps.router
from django.urls import path, include


urlpatterns = [
    path("tasks/", include('apps.todo.urls')),
]

```

---

# **StaticFiles**

Файлы, которые в процессе вашего приложения никогда не изменятся       
являются `Static files` (статическими файлами). Это могут быть         
изображения, `.css` файлы, `.js` файлы и др., которые связаны с внешним           
видом и функциональностью веб-приложения.     


Для того, чтобы использовать такие файлы требуется создать папку `static`
в каталоге приложения и подключить её в настройках проекта:

```python
# settings.py
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')


MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"
```

После этой махинации, чтобы на стороне браузера ваша статика так же была                                           
видна, необходимо добавить её к урлам:                                              

```python
# app.urls.py
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.router")),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  # new
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # new

# new
if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

```

Для того, чтобы по иерархии не было конфликтов, если вдруг вы будите создавать                                           
файлы с одинаковым названием, просто в разных приложениях, необходимо в папке `static`                                     
создавать папку с названием самого приложения, а в ней уже дополнительно три папки:                                     

* `css`
* `js`
* `img`

Стандартная структура будет выглядеть так:                                           
```
<app_name> |
           | static |
                    | <app_name> |
                                 | css
                                 | js
                                 | img
```

```html
<!--templates/todo/all_todos.html-->
{% extends 'main.html' %}
{% load static %} <!-- NEW -->

{% block title %}
    All Tasks
{% endblock %}

{% block content %}
    <link rel="stylesheet" href="{% static 'todo/css/tasks.css' %}">  <!-- NEW -->
    <div class="todos">
        {% for task in tasks %}
            <div class="task">
                <h2>title: {{ task.title }}</h2>
                <h4>category: {{ task.category }}</h4>
                <h4>status: <b>{{ task.status }}</b></h4>
                <p><b>description: </b>{{ task.description }}</p>
                <h4>creator: {{ task.creator }}</h4>
                <h4>date started: {{ task.date_started }}</h4>
                <h4>deadline: {{ task.deadline }}</h4>
            </div>
        {% endfor %}
    </div>
{% endblock %}

```

И напишем стилей в самом CSS:

```css
/*apps.todo.static.todo.css.styles.css*/
body {
    background: #b2e5af;
}

.container {
    max-width: 1440px;
    margin: 0 auto;
}
```

```css
/*apps.todo.static.todo.css.tasks.css*/
.todos {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
    justify-content: center;
    margin-top: 30px;
}

.task {
    width: 100%;
    height: 100%;
    box-sizing: border-box;
    border: 1px solid #2ECC71;
    padding: 10px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(46, 204, 113, 0.5);
    background-color: #ecf0f1;
}

.task h2, .task h4, .task p {
    margin: 5px 0;
}

.task h4 {
    color: #16a085;
}

.task h4 b {
    color: chocolate;
}


.task p {
    color: #34495e;
}


.task h4[style*="color: chocolate"] {
    color: #e67e22;
}

.task-link {
    display: flex;
    text-decoration: none;
    color: inherit;
    width: 300px;
    margin-bottom: 20px;
}

.task-link:hover {
    background-color: #dfe6e9; /* Светлый фон при наведении */
    border-color: #27ae60; /* Темно-зеленая граница при наведении */
}

.task-link:hover h2 {
    color: #27ae60;
}
```
---

# **FORMS**

`Django` предоставляет специальные возможности для создания форм на         
странице, которые можно использовать многократно в разных местах, они            
упрощают валидацию данных, помогают связывать формы с моделями и            
многое другое. Создание форм происходит в приложении и файле `forms.py`         
Создадим форму создания новой задачи      


```python
# apps.todo.forms.py
from django.contrib.auth.models import User
from django.forms import fields, widgets, ModelForm
from django.forms import ModelChoiceField

from apps.todo.models import (
    Task,
    SubTask,
    Category,
    Status,
)


class CreateTaskForm(ModelForm):

    title = fields.CharField(max_length=25)
    description = fields.CharField(max_length=1500, widget=fields.Textarea)
    creator = ModelChoiceField(queryset=User.objects.all())
    category = ModelChoiceField(queryset=Category.objects.all(), required=False)
    status = ModelChoiceField(queryset=Status.objects.all())

    date_started = fields.DateField(widget=widgets.DateInput(attrs={'type': 'date'}))
    deadline = fields.DateField(widget=widgets.DateInput(attrs={'type': 'date'}))
    updated_at = fields.DateTimeField(widget=widgets.DateTimeInput(attrs={'type': 'datetime-local'}), required=False)
    deleted_at = fields.DateTimeField(widget=widgets.DateTimeInput(attrs={'type': 'datetime-local'}), required=False)

    class Meta:
        model = Task
        fields = '__all__'

```

Создание формы схоже на создание модели, тут так же имеются поля, которые                                              
хранятся в модуле `fields`. Так же, если какое-то поле должно быть                                                     
выпадающим списком, в котором будут данные из присоединённой таблицы, нужно                                                   
использовать класс `ModelChoiceField`, в котором прописывать `queryset` тех                                               
данных, которые должны будут отображаться.                                         
`widget` помогают определить, как именно конкретное поле должно быть отображено                                             
в браузере (HTML странице)                                                                    

Каждое поле формы (`Field`) в `Django` может быть связано с виджетом, который                                                                     
управляет следующими аспектами:                                                                    

**HTML-представление поля**: Виджет определяет **HTML-код**, который будет использоваться                                                                    
для отображения поля формы. Например, для текстового поля (`CharField`) это может                                                                     
быть `<input type="text">`, а для поля выбора (`ChoiceField`) - `<select>`.                                                                    

**Атрибуты HTML-элементов**: Виджеты позволяют определять дополнительные HTML-атрибуты                                                                     
для поля, такие как `class`, `id`, `style`, `placeholder` и т.д.                                                                    

Обработка данных на стороне клиента: Некоторые виджеты могут включать `JavaScript`                                                                    
для добавления интерактивных функций, таких как календари для выбора даты или                                                                     
слайдеры для числовых значений.                                                                     

Виджеты могут быть использованы в формах двумя основными способами:                                                                     

1) Назначение виджета при определении поля формы:                                                  
```python
class MyForm(forms.Form):
    my_field = forms.CharField(widget=forms.Textarea)
# Здесь поле my_field будет отображаться как многострочное текстовое поле (<textarea>).
```

2) Изменение виджета для модельной формы:                                                
```python
class MyModelForm(ModelForm):
    class Meta:
        model = MyModel
        fields = ['my_field']
        widgets = {
            'my_field': forms.Textarea(attrs={'placeholder': 'Введите текст'})
        }

# В этом примере для поля my_field модели MyModel устанавливается многострочное
# текстовое поле с атрибутом placeholder.
```

В шаблоне мы создаём форму, которая дополнительно содержит кнопку             
`submit`. Если в форме указан атрибут `method`, тогда при нажатии на кнопку             
формы на сервер будет отправлен `post-запрос`      

```html
<!--templates/todo/create_task.html-->
{% extends 'main.html' %}
{% block title %}
    Create New Task
{% endblock %}

{% block content %}
    <div class="new-task-title">
        Create New Task
    </div>
    <div class="new-task-container">
        <form method="post">
            {% csrf_token %}

            <div class="mb-3">
                <label for="title" class="form-label">Title</label>
                <input type="text" class="form-control" id="title" name="title" maxlength="25" placeholder="Title">
            </div>

            <div class="mb-3">
                <label for="description" class="form-label">Description</label>
                <textarea class="form-control" id="description" name="description" maxlength="1500"
                          placeholder="Description"></textarea>
            </div>

            <div class="mb-3">
                <label for="creator" class="form-label">Creator</label>
                <select class="form-control" id="creator" name="creator">
                    <option value="" selected="">---</option>
                    {% for user in users %}
                        <option value="{{ user.id }}">{{ user.username }}</option>
                    {% endfor %}
                </select>
            </div>

            <div class="mb-3">
                <label for="category" class="form-label">Category</label>
                <select class="form-control" id="category" name="category">
                    <option value="" selected="">---</option> <!-- For optional category -->
                    {% for category in categories %}
                        <option value="{{ category.id }}">{{ category.name }}</option>
                    {% endfor %}
                </select>
            </div>

            <div class="mb-3">
                <label for="status" class="form-label">Status</label>
                <select class="form-control" id="status" name="status">
                    <option value="" selected="">---</option>
                    {% for status in statuses %}
                        <option value="{{ status.id }}">{{ status.name }}</option>
                    {% endfor %}
                </select>
            </div>

            <div class="mb-3">
                <label for="date_started" class="form-label">Date Started</label>
                <input type="date" class="form-control" id="date_started" name="date_started">
            </div>

            <div class="mb-3">
                <label for="deadline" class="form-label">Deadline</label>
                <input type="date" class="form-control" id="deadline" name="deadline">
            </div>

            <button type="submit" class="btn btn-primary">Create</button>
        </form>
    </div>
{% endblock %}
```

В представлении прописываем 2 варианта событий, если приходит `POST` запрос,          
тогда собираем данные с помощью `request.POST.get` (“Название             
атрибута”) и создаём новый объект задачи в БД, иначе же просто                
рендерим страницу.             
Для соединения формы с шаблоном передаем ее экземпляр в `context`         

```python
# apps.todo.views.py
from django.shortcuts import render, redirect

from news.forms import CreateNewsForm
from news.models import News


def create_new_task(request):
    users = User.objects.all()
    categories = Category.objects.all()
    statuses = Status.objects.all()

    if request.method == "POST":
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            task_data = form.cleaned_data
            Task.objects.create(**task_data)
            return redirect('router:todos:all_tasks')

        context = {
            "form": form,
            "users": users,
            "categories": categories,
            "statuses": statuses
        }
    else:
        form = CreateTaskForm()
        context = {
            "form": form,
            "users": users,
            "categories": categories,
            "statuses": statuses
        }

    return render(
        request=request,
        template_name='todo/create_task.html',
        context=context
    )
```

ну и стилей накидаем, раз уж начали...:

```css
/*apps.todo.static.todo.css.task_form.css*/
.new-task-title {
    text-align: center;
    color: #2ECC71;
    font-size: 24px;
    font-weight: bold;
    margin-top: 30px;
    margin-bottom: 20px;
}

.new-task-container {
    border: 1px solid #2ECC71;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(46, 204, 113, 0.5);
    background-color: #ecf0f1;
    width: 600px;
    margin: 50px auto auto;
}

.new-task-container input[type="text"],
.new-task-container input[type="date"],
.new-task-container input[type="datetime-local"],
.new-task-container textarea {
    width: 100%;
    padding: 8px;
    margin: 8px 0;
    display: inline-block;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
}

.new-task-container button {
    width: 100%;
    background-color: #2ECC71;
    color: white;
    padding: 14px 20px;
    margin: 8px 0;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

.new-task-container button:hover {
    background-color: #45a049;
}

.new-task-container label {
    margin-top: 10px;
    display: block;
}
```

Давайте так же создадим форму для обновления задачи через браузер!

Создадим новую форму:

```python
# apps.todo.forms.py
class TaskUpdateForm(ModelForm):

    class Meta:
        model = Task
        fields = ('title', 'description', 'category', 'status', 'updated_at',)
```

Теперь нам нужно создать новую вьюшку(отображение) - спец функцию, которая       
должна отработать при триггере какого-то из эндпоинтов:

```python
# apps.todo.views.py
def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    categories = Category.objects.all()
    statuses = Status.objects.all()

    if request.method == 'POST':
        form = TaskUpdateForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect('router:todos:all_tasks')

        context = {
            "form": form,
            "categories": categories,
            "statuses": statuses
        }

    else:
        form = TaskUpdateForm(instance=task)

        context = {
            "form": form,
            "categories": categories,
            "statuses": statuses
        }

    return render(
        request=request,
        template_name='todo/update_task.html',
        context=context
    )
```

После нужно создать вэб шаблон, в котором мы собственно всё это дело отобразим:

```html
<!--templates/todo/update_task.html-->
{% extends 'main.html' %}

{% block title %}
    Update task
{% endblock %}

{% block content %}
	<div class="new-task-title">
        Update Task
    </div>
    <div class="new-task-container">
        <form method="post">
            {% csrf_token %}

            <div class="mb-3">
                <label for="title" class="form-label">Title</label>
                <input type="text" class="form-control" id="title" name="title" maxlength="25" placeholder="Title">
            </div>

            <div class="mb-3">
                <label for="description" class="form-label">Description</label>
                <textarea class="form-control" id="description" name="description" maxlength="1500"
                          placeholder="Description"></textarea>
            </div>

            <div class="mb-3">
                <label for="category" class="form-label">Category</label>
                <select class="form-control" id="category" name="category">
                    <option value="" selected="">---</option> <!-- For optional category -->
                    {% for category in categories %}
                        <option value="{{ category.id }}">{{ category.name }}</option>
                    {% endfor %}
                </select>
            </div>

            <div class="mb-3">
                <label for="status" class="form-label">Status</label>
                <select class="form-control" id="status" name="status">
                    <option value="" selected="">---</option>
                    {% for status in statuses %}
                        <option value="{{ status.id }}">{{ status.name }}</option>
                    {% endfor %}
                </select>
            </div>

            <div class="mb-3">
                <label for="updated_at" class="form-label">Updated At</label>
                <input type="date" class="form-control" id="updated_at" name="updated_at">
            </div>

            <button type="submit" class="btn btn-primary">Update</button>
        </form>
    </div>
{% endblock %}
```

В конце это дело всё нужно скрепить, создав отдельный эндпоинт для этих действий:

```python
# apps.todo.urls.py
from django.urls import path

from apps.todo.views import (
    get_all_tasks,
    create_new_task,
    update_task,  # NEW
)

app_name = 'todos'


urlpatterns = [
    path("", get_all_tasks, name='all_tasks'),
    path("create/", create_new_task, name='create-task'),
    path("<int:task_id>/update/", update_task, name='update-task'),  # NEW
]

```

Остаётся дело за малым:                                                 

Добавить возможность получать определённую задачу                                            

```python
# apps.todo.views.py
def get_task_info_by_task_id(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    context = {
        "task": task
    }

    return render(
        request=request,
        template_name='todo/task_info.html',
        context=context
    )
```

```html
<!--templates/todo/task_info.html-->
{% extends 'main.html' %}

{% block title %}
    {{ task.title }}
{% endblock %}

{% block content %}
    <div class="task-content">
        <div class="task-info">
            <h2>title: {{ task.title }}</h2>
            <h4>category: {{ task.category }}</h4>
            <h4>status: <b>{{ task.status }}</b></h4>
            <p><b>description: </b>{{ task.description }}</p>
            <h4>creator: {{ task.creator }}</h4>
            <h4>date started: {{ task.date_started }}</h4>
            <h4>deadline: {{ task.deadline }}</h4>
        </div>
        <div class="button-container">
            <button class="update-button"><a href="{% url 'router:todos:update-task' task.id %}">Update</a></button>
            <button class="delete-button"><a href="{% url 'router:todos:delete-task' task.id %}">Delete</a></button>
        </div>
    </div>
{% endblock %}
```

```css
/*apps.todo.static.todo.css.task_info.css*/
.task-content {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20px;
}

.task-info {
    border: 1px solid #2ECC71;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(46, 204, 113, 0.5);
    background-color: #ecf0f1;
    margin-bottom: 20px;
    width: 100%;
    max-width: 600px; /* Максимальная ширина для больших экранов */
}

.button-container {
    display: flex;
    justify-content: center;
    gap: 10px; /* Добавляет пространство между кнопками */
}


.update-button, .delete-button {
    padding: 10px 15px;
    border-radius: 5px;
    cursor: pointer;
    font-weight: bold;
    background-color: transparent; /* Прозрачный фон */
    color: #34495e; /* Цвет текста */
    transition: background-color 0.3s ease;
}

.update-button {
    border: 2px solid #27ae60; /* Зеленая граница */
    box-shadow: 0 0 10px rgba(46, 204, 113, 0.5);
}

.update-button a {
    text-decoration: none;
    color: black;
}

.update-button a:hover {
    color: white;
}

.update-button:hover {
    background-color: #27ae60;
    color: white;
}

.delete-button {
    border: 2px solid #e74c3c; /* Красная граница */
    box-shadow: 0 0 10px rgba(231, 76, 60, 0.5);
}

.delete-button a {
    text-decoration: none;
    color: black;
}

.delete-button a:hover {
    color: white;
}

.delete-button:hover {
    background-color: #e74c3c;
    color: white;
}
```
```python
# apps.todo.urls.py
urlpatterns = [
    path("", get_all_tasks, name='all-tasks'),
    path("create/", create_new_task, name='create-task'),
    path("<int:task_id>/", get_task_info_by_task_id, name='task-detail'),  # NEW
]
```


Добавить овзможность в этой задаче редактировать её и удалять                                            

```python
# apps.todo.views.py
def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    categories = Category.objects.all()
    statuses = Status.objects.all()

    if request.method == 'POST':
        form = TaskUpdateForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect('router:todos:all_tasks')

        context = {
            "form": form,
            "categories": categories,
            "statuses": statuses
        }

    else:
        form = TaskUpdateForm(instance=task)

        context = {
            "form": form,
            "categories": categories,
            "statuses": statuses
        }

    return render(
        request=request,
        template_name='todo/update_task.html',
        context=context
    )


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    task.delete()
    return redirect('router:todos:all-tasks')
```

```html
<!--templates/todo/update_task.html-->
{% extends 'main.html' %}

{% block title %}
    Update task
{% endblock %}

{% block content %}
	<div class="new-task-title">
        Update Task
    </div>
    <div class="new-task-container">
        <form method="post">
            {% csrf_token %}

            <div class="mb-3">
                <label for="title" class="form-label">Title</label>
                <input type="text" class="form-control" id="title" name="title" maxlength="25" placeholder="Title">
            </div>

            <div class="mb-3">
                <label for="description" class="form-label">Description</label>
                <textarea class="form-control" id="description" name="description" maxlength="1500"
                          placeholder="Description"></textarea>
            </div>

            <div class="mb-3">
                <label for="category" class="form-label">Category</label>
                <select class="form-control" id="category" name="category">
                    <option value="" selected="">---</option> <!-- For optional category -->
                    {% for category in categories %}
                        <option value="{{ category.id }}">{{ category.name }}</option>
                    {% endfor %}
                </select>
            </div>

            <div class="mb-3">
                <label for="status" class="form-label">Status</label>
                <select class="form-control" id="status" name="status">
                    <option value="" selected="">---</option>
                    {% for status in statuses %}
                        <option value="{{ status.id }}">{{ status.name }}</option>
                    {% endfor %}
                </select>
            </div>

            <div class="mb-3">
                <label for="updated_at" class="form-label">Updated At</label>
                <input type="date" class="form-control" id="updated_at" name="updated_at">
            </div>

            <button type="submit" class="btn btn-primary">Update</button>
        </form>
    </div>
{% endblock %}
```


Ну и ссылками подвязать всё                                                   

```html
<!--templates/main.html-->
<!DOCTYPE html>
<html lang="en">
<head>
    {% load static %}
    <meta charset="UTF-8">
    <link rel="stylesheet" href="{% static 'todo/css/styles.css' %}">
    <link rel="stylesheet" href="{% static 'todo/css/tasks.css' %}">
    <link rel="stylesheet" href="{% static 'todo/css/task_form.css' %}">
    <link rel="stylesheet" href="{% static 'todo/css/task_info.css' %}">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet"
          integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"
            integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM"
            crossorigin="anonymous"></script>
    <title>{% block title %}{% endblock %}</title>
</head>
<body>
<div class="container">
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="container-fluid">
            <a class="navbar-brand" href="{% url 'router:home' %}">MyApp</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
                    data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent"
                    aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    <li class="nav-item">
                        <a class="nav-link active" aria-current="page" href="{% url 'router:home' %}">Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Profile</a>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button"
                           data-bs-toggle="dropdown" aria-expanded="false">
                            Tasks
                        </a>
                        <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                            <li><a class="dropdown-item" href="{% url 'router:todos:all-tasks' %}">All</a></li>
                            <li><a class="dropdown-item" href="#">Subtasks</a></li>
                            <li>
                                <hr class="dropdown-divider">
                            </li>
                            <li><a class="dropdown-item" href="#">Board</a></li>
                        </ul>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'router:todos:create-task' %}" tabindex="-1">Add Task</a>
                    </li>
                </ul>
                <form class="d-flex">
                    <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
                    <button class="btn btn-outline-success" type="submit">Search</button>
                </form>
            </div>
        </div>
    </nav>
    {% block content %}
    {% endblock %}
</div>
</body>
</html>
```

---