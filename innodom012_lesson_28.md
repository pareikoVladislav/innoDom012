# **Finalize project. Django templates, forms, view-classes**

<!-- TOC -->
* [**Subtasks**](#subtasks-)
* [**Specified subtask info**](#specified-subtask-info-)
* [**Update specified task view**](#update-specified-task-view-)
* [**Update Subtask**](#update-subtask-)
* [**Create subtask**](#create-subtask-)
* [**Delete subtask**](#delete-subtask)
* [**New app, create login functionality**](#new-app-create-login-functionality)
* [**Registration**](#registration-)
* [**Profile info**](#profile-info)
* [**Logout**](#logout-)
<!-- TOC -->

Что ж, продолжим с вами создавать наш проект!                                                       

Сегодня по плану:


1) Добавить возможность смотреть список всех подзадач, или сообщение,                                                  
что подзадач нет.
2) Добавить возможность смотреть конкретную подзадачу.
3) Переделать отображение определённой задачи, чтобы там были видны                                                          
ещё и подзадачи, или же окно, что подзадач ешё нет                                                               
4) Добавить возможность обновлять подзадачу
5) Добавить возможность создавать новую подзадачу
6) ДОбавить возможность удалять подзадачу
7) Добавить формы логина и пароля


# **Subtasks**                                                                            

Для того, чтобы добавить возможность смотреть список всех подзадач,                                                    
напишем функцию, которая будет собирать все сущности из базы данных.                                                    
Нам так же нужно будет учитывать тот момент, что получать мы должны                                                     
будем не полностью все задачи, а только те, что пренадлежат пользователю,                                               
который и сделал этот запрос на получение:                                                     

```python
def get_subtasks_info(request):
    subtasks = SubTask.objects.filter(creator=request.user)  # именно благодаря фильтру мы получим то, что нам нужно.

    context = {
        "subtasks": subtasks
    }

    return render(
        request=request,
        template_name='todo/all_subtasks.html',
        context=context
    )
```

После чего нам нужно будет создать шаблон для того, чтобы это всё грамотно                                             
отобразить:                                                     

```html
...
{% block content %}
    <div class="subtasks">
        {% if subtasks %} <!-- Мы можем написать условие, что если сабтаски есть - отображаем их все. -->
            {% for subtask in subtasks %} <!-- -->
                <a href="#" class="subtask-link">
                    <div class="subtask">
                        <h2><span class="subtask-description">Title: </span>{{ subtask.title }}</h2>
                        <h4><span class="subtask-description">Category: </span>{{ subtask.category }}</h4>
                        <h4><span class="subtask-description">Status: </span><b>{{ subtask.status }}</b></h4>
                        <p><b><span class="subtask-description">Description: </span></b>{{ subtask.description }}</p>
                        <h4><span class="subtask-description">Task: </span>{{ subtask.task.title|slice:":10" }}
                            {% if subtask.task.title > 10 %}...{% endif %}</h4>
                        <h4><span class="subtask-description">Date started: </span>{{ subtask.date_started }}</h4>
                        <h4><span class="subtask-description">Deadline: </span>{{ subtask.deadline }}</h4>
                    </div>
                </a>
            {% endfor %} <!-- -->
        {% else %} <!-- Иначе мы отображать будем спец окошко, мол нет ни одной подзадачи -->
            <div class="no-subtasks-block">
                <h1>Looks like you don't have any subtask!</h1>
            </div>
        {% endif %} <!-- Всегда явно указываем закрытие наших блоков. Потому что html за них не шарит. -->
    </div>
{% endblock %}
```

Так же создать новый эндпоинт, чтобы наша функция могла отрабатывать:                                                  

```python
from apps.todo.views import (
    ...
    get_subtasks_info,  # NEW
)

...

urlpatterns = [
    ...
    path("subtasks/", get_subtasks_info, name='all-subtasks'),  # NEW
    ...
]
```

После этого нам так же нужно в нашей шапке обновить заглушку на новое значение:                                        

```html
...
        <li class="header-item">
            <a class="nav-link" href="{% url 'router:tasks:all-subtasks' %}">Subtasks</a>  <!-- NEW -->
        </li>
...
```

И немного стилей:                                                          

```css
.subtasks {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
    justify-content: center;
    margin-top: 30px;
}

.subtask {
    width: 100%;
    height: 100%;
    box-sizing: border-box;
    border: 1px solid rgba(22, 160, 133, 0.1);
    padding: 10px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(22, 160, 133, 0.3);
    background-color: inherit;
    transition: all 0.3s ease; /* Плавное изменение фона при наведении */
}

.subtask-description {
    color: #c3c1c1
}

.subtask h2, .subtask h4, .subtask p {
    margin: 5px 0;
    font-size: 28px;
    color: rgba(22, 160, 133, 0.8);
}

.subtask-link {
    display: flex;
    text-decoration: none;
    color: inherit;
    width: 400px;
    margin-bottom: 20px;
}

.subtask-link:hover {
    background-color: rgba(46, 204, 113, 0.07); /* Светлый фон при наведении */
    border-color: rgba(22, 160, 133, 0.4); /* Темно-зеленая граница при наведении */
}

.subtask-link:hover .subtask-description, h2, h4, p {
    color: rgba(22, 160, 133, 0.8);
}

.subtask-link:hover h2, .subtask-link:hover h4, .subtask-link:hover p {
    color: #c3c1c1
}

.no-subtasks-block {
    border: 1px solid #16A08566;
    text-align: center; /* Выравнивание текста и кнопки по центру */
    padding: 20px; /* Добавление отступов внутри блока */
    width: 447px;
    box-shadow: 0 0 10px rgba(22, 160, 133, 0.7);
}

.no-subtasks-block h1 {
    color: rgba(22, 160, 133, 0.8);
    font-weight: 700;
    font-size: 45px;
    margin-bottom: 20px;
}

.create-subtask {
    border: 2px solid #16a085;
    background-color: transparent;
    color: #16a085;
    margin: 0 auto;
    padding: 10px 15px;
    text-decoration: none;
    border-radius: 5px; /* Слегка закругленные углы */
    display: inline-block; /* Блочно-строчный элемент для правильного отображения отступов и бордера */
    transition: background-color 0.3s, color 0.3s; /* Плавный переход для фона и текста */
}

.create-subtask:hover {
    background-color: rgba(22, 160, 133, 0.1);
    color: #e0e0e0;
}

```

В конце не забываем собрать всю статику, чтобы стили вступили в силу:                                                   

`python manage.py collectstatic`

# **Specified subtask info**                                                     

Штош, теперь давайте добавим возможность просматривать инфо об                                                          
определённой задаче. Нам необходимо при клике на определённую сабтаску                                                     
передавать дальше `ID` этой сабтаски, на основе которого мы и будем                                                    
получать конкретный объект сабтаски.                                                                  

```python
def get_subtask_info_by_id(request, subtask_id):
    subtask = get_object_or_404(SubTask, id=subtask_id)

    context = {
        "subtask": subtask
    }

    return render(
        request=request,
        template_name='todo/subtask_info.html',
        context=context
    )
```

Здесь ничего особенного нет. Мы сперва получаем определённую задачу,                                                    
обращаясь к методу получения объекта, или же вывода ошибки 404. Такой                                                
подход избавит нас с вами от необходимости писать лишние условия, код                                                 
становится чуточку чище, легче, более понятнее.                                                                          

После мы создаём словарь контекста, который мы будем передавать в метод                                                  
`render`, ключ этого словаря будет впоследствии передан в наш шаблон.                                                   


Так же мы создаём новый `url`:                                                     

```python
from apps.todo.views import (
    ...
    get_subtask_info_by_id  # NEW
)

...

urlpatterns = [
    ...
    path("subtasks/<int:subtask_id>/", get_subtask_info_by_id, name='subtask-info'),  # NEW
    ...
]
```

Дальше создадим шаблон:                                                                        

```html
{% block content %}
    <div class="subtask-container">
        <div class="subtask-block">
            <h2 class="subtask-block-info"><span class="subtask-info-fields">Title: </span>{{ subtask.title }}</h2>
            <h4 class="subtask-block-info"><span class="subtask-info-fields">Category: </span>{{ subtask.category }}</h4>
            <h4 class="subtask-block-info"><span class="subtask-info-fields">Status: </span><b>{{ subtask.status }}</b></h4>
            <p class="subtask-block-info"><span class="subtask-info-fields">Description: </span>{{ subtask.description }}</p>
            <h4 class="subtask-block-info"><span class="subtask-info-fields">Creator: </span>{{ subtask.creator }}</h4>
            <h4 class="subtask-block-info"><span class="subtask-info-fields">Date started: </span>{{ subtask.date_started }}</h4>
            <h4 class="subtask-block-info"><span class="subtask-info-fields">Deadline: </span>{{ subtask.deadline }}</h4>
        </div>
        <div class="button-container">
            <a href="#" class="update-button">Update</a>
            <a href="#" class="delete-button">Delete</a>
        </div>
    </div>
{% endblock %}
```

Обновим в файле `all_subtasks.html` ссылку с заглушки на путь к нужному                                                  
`url`:                                                                   

```html
...
            {% for subtask in subtasks %}
                <a href="{% url 'router:tasks:subtask-info' subtask.id %}" class="subtask-link">  <!-- NEW -->
...
```

И остаются стили:                                                                            

```css
.subtask-container {
    width: 750px;
    margin: 8em auto 0;
    display: flex;
    flex-direction: column;
}

.subtask-block {
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 0 15px rgba(46, 204, 113, 0.5);
    background-color: inherit;
    margin-bottom: 20px;
    width: 100%;
    box-sizing: border-box;
}

.subtask-info-fields {
    color: #c3c1c1;
    font-size: 28px;
}

.subtask-block-info {
    margin: 5px 0;
    font-size: 28px;
    color: rgba(22, 160, 133, 0.8);
}

```

# **Update specified task view**                                                            

Теперь, когда у нас уже потенциально есть подзадачи, давайте                                                 
добавим возможность для нашей задачи отображать все её возможные                                                     
подзадачи. Если же таковых нет - отображать сообщение, что подзадач                                                 
пока что нет, и так же кнопку создания подзадачи.                                                              

Начнём с функции, как обычно.                                                        
Нам необходимо немного обновить уже существующую функцию на получение                                              
конкретной задачи. А именно - добавить туда список относящихся к ней                                                     
подзадач:                                                                 
```python
def get_task_info_by_task_id(request, task_id):
    ...
    subtasks = SubTask.objects.filter(task=task_id)  #  NEW

    context = {
        ...
        "subtasks": subtasks  # NEW
    }
```

Далее, необходимо обновить так же и шаблон. Добавим новый блок сразу после                                              
`task-block` класса, всё это будет внутри класса `task-content`:                                                   

```html
<div class="task-content">
    <div class="task-block">
        ...
    </div>
    {% if subtasks %}
            <div class="task-subtasks">
                {% for subtask in subtasks %}
                    <div class="subtask-info">
                        <a href="{% url 'router:tasks:subtask-info' subtask.id %}" class="subtask-title">
                            {{ subtask.title|slice:":10" }}{% if subtask.title|length > 10 %}...{% endif %}
                        </a>
                        <h3>{{ subtask.status }}</h3>
                        <div class="button-container">
                            <a href="#"
                               class="update-button">Update</a>
                            <a href="#" class="delete-button">Delete</a>
                        </div>
                    </div>
                {% endfor %}
            </div>
        {% else %}
            <div class="no-subtasks-block">
                <h1>You don't have any subtasks for this task</h1>
                <a href="#" class="create-subtask">Create
                    subtask</a>
            </div>
        {% endif %}
</div>>
```

Как можно заметить, мы здесь так же добавляем условие, что если вдруг                                                
у текущей задачи нет подзадач - будем отображать сообщеньку о том,                                                    
что подзадач нет и допом кнопку на создание. Ссылку на это пока что глушим.                                              


Так же необходимо обновить и стили для новых блоков и элементов:                                                     

Сперва добавим специальный псевдо элемент-разделитель, чтобы можно                                                    
было отделить информацию задачи от всех подзадач:                                                  

```css
.task-block {
    ...
}

.task-block::after {
    content: '';
    position: absolute;
    top: 0;
    right: 0;
    width: 2px;
    height: 100%;
    box-shadow: 4px 0 10px rgba(46, 204, 113, 0.5);
    pointer-events: none;
}
```

И уже после добавляем стили для наших новых элементов подзадачи:                                                

```css
.task-subtasks {
    display: flex;
    flex-direction: column;
    height: 600px;
    max-height: 600px;
    overflow-y: auto;
    overflow-x: hidden;
    padding-right: 25px;
}

.task-subtasks::-webkit-scrollbar {
    width: 1px;
}

.task-subtasks::-webkit-scrollbar-track {
    background: rgba(22, 160, 133, 0.6);
}

.task-subtasks::-webkit-scrollbar-thumb {
    background-color: rgba(22, 160, 133, 0.6); /* Цвет бегунка скроллбара */
    border-radius: 10px; /* Закругленные углы для бегунка */
}

.task-subtasks::-webkit-scrollbar-thumb:hover {
    background-color: rgba(22, 160, 133, 0.8); /* Более темный цвет бегунка при наведении */
}

.subtask-info {
    background-color: inherit;
    border: 2px solid rgba(22, 160, 133, 0.6);
    box-shadow: 0 0 10px rgba(22, 160, 133, 0.8);
    width: 640px;
    height: 75px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-radius: 10px;
    margin-top: 3em;
    padding: 0 15px;
}

.subtask-title {
    text-decoration: none;
    color: rgba(22, 160, 133, 0.6);
    font-weight: 600;
    font-size: 26px;
    transition: 0.3s ease;
    width: 171px;
}

.subtask-title:hover {
    color: #c0bfbf;
    cursor: pointer;
}

.subtask-info h3 {
    color: rgba(22, 160, 133, 0.8);
    font-weight: 600;
    width: 171px;
}
```

# **Update Subtask**                                                                     

Получить список всех возможных сабтасок у нас возможность имеется,                                                    
так же как и возможность просматривать определённую. Теперь же добавим                                                  
возможность обновить полученную задачу, если есть такая необходимость.                                                  

Начнём с написания формы. Она будет достаточно простой, на основе специального                                           
класса `ModelForm`, который позволяет автоматически создать готовую форму с уже                                        
написанными валидаторами на основе настроек нашей модели. Всё, что нам нужно указать                                    
из основного - какую конкретную модель она будет обрабатывать и какие конкретные                                         
поля в ней:                                                        

```python
...
class SubTaskUpdateForm(ModelForm):
    class Meta:
        model = SubTask
        fields = ['title', 'description', 'category', 'status', 'deadline']
```

После чего нужно будет добавить функцию, которая должна будет срабатывать на `url`,                                     
запуская все наши процессы. В ней мы сперва будем собирать все статусы, категории                                         
для их дальнейшего отображения в дропбоксах, и так же саму подзадачу, которую мы                                        
будем обновлять. При прохождении пост запроса мы будем получать данные из формы,                                        
после чего подставлять их для обновления определённой сущности:                                                        

```python
def update_subtask(request, subtask_id):
    subtask = get_object_or_404(SubTask, id=subtask_id)
    categories = Category.objects.all()
    statuses = Status.objects.all()

    if request.method == 'POST':
        form = SubTaskUpdateForm(request.POST, instance=subtask)

        if form.is_valid():
            form.save()

            return redirect('router:tasks:subtask-info', subtask_id=subtask_id)

    else:
        form = SubTaskUpdateForm(instance=subtask)

    context = {
        "form": form,
        "subtask": subtask,
        "categories": categories,
        "statuses": statuses
    }

    return render(
        request=request,
        template_name='todo/update_subtask.html',
        context=context
    )
```

Так же добавим наш шаблон:                                              

```html
...
<div class="subtask-container-form">
        <form method="post" autocomplete="on">
            {% csrf_token %}

            <div class="subtask-mb-3">
                <label for="title" class="subtask-form-label">Title</label>
                <input type="text" class="subtask-form-control" id="title" name="title"
                       maxlength="25" value="{{ subtask.title }}">
            </div>

            <div class="subtask-mb-3">
                <label for="description" class="subtask-form-label">Description</label>
                <textarea class="subtask-form-control" id="description" name="description"
                          maxlength="1500">{{ subtask.description }}</textarea>
            </div>

            <div class="subtask-mb-3">
                <label for="category" class="subtask-form-label">Category</label>
                <select class="subtask-form-control" id="category" name="category">
                    <option value="{{ subtask.category.id }}" selected="{{ subtask.category }}">{{ subtask.category }}</option> <!-- For optional category -->
                    {% for category in categories %}
                        <option value="{{ category.id }}">{{ category.name }}</option>
                    {% endfor %}
                </select>
            </div>

            <div class="subtask-mb-3">
                <label for="status" class="subtask-form-label">Status</label>
                <select class="subtask-form-control" id="status" name="status">
                    <option value="{{ subtask.status.id }}" selected="{{ subtask.status }}">{{ subtask.status }}</option>
                    {% for status in statuses %}
                        <option value="{{ status.id }}">{{ status.name }}</option>
                    {% endfor %}
                </select>
            </div>

            <div class="subtask-mb-3">
                <label for="deadline" class="subtask-form-label">Deadline</label>
                <input type="date" class="subtask-form-control" id="deadline" name="deadline">
            </div>

            <button type="submit" class="subtask-update-button">Update</button>
            {{ form.title.errors }}
            {{ form.description.errors }}
            {{ form.category.errors }}
            {{ form.status.errors }}
            {{ form.updated_at.errors }}
        </form>
    </div>
...
```

Для того, чтобы при обновлении в форме уже были проставлены текущие значения,                                             
мы добавляем в наши `option` специальные атрибуты, которые называются                                                  
`value` и `selected`. В value мы прокидываем то значение, что на данный момент                                          
есть у записи. Так же, если речь идёт о полях `foreignkey`, то в этот атрибут                                            
мы прокидываем значение id первичного ключа. И как раз уже в поле selected                                              
добавляем само значение, какое там должно быть от этого ключа.                                                        

Так же обновим url путь для кнопки обновления:                                         

```html
...
        <div class="button-container">
            <a href="{% url 'router:tasks:update-subtask' subtask.id %}" class="update-button">Update</a>  <!-- NEW -->
            <a href="#" class="delete-button">Delete</a>
        </div>
...
```

И новый url:                                                                   

```python
urlpatterns = [
    ...
    path("subtasks/<int:subtask_id>/update/", update_subtask, name='update-subtask'),
    ...
]
```

Остались лишь стили:                                                                     

```css
.new-subtask-title, .update-subtask-title {
    text-align: center;
    color: rgba(46, 204, 153, 0.5);
    font-size: 24px;
    font-weight: bold;
    margin-top: 30px;
    margin-bottom: 20px;
}

.subtask-container-form, .new-subtask-container {
    border: 1px solid rgba(46, 204, 153, 0.5);
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(46, 204, 153, 0.8);
    background-color: inherit;
    width: 600px;
    margin: 50px auto;
}

.subtask-form-label {
    color: rgba(46, 204, 153, 0.4);
    font-weight: 600;
    font-size: 20px;
}

.subtask-form-control {
    background-color: transparent;
    border: 1px solid rgba(46, 204, 153, 0.5);
    color: #c0bfbf;
    padding: 8px;
    margin: 8px 0;
    display: inline-block;
    border-radius: 10px;
    box-sizing: border-box;
    width: 100%;
    box-shadow: 0 0 10px rgba(46, 204, 153, 0.6);
}

.subtask-form-control:hover,
.subtask-form-control:focus {
    border-color: rgba(46, 204, 153, 0.75);
    box-shadow: 0 0 10px rgba(46, 204, 153, 0.8);
    outline: none;
}

.subtask-create-button,
.subtask-update-button {
    background-color: rgba(46, 204, 153, 0.1);
    border: 1px solid rgba(46, 204, 153, 0.5);
    color: rgba(46, 204, 153, 0.5);
    font-weight: 500;
    font-size: 25px;
    transition: all 0.3s ease;
    margin: 0 auto;
    width: 100%;
    padding: 14px 20px;
    cursor: pointer;
    display: block;
    border-radius: 4px;
}

.subtask-create-button:hover,
.subtask-update-button:hover {
    background-color: rgba(46, 204, 153, 0.1);
    color: #c0bfbf;
    border-color: rgba(46, 204, 153, 0.75);
    box-shadow: 0 0 10px rgba(46, 204, 153, 0.8);
}

```

# **Create subtask**                                                                

Для подзадач осталось лишь последнее - возможность создания новой!                                                     

Начнём с формы, опять же:                                                          

```python
class SubTaskCreateForm(ModelForm):  # NEW
    class Meta:
        model = SubTask
        fields = [
            'title',
            'description',
            'category',
            'task',
            'status',
            'creator',
            'date_started',
            'deadline'
        ]


class SubTaskUpdateForm(ModelForm):
    ...
```

И сразу же начнём писать новую функцию на это дело:                                                            

```python
def create_subtask(request):
    task_id = request.GET.get("task_id")  # получаем ID определённой задачи через query params

    user = get_object_or_404(User, id=request.user.id)
    categories = Category.objects.all()
    statuses = Status.objects.all()
    task = get_object_or_404(Task, id=task_id)

    form = SubTaskCreateForm()

    if request.method == 'POST':
        form = SubTaskCreateForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('router:tasks:all-subtasks')

    context = {
        "form": form,
        "user": user,
        "categories": categories,
        "task": task,
        "statuses": statuses
    }

    return render(
        request=request,
        template_name='todo/create_subtask.html',
        context=context
    )
```

Так же добавим новый шаблон:                                              

```html
{% block content %}
    <div class="new-subtask-title">
        Create New Sub Task
    </div>
    <div class="new-subtask-container">
        <form method="post">
            {% csrf_token %}

            <div class="subtask-subtask-mb-3">
                <label for="title" class="subtask-form-label">Title</label>
                <input type="text" class="subtask-form-control" id="title" name="title" maxlength="25">
            </div>

            <div class="subtask-mb-3">
                <label for="description" class="subtask-form-label">Description</label>
                <textarea class="subtask-form-control" id="description" name="description" 
                          maxlength="1500"></textarea>
            </div>

            <div class="subtask-mb-3">
                <label for="category" class="subtask-form-label">Category</label>
                <select class="subtask-form-control" id="category" name="category">
                    <option value="" selected="">---</option> <!-- For optional category -->
                    {% for category in categories %}
                        <option value="{{ category.id }}">{{ category.name }}</option>
                    {% endfor %}
                </select>
            </div>

            <div class="subtask-mb-3">
                <label for="task" class="subtask-form-label">Task</label>
                <select class="subtask-form-control" id="task" name="task">
                    <option value="{{ task.id }}">{{ task.title }}</option>
                </select>
            </div>

            <div class="subtask-mb-3">
                <label for="status" class="subtask-form-label">Status</label>
                <select class="subtask-form-control" id="status" name="status">
                    <option value="" selected="">---</option>
                    {% for status in statuses %}
                        <option value="{{ status.id }}">{{ status.name }}</option>
                    {% endfor %}
                </select>
            </div>

            <div class="subtask-mb-3">
                <label for="creator" class="subtask-form-label">Creator</label>
                <select class="subtask-form-control" id="creator" name="creator">
                    <option value="{{ user.id }}">{{ user.username }}</option>
                </select>
            </div>

            <div class="subtask-mb-3">
                <label for="date_started" class="subtask-form-label">Date Started</label>
                <input type="date" class="subtask-form-control" id="date_started" name="date_started">
            </div>

            <div class="subtask-mb-3">
                <label for="deadline" class="subtask-form-label">Deadline</label>
                <input type="date" class="subtask-form-control" id="deadline" name="deadline">
            </div>

            <button type="submit" class="subtask-create-button">Create</button>
        </form>
    </div>
{% endblock %}
```

И так же не забываем про кнопку создания подзадачи в разделе информации                                                
о конкретной задаче:                                                    

```html
    ...
            <div class="button-container">
                <a href="{% url 'router:tasks:update-task' task.id %}" class="update-button">Update</a>
                <a href="{% url 'router:tasks:delete-task' task.id %}" class="delete-button">Delete</a>
                <a href="{% url 'router:tasks:create-subtask' %}?task_id={{ task.id }}" class="create-subtask">Create subtask</a> <!-- NEW -->
            </div>
    ...
```
Здесь мы будем пользоваться query params, передавая ID определённой задачи                                              
для которой подзадача и будет создаваться.                                                  

Не хватает только url:                                                         

```python
...
urlpatterns = [
    ...
    path("subtasks/create/", create_subtask, name='create-subtask'),  # NEW
    ...
]
```

# **Delete subtask**

Осталось добавить возможность удалять задачу:                                                    

Для удаления будет вполне достаточно лишь самой функции и добавления пути                                               
для кнопок:                                                            

```python
def delete_subtask(request, subtask_id):
    subtask = get_object_or_404(SubTask, id=subtask_id)

    subtask.delete()
    return redirect('router:tasks:all-subtasks')
```

```python
urlpatterns = [
    ...
    path("subtasks/<int:subtask_id>/delete/", delete_subtask, name='delete-subtask'),
    ...
]

```
`subtask_info.html`
```html
...
        <div class="button-container">
            <a href="{% url 'router:tasks:update-subtask' subtask.id %}" class="update-button">Update</a>
            <a href="{% url 'router:tasks:delete-subtask' subtask.id %}" class="delete-button">Delete</a> <!-- NEW -->
        </div>
...
```

`task_info.html`
```html
...
                        <h3>{{ subtask.status }}</h3>
                        <div class="button-container">
                            <a href="{% url 'router:tasks:update-subtask' subtask.id %}"
                               class="update-button">Update</a>
                            <a href="{% url 'router:tasks:delete-subtask' subtask.id %}"
                               class="delete-button">Delete</a>  <!-- NEW -->
                        </div>
...
```
---

# **New app, create login functionality**

Мы достаточно успешно создали небольшой функционал для работы с задачами                                               
и подзадачами. Но всё это было в рамках одного пользователя - суперадмина,                                               
вход в систему для которого был в основном через админ-панель, что так себе.                                            
Давайте добавим возможность создавать новых пользователей именно на сайте,                                              
у каждого будет свой профиль, свои задачи и подзадачи.                                               

Сперва создадим приложение:                                                 

`python manage.py startapp user`

Тут нужно будет сразу обновить строчку в `apps.py`:                                         

```python
class UserConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.user"  # NEW
```

Это из-за того, что все приложения у нас лежат не в корне, а в модуле `apps`.                                            

После этого это приложение нужно в проекте зарегистрировать в настройках проекта:                                         

```python
    ...
    ...
    # local
    "apps.todo.apps.TodoConfig",
    "apps.user.apps.UserConfig",  # NEW

...
```

Так же обновим роутер, добавив в него путь к урлам для пользователя:                                                 

```python
urlpatterns = [
    path("", home_page, name='home'),
    path("tasks/", include('apps.todo.urls')),
    path("user/", include('apps.user.urls'))  # NEW
]
```

Итак, начнём с форм. Мы будем работать с дефолтным пользователем от Django.                                             
Для того, чтобы написать форму нам понадобится класс из "коробки" самого                                             
Джанго. Он называется `AuthenticationForm`. В нём уже есть весь необходимый                                             
нам функционал:                                                

```python
from django.contrib.auth.forms import (
    AuthenticationForm,
)
from django import forms
from django.forms.widgets import TextInput, PasswordInput


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
```

После определения формы можем написать и функцию:                                             
```python
from django.shortcuts import (
    render,
    redirect,
)
from django.contrib.auth import authenticate
from django.contrib.auth.models import auth

from apps.user.forms import LoginForm


def us_login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)

                return redirect('router:tasks:all-tasks')

    context = {
        "form": form
    }

    return render(
        request=request,
        template_name='user/login.html',
        context=context
    )
```

Если при ПОСТ запросе данные валидны - мы вытягиваем их методом `get()` из                                             
объекта нашего `POST` запроса. В нашем случае нас интересуют именно логин                                                
и пароль. После этого нам нужно создать объект пользователя нашего, это                                             
мы сделаем благодаря методу `authenticate()`. Он достаточно прост:                                                    
мы передаём в него объект запроса нашего и креды для входа (логин и                                                     
пароль). Если креды верны - этот метод возвращает объект пользователя                                           
по этим кредам. Дальше мы как раз проверяем, что если у нас юзер получен -                                           
мы запускаем метод `login()` из нашего файла `django.contrib.auth`.                                                     
Он выполняет процесс аутентификации пользователя, фактически "входя" в систему.                                                     

Этот метод принимает два аргумента:                                                     
* **объект request**, который представляет текущий **HTTP-запрос**                                                     
* **объект user**, который является экземпляром пользователя, прошедшего                                                    
аутентификацию.                                                    

Когда мы вызываем `login(request, user)`, `Django` устанавливает для данного                                                     
пользователя сессию, что позволяет пользователю **оставаться аутентифицированным**                                                     
в течение **всей сессии браузера**. Это означает, что после успешного вызова                                                    
этого метода система будет распознавать пользователя при последующих                                                     
запросах до тех пор, пока сессия не закончится или пользователь явно                                                     
не выйдет из системы.                                                    


Дальше создадим с вами шаблон:                                               

```html
{% extends 'main.html' %}

{% block title %}
    Login
{% endblock %}

{% block content %}
    <div class="login-container">
        <form method="post" class="log-in-form">
            {% csrf_token %}

            <div class="mb-3">
                <label for="email" class="login-form-label">Email</label>
                {{ form.username }}
            </div>

            <div class="mb-3">
                <label for="password1" class="login-form-label">Password</label>
                {{ form.password }}
            </div>

            <button type="submit" class="login-button">Login</button>
            <div class="login-account-choice">
                <p>You don't have an account?</p>
                <a href="#">Register</a>
            </div>
        </form>
    </div>
{% endblock %}
```

И стили css:                                                         

```css
.registration-container, .login-container {
    border: 1px solid rgba(46, 204, 113, 0.5);
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(46, 204, 113, 0.8);
    background-color: inherit;
    width: 600px;
    margin: 50px auto;
}

.register-form .mb-3, .log-in-form .mb-3 {
    margin-bottom: 1rem;
}

.registration-form-label, .login-form-label {
    display: block;
    color: rgba(46, 204, 113, 0.4);
    font-weight: 600;
    font-size: 20px;
    margin-bottom: .5rem;
}

.register-form input, .log-in-form input,
.register-form textarea, .log-in-form textarea,
.register-form select, .log-in-form select {
    width: 100%;
    padding: 8px;
    margin-bottom: 8px;
    border-radius: 10px;
    border: 1px solid rgba(46, 204, 113, 0.5);
    box-shadow: 0 0 10px rgba(46, 204, 113, 0.6);
    background-color: transparent;
    color: #c0bfbf;
}

.register-form input::placeholder, .log-in-form input::placeholder {
    color: rgba(46, 204, 113, 0.5);
}

.register-form input:hover, .log-in-form input:hover,
.register-form input:focus, .log-in-form input:focus,
.register-form select:hover, .log-in-form select:hover,
.register-form select:focus, .log-in-form select:focus {
    border-color: rgba(46, 204, 113, 0.75);
    outline: none;
    box-shadow: 0 0 10px rgba(46, 204, 113, 0.8);
}

.register-button, .login-button {
    width: 100%;
    padding: 14px 20px;
    border-radius: 4px;
    border: 1px solid rgba(46, 204, 113, 0.5);
    background-color: transparent;
    color: rgba(46, 204, 113, 0.5);
    font-weight: 500;
    font-size: 25px;
    transition: all 0.3s ease;
    display: block;
    margin-top: 20px;
    cursor: pointer;
}

.register-button:hover, .login-button:hover {
    background-color: rgba(46, 204, 113, 0.1);
    color: #c0bfbf;
    border-color: rgba(46, 204, 113, 0.75);
    box-shadow: 0 0 10px rgba(46, 204, 113, 0.8);
}

.register-account-choice, .login-account-choice {
    text-align: center;
    margin-top: 15px;
}

.register-account-choice a, .login-account-choice a {
    color: rgba(46, 204, 113, 0.5);
    text-decoration: none;
    font-weight: 500;
}

.register-account-choice a:hover, .login-account-choice a:hover {
    text-decoration: underline;
    color: rgba(46, 204, 113, 0.75);
}

```

И не забываем подключить их к нашему главному файлу html:                                                 
```html
...
<link rel="stylesheet" href="{% static 'user/css/login.css' %}">
...
```

Последнее, что нам осталось для этой логики - добавить во всех предыдущих                                               
функциях спец декоратор, чтобы наши функции были доступны только                                                  
авторизированным пользователям:                                            

```python
@login_required(login_url='router:user:login')
```
Благодаря этому декоратору весь наш функционал будет заблокирован для анонимных                                        
пользователей и будет автоматически перенаправлять их на страницу входа в систему.                                           


# **Registration**                                                          

Добавим теперь возможность регистрации, то есть создания нового пользователя,                                            
чтобы, опять же, не заниматься этим через админ панель.                                                 

Сперва создадим форму регистрации. Для этого мы так же используем готовый                                                
функционал самого Django - `UserCreationForm` класс. С нашей же стороны мы                                          
в классе **Meta** укажем нужную нам модель и определённые поля, требующиеся                                              
при регистрации:                                                         

```python
class CreateUserForm(UserCreationForm):  # NEW
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2'
        ]


class LoginForm(AuthenticationForm):
    ...
```

И создадим функцию для работы регистрации:                                          

```python
def register(request):  # NEW
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("router:user:login")

    context = {
        "form": form
    }

    return render(
        request,
        'user/register.html',
        context=context
    )


def us_login(request):
    ...
```

Так же добавим шаблон:                                                

```html
{% block content %}
    <div class="registration-container">
        <form method="post" class="register-form">
            {% csrf_token %}

            <div class="mb-3">
                <label class="registration-form-label">Name</label>
                {{ form.first_name }}
                {{ form.first_name.errors }}
            </div>

            <div class="mb-3">
                <label class="registration-form-label">Surname</label>
                {{ form.last_name }}
                {{ form.last_name.errors }}
            </div>

            <div class="mb-3">
                <label for="username" class="registration-form-label">Username</label>
                {{ form.username }}
                {{ form.username.errors }}
            </div>

            <div class="mb-3">
                <label for="email" class="registration-form-label">Email</label>
                {{ form.email }}
                {{ form.email.errors }}
            </div>

            <div class="mb-3">
                <label for="password1" class="registration-form-label">Password</label>
                {{ form.password1 }}
                {{ form.password1.errors }}
            </div>

            <div class="mb-3">
                <label for="password2" class="registration-form-label">Repeat Password</label>
                {{ form.password2 }}
                {{ form.password2.errors }}
            </div>

            <button type="submit" class="register-button">Register</button>
            <div class="register-account-choice">
                <p>Already have an account??</p>
                <a href="{% url 'router:user:login' %}">Log-in</a>
            </div>
            {{ form.non_field_errors }}
        </form>
    </div>
{% endblock %}
```

Обновим ссылку на странице логинизации:                                                  

```html
...
            <div class="login-account-choice">
                <p>You don't have an account?</p>
                <a href="{% url 'router:user:register' %}">Register</a>  <!-- NEW -->
            </div>
...
```

И добавим роутинг:                                                                    

```python
urlpatterns = [
    path("register/", register, name='register'),  # NEW
    ...
]
```

# **Profile info**

Одно из последнего, что сделаем - добавим возможность посмотреть профиль.                                               

Тут форм не будет уже никаких, начнём с функции. Нам понадобится сам пользователь,                                        
и так же задачи и подзадачи, для отображения их количества:                                                              

```python
@login_required(login_url='router:user:login')
def us_info(request):
    user = get_object_or_404(User, id=request.user.id)
    tasks = Task.objects.filter(creator__task=request.user.id)
    subtasks = SubTask.objects.filter(creator__subtask=request.user.id)

    context = {
        "user": user,
        "tasks": tasks,
        "subtasks": subtasks
    }

    return render(
        request=request,
        template_name='user/profile.html',
        context=context
    )
```

Шаблон для отображения:                                                          

```html
...

{% block title %}
    {{ user.username }} Profile
{% endblock %}

{% block content %}
    <div class="profile-container">
        <div class="main-info">
            <div class="photo-block">
                <img src="https://imgs.search.brave.com/MWlI8P3aJROiUDO9A-LqFyca9kSRIxOtCg_Vf1xd9BA/rs:fit:860:0:0/g:ce/aHR0cHM6Ly90NC5m/dGNkbi5uZXQvanBn/LzAyLzE1Lzg0LzQz/LzM2MF9GXzIxNTg0/NDMyNV90dFg5WWlJ/SXllYVI3TmU2RWFM/TGpNQW15NEd2UEM2/OS5qcGc"
                     alt="#" class="prof-photo">
                <h3>{{ user.username }}</h3>
            </div>
            <div class="prof-buttons">
                <a href="#" class="log-out">Logout</a>
                <a href="#" class="edit-profile">Edit profile</a>
            </div>
        </div>
        <div class="tasks-info-block">
            <div class="header-task-block">
                <h4 class="header-task-counter">{{ tasks.count }}</h4>
                <p class="header-task-name">Tasks</p>
            </div>
            <div class="header-subtask-block">
                <h4 class="header-subtask-counter">{{ subtasks.count }}</h4>
                <p class="header-subtask-name">Subtasks</p>
            </div>
        </div>

        <div class="about-block">
            <h3>About</h3>
            <div class="user-info">
                {% if user.first_name and user.last_name %}
                    <h3><b>Name: </b><span>{{ user.first_name }}</span></h3>
                    <h3><b>Surname: </b><span>{{ user.last_name }}</span></h3>
                    <h3><b>Ssername: </b><span>{{ user.username }}</span></h3>
                    <h3><b>Email: </b><span>{{ user.email }}</span></h3>
                {% else %}
                    <h3><b>Username: </b><span>{{ user.username }}</span></h3>
                    <h3><b>Email: </b><span>{{ user.email }}</span></h3>
                {% endif %}

            </div>
        </div>

        <div class="tasks-block">
            <div class="recent-tasks">
                <h3>Recent Tasks</h3>
                <a href="{% url 'router:tasks:all-tasks' %}" class="all-tasks-link">Show all</a>
            </div>
            <div class="all-tasks">
                {% for task in tasks|slice:":4" %}
                    <a href="{% url 'router:tasks:task-info' task.id %}" class="user-task-link">
                        <div class="profile-task-block">
                            <h5 class="task-title">
                                {{ task.title|slice:":15" }}{% if task.title|length > 15 %}...{% endif %}
                            </h5>
                            <p class="task-status"><b>status: </b>
                                {{ task.status.name|slice:":6" }}{% if task.status.name|length > 6 %}...{% endif %}
                            </p>
                            <p class="task-category"><b>category: </b>
                                {{ task.category.name|slice:":6" }}{% if task.category.name|length > 6 %}...{% endif %}
                            </p>
                        </div>
                    </a>
                {% endfor %}
            </div>
        </div>
    </div>
{% endblock %}
```

новый url:                                                  

```python
...
...

urlpatterns = [
    ...
    ...
    path("info/", us_info, name='info'),  # NEW
]
```

И конечно же стили:                                                

```css
.profile-container {
    display: flex;
    flex-direction: column;
    margin: 4em auto 0;
    color: #e0e0e0;
    background-color: inherit;
    padding: 20px;
    border-radius: 8px;
    max-width: 900px;
    border: 1px solid rgba(22, 160, 133, 0.1);
    box-shadow: 0 0 10px rgba(22, 160, 133, 0.7);
    overflow-y: hidden;
    box-sizing: border-box;
}

.main-info {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
    border-bottom: 1px solid rgba(22, 160, 133);
    padding-bottom: 20px;
}

.main-info a {
    text-decoration: none;
    color: #16a085;
    transition: all 0.3s ease;
}

.photo-block {
    display: flex;
    justify-content: flex-start;
    align-items: center;
}

.edit-profile, .log-out {
    border: 2px solid #16a085;
    background-color: transparent;
    color: #16a085;
}

.edit-profile:hover, .log-out:hover {
    background-color: rgba(22, 160, 133, 0.1);
    color: #e0e0e0;
}


.prof-photo {
    border-radius: 50%;
    width: 100px;
    height: 100px;
    object-fit: cover;
    margin-right: 20px;
}

.photo-block h3 {
    margin: 0 auto;
    font-size: 36px;
}

.prof-buttons {
    display: flex;
    justify-content: space-around;
    width: 17em;
    text-decoration: none;
    color: #16a085;
    background-color: transparent;
    padding: 8px 16px;
    border-radius: 4px;
    margin-left: 8px;
    transition: all 0.3s ease;
}

.edit-profile, .log-out {
    margin-left: auto;
    padding: 10px 15px;
    text-decoration: none;
    border-radius: 4px;
    transition: all 0.3s ease;
}

.tasks-info-block {
    display: flex;
    justify-content: flex-end;
    background-color: rgba(22, 160, 133, 0.1);
    margin-top: 20px;
    margin-bottom: 20px;
    color: #c0bfbf;
    font-weight: 700;
    border-radius: 10px;
}

.header-task-block, .header-subtask-block {
    padding: 10px;
    border-radius: 8px;
    margin-right: 3em;
}

.header-task-counter, .header-subtask-counter {
    color: #c0bfbf;
    margin: 0 auto 5px;
    text-align: center;
}

.header-task-name, .header-subtask-name {
    margin: 0 auto;
    color: #c0bfbf;
}

.about-block {
    background-color: rgba(22, 160, 133, 0.1);
    padding: 20px;
    margin-top: 20px;
    border-radius: 16px;
    color: #c0bfbf;
    font-weight: 700;
}

.user-info h3 {
    margin-bottom: 10px;
}

.user-info h3 span {
    color: rgb(22, 160, 133);
}

.recent-tasks {
    display: flex;
    justify-content: space-between;
    margin-bottom: 1em;
    border-top: 1px solid rgb(22, 160, 133);
    padding-top: 20px;
    margin-top: 20px;
    font-weight: 700;
    color: #c0bfbf;
    align-items: center;
}

.all-tasks-link {
    color: #16a085;
    padding: 10px 15px;
    text-decoration: none;
    border-radius: 4px;
    display: inline-block;
    border: 2px solid #16a085;
    background-color: transparent;
    transition: all 0.3s ease;
}

.all-tasks-link:hover {
    background-color: rgba(22, 160, 133, 0.1);
    color: #e0e0e0;
}

.all-tasks {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    justify-content: center;
    background-color: rgba(22, 160, 133, 0.1);
    text-decoration: none;
    color: #16a085;
    border-radius: 10px;
    transition: all 0.3s ease;
    padding: 1em;
}

.user-task-link {
    display: flex;
    text-decoration: none;
    color: #c0bfbf;
    width: 190px;
}

.user-task-link:hover {
    background-color: rgba(22, 160, 133, 0.1);
    border-color: rgb(22, 160, 133);
}

.profile-task-block {
    width: 100%;
    height: 100%;
    box-sizing: border-box;
    background-color: rgba(68, 70, 68, .1);
    padding: 10px;
    border-radius: 8px;
    text-align: center;
    border: 1px solid rgb(22, 160, 133);
    box-shadow: 0 0 10px rgba(138, 242, 231, 0.5);
}
```

# **Logout**                                                   

Тут всё кратко и просто. Нужны будут функция, новый эндпоинт и обновить ссылки.                                             


```python
@login_required(login_url='router:user:login')
def us_logout(request):
    auth.logout(request=request)
    return redirect('router:user:login')
```

```python
urlpatterns = [
    path("register/", register, name='register'),
    path("login/", us_login, name='login'),
    path("info/", us_info, name='info'),
    path("logout/", us_logout, name='logout')  # NEW
]
```

```html
...
            <div class="prof-buttons">
                <a href="{% url 'router:user:logout' %}" class="log-out">Logout</a>  <!-- NEW -->
...
```
