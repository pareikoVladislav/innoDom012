<!-- TOC -->
* [**Permissions, Custom JWT, Testing**](#permissions-custom-jwt-testing)
* [**Default DRF permissions**](#default-drf-permissions-)
* [**List Users, Retrieve User**](#list-users-retrieve-user-)
* [**Testing**](#testing)
<!-- TOC -->

# **Permissions, Custom JWT, Testing**

На прошлом занятии мы с вам благополучно подключили наши                                                               
дефолтные эндпоинты для аутентификации по JWT-токенам.                                                                  
Теперь же, для того, чтобы всё это дело начало играть новыми                                             
красками, нам необходимо с вами доабвить новый статический                                                            
атрибут-настройку в наши классы-отображения: `permission_classes`,                                                
в этом поле мы обычно можем прокидывать различные разрешения.                                                               

`permission_classes` — это механизм в **Django REST framework**, который                                       
используется для определения прав доступа к различныым API-эндпоинтам. Он                                       
помогает контролировать, кто может выполнять определенные действия                                           
(например, чтение, редактирование, удаление) с ресурсами **API**.                                        

Список позволяет указать несколько классов разрешений. Это дает гибкость в                                          
определении прав доступа, позволяя **комбинировать** разные уровни доступа в                                            
зависимости от требований нашего приложения приложения, ну или же хотелок.                                                     

Все классы в списке `permission_classes` проверяются **последовательно**. Чтобы                                         
запрос был одобрен, он должен удовлетворять условиям **всех классов разрешений**                                        
в списке. **Если** какой-либо из классов возвращает **отказ**, запрос будет **отклонен**,                                        
даже если другие классы разрешают его.                                        


# **Default DRF permissions**                                           

существует несколько встроенных классов разрешений (`permissions`), которые                                       
предоставляют базовый набор правил для управления доступом                                               

* **AllowAny**                                               
Это разрешение предоставляет неограниченный доступ к **API**. Любой пользователь,                                                
вне зависимости от аутентификации, может выполнять любые запросы.                                               


* **IsAuthenticated**                                               
**Только аутентифицированные** пользователи имеют доступ к API. Если пользователь                                                
не аутентифицирован, **запрос будет отклонен**.                                               


* **IsAdminUser**                                               
Доступ к API разрешен **только администраторам**. Это означает, что пользователь                                                
должен быть аутентифицирован и иметь статус `is_staff` в модели пользователя.                                               


* **IsAuthenticatedOrReadOnly**                                               
Аутентифицированные пользователи имеют полный доступ к API. Неаутентифицированные                                               
пользователи могут **только читать** данные (`GET`, `HEAD`, `OPTIONS`).                                               


* **DjangoModelPermissions**
Этот класс разрешений связан с системой разрешений моделей **Django**. Он проверяет,                                               
имеет ли пользователь необходимые разрешения для модели (например, `add`,                                                
`change`, `delete`, `view`) для выполнения соответствующих **CRUD-операций**.                                               


* **DjangoModelPermissionsOrAnonReadOnly**                                               
Похож на `DjangoModelPermissions`, но неаутентифицированные пользователи                                                
могут выполнять только операции чтения.                                               


* **DjangoObjectPermissions**                                               
Это разрешение основано на объектно-ориентированных разрешениях моделей Django.                                               
Оно проверяет, имеет ли пользователь разрешения на конкретный объект                                               
(например, конкретный экземпляр модели).                                               


* **Custom Permissions**                                               
Вы также можете создать свои собственные классы разрешений, наследуя их от                                                
`BasePermission` и переопределяя метод `has_permission` и/или                                                
`has_object_permission`. Это позволяет вам точно настроить логику доступа                                                
в соответствии с потребностями вашего приложения.                                               


На данный момент нас интересует разрещение типа `IsAuthenticated`. Оно                                           
как раз и отвечает за предоставление доступа контента только тем                                       
пользователям, которые авторизированы в системе.                                               

Для всего этого нам необходимо добавить с вами следующую строку:                                   

```python
permission_classes = [IsAuthenticated]
```

Эту строчку нам нужно будет добавить везде, где мы хотим, чтобы доступ был                                            
только для авторизованных пользователей. При попытке проброса запроса                                   
анонимным пользователем он увидит что-то в этом духе:                                          

```json
{
    "detail": "Authentication credentials were not provided."
}
```

В случае же, если всё прошло оке - клиенту просто отобразятся данные,                                         
которые он запросил.                                        

Это что касалось дефолтной работы. Но иногда нужно кастомизировать                                               
создание токена. Условно, просто хочется\нужно передавать больше                                            
информации о пользователе в этом самом токене. Хочется отображение                                               
его изменить при проходе запроса, или же сообщения об ошибках                                             
кастомизировать. В общем стандартная тема. Как же мы можем это сделать?                                           

В идеале это будет отдельное приложение, в котором будут как раз отдельно                                        
настройки для `JWT`. Там с большего нужно всего пара моментов: кастомизировать                                           
сериализатор и класс-отображение:                                            

```python
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer,
    AuthUser
)
from rest_framework_simplejwt.tokens import Token


class CustomTokenObtainSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user: AuthUser) -> Token:
        token = super().get_token(user)

        token['email'] = user.email
        token['first_name'] = user.first_name

        return token

```

Тут мы в целом пользоуемся кастомной функциональностью для создания самого                                             
токена, но перед тем, как его вернуть, мы прокидываем в него доп информацию.                                             
В нашем случае это доп инфа о пользователе.                                              


Дальше нужно в наших настройках `JWT` обновить старый сериализатор на наш:                                              

```python
SIMPLE_JWT = {
    ...
    ...
    ...
    ...
    "TOKEN_OBTAIN_SERIALIZER": "apps.custom_jwt.serializers.CustomTokenObtainSerializer",
    ...
    ...
}
```

И, если необходимо, так же можем переписать класс-отображение на свой.                                                

```python
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.exceptions import (
    TokenError,
    InvalidToken
)
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.custom_jwt.serializers import CustomTokenObtainSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainSerializer

    def post(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.serializer_class(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as err:
            raise InvalidToken(err.args[0])

        return Response(
            status=status.HTTP_200_OK,
            data={
                "message": "Successful log-in",
                "refresh_token": serializer.validated_data.get("refresh"),
                "access_token": serializer.validated_data.get("access")
            }
        )

```

Тут опять же, особо ничего сложного, мега кастомного. Самый обычный `post`                                          
запрос мы переопределяем на своё кастомное отображение объекта `Response`


Не забудьте только потом в файле своём `urls.py` поменять класс на новый,                                   
созданный вами.                                      
---

# **List Users, Retrieve User**                                   

```python
class ListAllUsersGenericView(ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = UsersListSerializer

    def get_queryset(self):
        users = User.objects.all()

        return users

    def get(self, request: Request, *args, **kwargs):
        users = self.get_queryset()

        if not users:
            return Response(
                status=status.HTTP_204_NO_CONTENT,
                data=[]
            )

        serializer = self.serializer_class(users, many=True)

        return Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )


class UserDetailGenericView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserInfoSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user_id = self.kwargs.get('user_id')
        user = get_object_or_404(
            User,
            id=user_id
        )

        return user

    def get(self, request: Request, *args, **kwargs):
        user = self.get_object()

        serializer = self.serializer_class(instance=user)

        return Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )

    def put(self, request: Request, *args, **kwargs) -> Response:
        user = self.get_object()

        serializer = self.serializer_class(
            user,
            data=request.data,
            partial=True
        )

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response(
                status=status.HTTP_200_OK,
                data=serializer.data
            )
        return Response(
            status=status.HTTP_400_BAD_REQUEST,
            data=serializer.errors
        )

    def delete(self, request: Request, *args, **kwargs) -> Response:
        user = self.get_object()

        user.delete()

        return Response(
            status=status.HTTP_200_OK,
            data=[]
        )
```


```python
class UsersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'first_name',
            'last_name',
            'username',
            'phone',
            'date_joined'
        ]

```
---

# **Testing**

Тестирование - штука крайне важная и полезная, помогающая понять нам, на                                                 
сколько правильно работает наше приложение, которое мы пишем \ написали.                                                 

Вариаций тестирования много разных существует:                                                       

* **Юнит тесты**                                                            
Тестируют отдельные части кода (например, функции, методы, классы)                                                        
на корректность работы. Обычно быстрые и написаны разработчиками.                                                    

* **Интеграционные тесты**                                                   
Проверяют взаимодействие между различными компонентами системы (например,                                                   
взаимодействие между базой данных и приложением).                                                       
Полезны для проверки корректности работы всей системы в целом.

* **Нагрузочные тесты**                                                
Помогают посмотреть на сколько хорошо ваша система написана. Как она                                                      
справляется с высокими нагрузками по запросам (кол-во запросов + кол-во юзеров)                                                    

* **E2E тесты**                                                                  
Проверяют работу приложения в условиях, максимально приближенных к реальным.                                                  
Тестируют всю систему с начала до конца, имитируя действия реальных пользователей.                                        

Давайте напишем тест для последних наших классов для пользователя:                                              

Так как наш `ListAllUsersGenericView` взаимодействует с **базой данных** и                                                 
управляет **HTTP-ответами**, делает его подходящим кандидатом как для модульного                                                 
(`unit`), так и для **интеграционного тестирования**. Модульные тесты будут                                                 
проверять логику внутри методов класса в изоляции, в то время как                                                 
интеграционные тесты проверят, как этот класс взаимодействует с другими                                                
частями Django-приложения (например, с базой данных и маршрутизацией).                                                

Мы будем использовать `TestCase`.                                         

`TestCase` в Django – это специализированный класс, предназначенный для написания                                         
и выполнения тестов. Он является частью фреймворка для тестирования,                                          
предоставляемого **Django**, который наследуется от стандартного модуля                                         
`Python unittest.TestCase`.                                         

Он обеспечивает создание "чистой" тестовой среды перед выполнением каждого                                          
теста. Это означает, что для каждого теста (**метода в классе TestCase**) создаётся                                          
новая база данных, которая **НИКАК не зависит от реальной** базы данных приложения                                          
или результатов других тестов.                                         


Внутри тестов можно достаточно часто увидеть методы `setUp` и `tearDown`                                              

Методы `setUp` и `tearDown` используются для настройки начальных условий перед                                         
каждым тестом (`setUp`) и для очистки после его выполнения (`tearDown`). Мы пока что                                         
используем только `setUp` для создания пользователей и настройки                                          
тестового клиента **API**.                                         

Так как для каждого теста будет создаваться своя среда, благодаря методу ``setUp()`,                                         
тесты не влияют друг на друга. Это помогает в обеспечении точности                                         
и надёжности тестирования.                                         


Код тестировать мы будем благодаря такой сущности, как `Assert`.                                       
`Assert` – это ключевое слово или функция в программировании, используемая                                          
для проверки того, что определённое условие в коде является истинным.                                          
Если условие оказывается ложным, то обычно это приводит к прерыванию                                          
выполнения программы или генерации исключения, что помогает разработчикам                                          
быстро обнаруживать ошибки и проблемы в логике кода.                                         

В модуле `unittest`, который используется в **Django** для написания тестов, есть                                          
множество различных методов `assert`, каждый из которых предназначен для проверки                                          
определённых условий в коде. Вот некоторые из наиболее часто используемых видов `assert`:                                       

* `assertEquals (assertEqual) / assertNotEqual`:                                         
Проверяет, равны ли два значения. `assertNotEqual` делает                                          
противоположное — проверяет, что значения не равны.                                         


* `assertTrue / assertFalse`:                                         
`assertTrue` проверяет, что значение является `True`. `assertFalse` проверяет,                                          
что значение является `False`.                                         


* `assertIsNone / assertIsNotNone`:                                         
Проверяет, является ли значение `None` (`assertIsNone`) или не                                          
является `None` (`assertIsNotNone`).                                         


* `assertIn / assertNotIn`:                                         
`assertIn` проверяет, содержится ли элемент в контейнере (например, списке,                                         
кортеже, множестве). `assertNotIn` проверяет обратное.                                         


* `assertIsInstance / assertNotIsInstance`:                                         
Проверяет, является ли объект экземпляром определённого класса                                          
(`assertIsInstance`) или не является (`assertNotIsInstance`).                                         


* `assertRaises`:                                         
Используется в контекстном менеджере для проверки, что вызов функции                                          
генерирует определённое исключение.                                         


* `assertAlmostEqual / assertNotAlmostEqual`:                                         
Проверяет, что два числа почти равны (то есть равны с учетом                                          
плавающей точки). `assertNotAlmostEqual` проверяет обратное.                                         


* `assertGreater / assertLess / assertGreaterEqual / assertLessEqual`:                                         
Эти методы используются для сравнения чисел. Например, `assertGreater`                                         
проверяет, что одно число больше другого.                                         


* `assertCountEqual`:                                         
Проверяет, что два контейнера имеют одинаковые элементы,                                          
независимо от их порядка.                                         


* `assertDictEqual / assertListEqual / assertTupleEqual / assertSetEqual`:                                         
Сравнивают структуры данных (словари, списки, кортежи, множества)                                          
на равенство.                                         


```python
import re
from datetime import datetime

from django.test import TestCase
from apps.user.models import User
from rest_framework.test import APIClient
from rest_framework import status


class ListAllUsersGenericViewTest(TestCase):
    datetime_regex = re.compile(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d+Z')

    def setUp(self):
        # Создаем тестовых пользователей
        self.user = User.objects.create_user(
            email='test.email@mail.ru',
            first_name='test',
            last_name='user',
            username='testUser',
            password='password'
        )
        self.admin = User.objects.create_superuser(
            email='test.admin@mail.ru',
            first_name='admintest',
            last_name='testadmin',
            username='admin',
            password='admin',
            is_staff=True,
            is_superuser=True
        )

        self.client = APIClient()

    def test_get_users_as_admin(self):
        # Администратор получает список пользователей
        self.client.force_authenticate(user=self.admin)
        response = self.client.get('http://127.0.0.1:8000/api/v1/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), User.objects.count())
        self.assertIsInstance(response.data, list)

        for user in response.data:
            self.assertIsInstance(user['email'], str)
            self.assertIsInstance(user['first_name'], str)
            self.assertIsInstance(user['last_name'], str)
            self.assertIsInstance(user['username'], str)
            self.assertIsInstance(user['phone'], (str | None))
            self.assertIsInstance(user['is_staff'], bool)
            self.assertIsInstance(user['is_superuser'], bool)
            self.assertIsInstance(user['is_verified'], bool)
            self.assertIsInstance(user['is_active'], bool)
            self.assertTrue(self.datetime_regex.match(user['date_joined']), datetime)
            self.assertTrue(self.datetime_regex.match(user['last_login']), datetime)

    def test_get_users_as_non_admin(self):
        # Неадминистратор получает запрет доступа
        self.client.force_authenticate(user=self.user)
        response = self.client.get('http://127.0.0.1:8000/api/v1/users/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_no_users(self):
        # Проверка на отсутствие пользователей
        User.objects.all().delete()
        self.client.force_authenticate(user=self.admin)
        response = self.client.get('http://127.0.0.1:8000/api/v1/users/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

```

Таким же образом можем создать второй тест-блок для тестирования                                                 
класса-отображения для определённого пользователя:                                                

```python
class RetrieveUserGenericViewTest(TestCase):
    datetime_regex = re.compile(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d+Z')

    def setUp(self):
        self.user = User.objects.create_user(
            email='test.email@mail.ru',
            first_name='test',
            last_name='user',
            username='testUser',
            password='password'
        )

        self.admin = User.objects.create_superuser(
            email='test.admin@mail.ru',
            first_name='admintest',
            last_name='testadmin',
            username='admin',
            password='admin',
            is_staff=True,
            is_superuser=True
        )

        self.client = APIClient()

    def test_get_user_details(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.get(f'http://127.0.0.1:8000/api/v1/users/{self.user.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)
        self.assertIsInstance(response.data['email'], str)
        self.assertIsInstance(response.data['first_name'], str)
        self.assertIsInstance(response.data['last_name'], str)
        self.assertIsInstance(response.data['username'], str)
        self.assertIsInstance(response.data['phone'], (str | None))
        self.assertTrue(self.datetime_regex.match(response.data['date_joined']), datetime)

    def test_get_no_user(self):
        User.objects.all().delete()
        self.client.force_authenticate(user=self.admin)
        response = self.client.get(f'http://127.0.0.1:8000/api/v1/users/{self.user.id}')
        self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)

    def test_delete_user(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.delete(f'http://127.0.0.1:8000/api/v1/users/{self.user.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_user(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.put(
            f'http://127.0.0.1:8000/api/v1/users/{self.user.id}/',
            {'first_name': 'UpdatedName'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, 'UpdatedName')

```

Что же не счёт тестирования вложенных объектов?                                                

Чтобы протестировать вложенность в **API**, где задачи содержат подзадачи (**subtasks**),                                                 
мы должны сосредоточиться на проверке того, что данные о подзадачах корректно                                                 
возвращаются в ответе API. Наши тесты должны убедиться, что:                                                

1) Список подзадач включается в ответ API при запросе информации                                                 
о задаче.
2) Данные подзадач соответствуют ожидаемым, включая проверку всех                                                 
необходимых полей.
3) Структура ответа API соответствует ожидаемой (особенно важно для                                                 
вложенных данных).


```python
import datetime
import re

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from apps.category.models import Category
from apps.status.models import Status
from apps.subtask.models import SubTask
from apps.task.models import Task
from apps.user.models import User


class TaskDetailViewTest(TestCase):
    datetime_regex = re.compile(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d+Z')
    date_regex = re.compile(r'\d{4}-\d{2}-\d{2}')

    def setUp(self):
        self.user = User.objects.create_user(
            email='test.email@mail.ru',
            first_name='test',
            last_name='user',
            username='testUser',
            password='password'
        )
        self.admin = User.objects.create_superuser(
            email='test.admin@mail.ru',
            first_name='admintest',
            last_name='testadmin',
            username='admin',
            password='admin',
            is_staff=True,
            is_superuser=True
        )

        self.category = Category.objects.create(
            name='Test category'
        )

        self.status_new = Status.objects.create(
            name='NEW'
        )

        self.status_in_progress = Status.objects.create(
            name='IN PROGRESS'
        )

        self.task = Task.objects.create(
            title="Test title",
            description="Test description",
            creator=self.user,
            category=self.category,
            status=self.status_new,
            date_started=datetime.date.today(),
            deadline=datetime.date.today() + datetime.timedelta(days=4),
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now(),
            deleted_at=None
        )

        self.subtask1 = SubTask.objects.create(
            title='Test SubTask 1',
            description='Description for SubTask 1',
            category=self.category,
            task=self.task,
            status=self.status_in_progress,
            creator=self.user,
            date_started=datetime.date.today(),
            deadline=datetime.date.today() + datetime.timedelta(days=4),
        )

        self.subtask2 = SubTask.objects.create(
            title='Test SubTask 2',
            description='Description for SubTask 2',
            category=self.category,
            task=self.task,
            status=self.status_new,
            creator=self.user,
            date_started=datetime.date.today(),
            deadline=datetime.date.today() + datetime.timedelta(days=4),
        )

        self.client = APIClient()

    def test_get_task_details_with_subtasks(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.get(f'http://127.0.0.1:8000/api/v1/tasks/1/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertIsInstance(response.data['title'], str)
        self.assertIsInstance(response.data['description'], str)
        self.assertIsInstance(response.data['category'], str)
        self.assertIsInstance(response.data['status'], str)
        self.assertTrue(
            self.date_regex.match(response.data['date_started']),
            datetime
        )
        self.assertTrue(
            self.date_regex.match(response.data['deadline']),
            datetime
        )
        self.assertTrue(
            self.datetime_regex.match(response.data['created_at']),
            datetime
        )

        self.assertIn('subtasks', response.data)
        self.assertIsInstance(response.data['subtasks'], list)

        for subtask_data in response.data['subtasks']:
            self.assertIsInstance(subtask_data['title'], str)
            self.assertIsInstance(subtask_data['status'], str)

```

