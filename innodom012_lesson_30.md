<!-- TOC -->
* [**DRF class-views, serializers, swagger**](#drf-class-views-serializers-swagger)
* [**Serializers**](#serializers)
* [**LIST all of subtasks + POST new subtask**](#list-all-of-subtasks--post-new-subtask)
* [**GET a specific subtask + PUT OR DELETE it**](#get-a-specific-subtask--put-or-delete-it)
* [**DRF filtration**](#drf-filtration-)
* [**Swagger**](#swagger)
<!-- TOC -->

# **DRF class-views, serializers, swagger**


**Представление (`view`) в DRF** - это компонент, который обрабатывает                                                   
**HTTP-запросы** и возвращает **HTTP-ответы**. Представление определяет, как                                                                
данные будут представлены в нашем `API`.                                                   

При обработке **HTTP-запроса**, представление может выполнять                                                                
следующие задачи:                                                   

* **извлекает данные** из базы данных или других источников данных для                                                                   
дальнейшей обработки.                                                                    
* **проверяет и валидирует** полученные данные, чтобы убедиться, что они                                                                  
соответствуют ожидаемому формату и типу.                                                                 
* **преобразует извлеченные** и валидированные данные в формат, который                                                              
будет возвращен клиенту (например, `JSON`, `XML` и т.д.). **Сериализация**                                                               
осуществляется с помощью сериализаторов `DRF`.                                                                
* **обрабатывает различные** типы `HTTP-запросов`, такие как `GET`, `POST`,                                                                
`PUT`, `DELETE` и т.д., и выполняет соответствующие действия в                                                              
зависимости от типа запроса.                                                               
* **после обработки данных**, формирует `HTTP-ответ`, который содержит                                                                  
данные, ошибки (если есть), статус код и другую информацию                                                                  


**Django** предоставляет различные виды представлений:                                                                                                     

1) **Функциональные представления**                                                   

2)  **Представления основанные на классах**:                                                   
    * **APIView** - базовый класс представления, который предоставляет обработку                                                   
    **HTTP-методов** (`GET`, `POST`, `PUT`, `DELETE`) через методы                                                               
    (`get()`, `post()`, `put()`, `delete()` и тд).                                                    

    * **GenericAPIView** - базовый класс представления, который предоставляет                                                   
    общие методы для работы с моделями и сериализаторами. Он часто                                                   
    используется с миксинами (`mixins`) для обработки различных типов запросов                                                   

    * **ViewSet** - это класс, который предоставляет более простой и декларативный                                                   
    способ определения представлений для работы с моделями. **ViewSet**                                                   
    объединяет логику для обработки различных **HTTP-методов** в одном классе,                                                   
    таком как `list()`, `create()`, `retrieve()`, `update()`, `destroy()`, и т.д.                                                   


**Функциональные представления**                                                   

**Функциональные представления** - это один из способов определения                                                               
представлений в **Django REST Framework (DRF)**. Вместо использования                                                                                                                  
классов для определения представлений, функциональные представления                                                                
представляют собой обычные функции `Python`, которые обрабатывают                                                              
**HTTP-запросы** и возвращают **HTTP-ответы**, то есть принимают                                                                                                          
`Request` и возвращают `Response`.                                                                                                            


**APIView** - это базовый класс представления в **DRF**, который предоставляет                                                              
более гибкий и детализированный подход к обработке запросов, чем функциональные                                                               
представления. Он позволяет явно определять методы для каждого типа                                                               
**HTTPзапроса** (`GET`, `POST`, `PUT`, `DELETE` и т.д.) и более гибко управлять                                                                    
логикой обработки запросов                                                    


**GenericAPIView** - это базовый класс представления в **DRF**, который                                                                 
предоставляет общий функционал для обработки различных типов                                                                   
запросов (`GET`, `POST`, `PUT`, `DELETE`) и операций с данными. Он                                                                 
предназначен для работы с одним объектом или списком объектов и                                                                  
является более гибким и кастомизируемым, чем `ModelViewSet`, но требует                                                                    
более явного определения логики для каждого метода запроса.                                                                   


В DRF **ViewSet** представляет собой класс, который предоставляет                                                                   
удобный и декларативный способ определения представлений (views) для                                                                  
работы с моделями или другими данными вашего приложения. ViewSet                                                                  
сочетает в себе различные методы для обработки различных типов                                                                 
запросов и операций над данными.                                                                

---

Продолжим с того, на чём остановились на прошлом занятии.                                                                                                             

# **Serializers**                                                   


**Сериализаторы** помогают нам с вами указывать нашему `DRF` какие именно                                                                                                     
поля должны быть включены в процесс **сериализации**, или же                                                                                                               
**десереализации**. Далеко не редкость, когда необходимо подготавливать                                                                                                       
`JSON-ответы` для фронта в струкруре вложенной.                                                                                                                           

В нашем случае, допустим, при переходе по определённой задаче мы хотим                                                                                                      
так же отображать и список всех подзадач, если он есть.                                                                                                                    
Это, как мы смотрели на прошлом занятии, вполне реально. Нужно добавить                                                                                                      
новое поле в классе-сериализаторе, значением которого будет другой                                                                                                            
сериализатор, отвечающий за те самые вложенные данные.                                                                                                                      

Но как писать код, если мы хотим, чтобы какие-то поля отображались не просто                                                                                                    
ID от первичного\вторичного ключа, а именно прям вот данные?                                                                                                               

ДЛя таких хотелок нам с вами нужно использовать `serializers.StringRelatedField`                                                                                              
класс, который поможет нам как раз преображать `related` поля вторичных ключей                                                                                                         
в нормальные, читабельные данные для нашего клиента:                                                   

```python
class SubTaskPreviewSerializer(serializers.ModelSerializer):
    status = serializers.StringRelatedField()  # NEW

    class Meta:
        model = SubTask
        fields = ['id', 'title', 'status']


class TaskInfoSerializer(serializers.ModelSerializer):
    subtasks = SubTaskPreviewSerializer(many=True, read_only=True)

    category = serializers.StringRelatedField()  # NEW
    status = serializers.StringRelatedField()  # NEW

    ...
    ...
```


Этот класс `StringRelatedField` берёт в возвращаемое значение то, что                                                                                                    
в главной, родительской модели, закреплено в репрезентации в магическом                                                                                                    
методе `__str__(self)`. Если вы прописали там отображение `name` - в                                                                                                          
вложенной структуре категорий, статусов и прочего будет отображаться,                                                                                                                  
собственно, вместо `ID` именно имя статуса\категории                                                   

Если мы прокинем в метод `__str__(self)` отображение:                                                                                                            

```python
class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return f"MY AWESOME {self.name}!"  # NEW
```

То в таком случае при построении нашего `JSON` ответа с данными в поле                                                                                                        
категории будет отображаться именно такой формат.                                                                                                              

Но при этом следует помнить, что это поле - исключительно для чтения.                                                                                                       
ПОля, которые вы переопределили с использованием `serializers.StringRelatedField()`                                                                                          
будут исключены из форм на создание, или обновление записей.                                                                                                             


# **LIST all of subtasks + POST new subtask**                                                   

Дальше добавим с вам в целом возможность отображать список всех подзадач                                                                                                    
и допом возможность создавать новую подзадачу:                                                                                                                             

```python
class AllSubTasksGenericView(ListCreateAPIView):
    serializer_class = SubTaskSerializer

    def create_subtask(self, data):
        serializer = self.serializer_class(data=data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return serializer.data

    def get_queryset(self):
        subtasks = SubTask.objects.filter(
            creator=self.request.user.id
        )

        return subtasks

    def get(self, request: Request, *args, **kwargs):
        subtasks = self.get_queryset()

        if not subtasks:
            return Response(
                status=status.HTTP_204_NO_CONTENT,
                data=[]
            )

        serializer = self.serializer_class(subtasks, many=True)

        return Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )

    def post(self, request: Request, *args, **kwargs):
        new_subtask = self.create_subtask(data=request.data)

        return Response(
            status=status.HTTP_201_CREATED,
            data=new_subtask
        )
```

И добавим сюды сериализатор для всего этого дела:                                                                                                                          

```python
class SubTaskSerializer(serializers.ModelSerializer):
    status = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Status.objects.all()
    )
    category = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Category.objects.all()
    )
    creator = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all()
    )
    task = serializers.PrimaryKeyRelatedField(
        queryset=Task.objects.all()
    )

    class Meta:
        model = SubTask
        fields = [
            'id',
            'title',
            'description',
            'category',
            'task',
            'status',
            'creator',
            'date_started',
            'deadline',
            'created_at'
        ]
```

Здесь мы переопределяем поля статуса и категории таким образом,                                                                                                           
чтобы мы получали в JSON формате не просто ID, а читабельные данные,                                                                                                         
при этом сохраняя возможность обновления этих полей, а не использование                                                                                                       
их только в режиме чтения, что делает класс `StringRelatedField`.                                                                                                          

Атрибут `slug_field` в `SlugRelatedField` используется для определения                                                                                                           
поля модели, **значение которого будет использоваться для представления**                                                                                                           
**связи в сериализаторе**. Это **не обязательно** должно быть поле типа                                                                                                           
`SlugField` в нашей модели `Django`; это может быть любое поле,                                                                                                           
значение которого **уникально** идентифицирует объекты,                                                                                                           
такое как `CharField`.                                                                                                          

В контексте `SlugRelatedField`, `slug_field` указывает **DRF** использовать                                                                                                           
значение поля `name` модели `Status` или `Category` для сериализации и                                                                                                           
десериализации, вместо использования первичного ключа. Когда мы                                                                                                           
отправляем данные через `API`, мы будем использовать значение `name`                                                                                                           
для указания статуса или категории, и `DRF` будет искать                                                                                                          
соответствующий объект с таким `name` для связи.                                                                                                          

**Вот как это работает:**                                                   

* При **сериализации** (отправке данных клиенту): **DRF** будет отображать значение                                                                                                           
поля `name` в `JSON` вместо `ID`.                                                                                                          

* При **десериализации** (приеме данных от клиента): **DRF** ожидает, что в поле будет                                                                                                           
передано значение `name`, и использует это значение для поиска соответствующего                                                                                                           
объекта `Status` или `Category` в базе данных. Если объект найден, он будет                                                                                                          
связан с экземпляром `SubTask`.                                                                                                          

Если мы хотим, чтобы пользователи могли создавать и обновлять `SubTask` через                                                                                                           
`API`, используя имя статуса или категории, то `SlugRelatedField` с                                                                                                          
`slug_field='name'` - это правильный подход. Однако, если поля `name` в `Status`                                                                                                          
или `Category` **не уникальны**, это может привести к ошибкам, так как `DRF` не                                                                                                          
сможет точно определить, на какой объект ссылаться. В этом случае нам                                                                                                           
нужно будет гарантировать уникальность значений `name` в этих моделях.                                                                                                          


# **GET a specific subtask + PUT OR DELETE it**                                                   

Теперь же добавим возможность просматривать определённую подзадачу, а так же                                                                                                 
добавим туда возможность обновлять её, или же и вовсе удалять:                                                                                                              

```python
class SubTaskInfoGenericView(RetrieveUpdateDestroyAPIView):
    serializer_class = SubTaskSerializer

    def update_subtask_info(self, instance):
        serializer = self.serializer_class(
            instance,
            data=self.request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return serializer.data

    def get_object(self):
        subtask_id = self.kwargs.get('subtask_id')

        subtask = get_object_or_404(SubTask, id=subtask_id)

        return subtask

    def get(self, request: Request, *args, **kwargs):
        subtask = self.get_object()

        serializer = self.serializer_class(subtask)

        return Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )

    def put(self, request: Request, *args, **kwargs):
        subtask = self.get_object()

        data = self.update_subtask_info(instance=subtask)

        return Response(
            status=status.HTTP_200_OK,
            data={
                "message": SUBTASK_UPDATE_SUCCESS_MESSAGE,
                "data": data
            },
        )

    def delete(self, request: Request, *args, **kwargs):
        subtask = self.get_object()

        subtask.delete()

        return Response(
            status=status.HTTP_200_OK,
            data=SUBTASK_DELETE_SUCCESS_MESSAGE
        )
```

# **DRF filtration**                                                                                                             

Всё это весело задорно, но как делать фильтрацию? Что, если нам хочется                                                                                                       
ещё и фильтровать наши данные по разным параметрам?                                                                                                                       

Мы так же можем это сделать. Обычно фильтрация происходит посредством                                                                                                        
передачи `query_params` атрибутов, которые не являются обязательными,                                                                                                          
то есть можно обойтись и без них. Обычно они указываются после символа `?`                                                                                                  
после чего указывается имя специального фильтрационного параметра запроса,                                                                                                    
и ему присваевается какое-то значение:                                                                                                                                    

```127.0.0.1:8000/tasks/?status=NEW``` - допустим так вот. Получить                                                                                                     
список всех задач, у которых статус - **NEW**                                                                                                                   


```python
class TaskFilterGenericView(RetrieveAPIView):
    serializer_class = TaskInfoSerializer

    def get_queryset(self):
        queryset = Task.objects.select_related(
            'category',
            'status'
        ).prefetch_related('subtasks')

        status = self.request.query_params.get('status')
        category = self.request.query_params.get('category')
        date_from = self.request.query_params.get('date_from')
        date_to = self.request.query_params.get('date_to')
        deadline = self.request.query_params.get('deadline')

        if status:
            queryset = queryset.filter(status__name=status)

        if category:
            queryset = queryset.filter(category__name=category)

        if date_from and date_to:
            queryset = queryset.filter(date_started__range=[date_from, date_to])

        if deadline:
            queryset = queryset.filter(deadline=deadline)

        return queryset

    def get(self, request: Request, *args, **kwargs):
        filtered_data = self.get_queryset()

        if filtered_data.exists():

            serializer = self.serializer_class(filtered_data, many=True)

            return Response(
                status=status.HTTP_200_OK,
                data=serializer.data
            )
        return Response(
            status=status.HTTP_404_NOT_FOUND,
            data=[]
        )

```

Тут логика следующая: Мы формируем первычный **queryset** и дальше,                                                                                                             
в зависимости от переданных фильтрационных параметров запроса,                                                                                                            
мы фильтруем наши задачи исходя из настроек. При этом, если не было                                                                                                          
передано ни единого фильтра - возвращаем просто первычный **queryset**,                                                                                                       
который получили изначально.                                                                                                           

Дальше, в самом методе `get()`, мы получаем все эти данные и проверяем:                                                                                                      
если наш **queryset** не пустой - пихаем его в сериализатор, не зыбывая                                                                                                    
указать ему флаг `many=True` для отображения списка всех задач. Если же                                                                                                          
ни одной задачи не будет - будем отображать пустой спикок.                                                                                                                  


Возможно в самом запросе вас напугали такие страшные методы, как `select_related`                                                                                                   
и `prefetch_related`. Это нормально, давайте разбираться:                                                                                                                   


`select_related` используется для уменьшения количества запросов к базе                                                                                                                    
данных путем "**соединения**" (`JOIN`) связанных объектов в одном **SQL-запросе**.                                                                                                                   
Это хорошо подходит для обращений к "**одиночным**" связям, таким как                                                                                                                    
`ForeignKey` или `OneToOneField`. Например, у нас есть модель `Task`                                                                                                                    
с `ForeignKey` на `Status`, использование `select_related` позволит избежать                                                                                                                    
дополнительного запроса к базе данных для получения связанного                                                                                                                   
`Status` для каждой `Task`.                                                                                                                   

`prefetch_related`, с другой стороны, используется для запроса                                                                                                                                                                       
"**множественных**" связей, таких как связи через `ManyToManyField` или                                                                                                                   
обратные связи от `ForeignKey`. Вместо выполнения отдельного запроса                                                                                                                   
для каждого объекта, `prefetch_related` выполнит отдельный запрос для                                                                                                                   
получения всех связанных объектов, а затем "**вручную**" свяжет их с                                                                                                                    
основными объектами, с которыми они ассоциированы. Это эффективно                                                                                                                    
для уменьшения количества запросов к базе данных при работе с                                                                                                                   
большим числом связанных объектов.                                                                                                                   

Использование `select_related` и `prefetch_related` может значительно                                                                                                                    
увеличить производительность вашего API за счет снижения количества                                                                                                                   
запросов к базе данных, но следует учитывать, что они могут привести                                                                                                                   
к большим объемам передаваемых данных, если связанные объекты                                                                                                                   
сами по себе велики или их много.                                                                                                                   


---

# **Swagger**

Штош, как труъ разрабы, давайте составим ещё и техническую                                                            
документацию к нашей `API`! Это, на самом деле, штука важная,                                                         
ведь эта тех дока для АПИ будет улетать нашим коллегам-фронтам                                                          
и именно по этой доке они и будут составлять работу у себя на стороне.                                                  


Такая тех дока называется `Swagger`. Для того, чтобы её вкинуть в проект                                                      
необходимо установить доп библиатеку:                                                                   

`pip install drf-yasg`

`drf-yasg` автоматически генерирует документацию из наших **представлений**                                                                    
и **сериализаторов**. Нужно убедиться, что наши `viewsets` и `views` правильно                                                                    
аннотированы и имеют соответствующие `docstrings`, чтобы улучшить                                                                    
сгенерированную документацию.

И, конечно же, добавить её в `INSTALLED_APPS`:                                                      

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'drf_yasg',  # NEW
    ...
]

```

И после этого нужно будет добавить небольшой доп код для генерации                                                         
нешего сваггера. Этот код можем впилить прямо в урлы главные:                                                       


```python
from django.urls import path, include, re_path  # NEW
from rest_framework.permissions import AllowAny  # NEW

from drf_yasg import openapi  # NEW
from drf_yasg.views import get_schema_view  # NEW


schema_view = get_schema_view(  # NEW
    openapi.Info(  # NEW
        title="API Documentation",  # NEW
        default_version='v1',  # NEW
        description="TO DO APPLICATION API documentation",  # NEW
        terms_of_service="https://www.google.com/policies/terms/",  # NEW
        contact=openapi.Contact(email="contact@yourapp.local"),  # NEW
        license=openapi.License(name="BSD License"),  # NEW
    ),
    public=True,  # NEW
    permission_classes=([AllowAny]),  # NEW
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('apps.router')),
    re_path(  # NEW
        r'^swagger(?P<format>\.json|\.yaml)$',  # NEW
        schema_view.without_ui(cache_timeout=0),  # NEW
        name='schema-json'  # NEW
    ),
    re_path(  # NEW
        r'^swagger/$',  # NEW
        schema_view.with_ui('swagger', cache_timeout=0),  # NEW
        name='schema-swagger-ui'  # NEW
    ),
    re_path(
        r'^redoc/$',  # NEW
        schema_view.with_ui('redoc', cache_timeout=0),  # NEW
        name='schema-redoc'  # NEW
    ),
]
```

**Этот код создает три маршрута**: один для **JSON-спецификации** (`/swagger.json`),                                                       
один для **YAML-спецификации** (`/swagger.yaml`), и два для визуализаций с                                                       
помощью **Swagger UI** (`/swagger/`) и **ReDoc** (`/redoc/`).                                                       
