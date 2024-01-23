<!-- TOC -->
* [**Authentication, Authorisation, JWT, Testing**](#authentication-authorisation-jwt-testing)
* [**Authentication, auth methods**](#authentication-auth-methods-)
* [**Authorisation, auth methods**](#authorisation-auth-methods-)
* [**Custom User model**](#custom-user-model-)
* [**Create custom UserManager**](#create-custom-usermanager-)
* [**Custom User's Serializer**](#custom-users-serializer-)
* [**JWT Authentication, and Authorisation**](#jwt-authentication-and-authorisation-)
* [**JWT principles**](#jwt-principles-)
* [**JWT creation**](#jwt-creation-)
* [**Custom JWT**](#custom-jwt-)
* [**Testing**](#testing-)
<!-- TOC -->

# **Authentication, Authorisation, JWT, Testing**

До этого мы реализовывали возможность регистрации                                                         
и логина в систему на стороне фронта, путём написания шаблонов,                                                         
форм, создания новых пользователей, входа в систему.                                                           

Давайте же рассмотрим теперь этот функционал со стороны бэка.                                                             

В целом, **аутентификация** и **авторизация** - понятия достаточно важные                                                         
в программировании. ИНогда с ними можно достаточно плотно работать,                                                         
крайне важно при этом не путать эти понятия, ведь они разные.


# **Authentication, auth methods**                                                          

**Аутентификация** - процесс подтверждения подлинности пользователя или                                                             
устройства, обычно для получения доступа к системе или ресурсу.                                                             
Основной целью аутентификации является убедиться, что пользователь                                                            
или система действительно являются тем, за кого они себя выдают.                                                 

**Существуют различные методы аутентификации:**                                                            

**Парольные методы**: Это самый распространенный метод, включающий в себя                                                             
использование **статических** (например, **PIN-коды**, **текстовые пароли**) или                                                             
**динамических** паролей (например, **одноразовые пароли**, отправляемые по **SMS**).                                                            

**Комбинированные методы**: Используются несколько методов одновременно,                                                             
например, **парольные методы** в сочетании с **криптографическими сертификатами**.                                                            

**Биометрические методы**: Основаны на уникальных физиологических или                                                            
поведенческих характеристиках пользователя, например, отпечатках пальцев,                                                             
сканировании сетчатки глаза, распознавании голоса или даже ДНК.                                                            

**Информация о пользователе**: Включает личные данные, которые могут быть                                                             
использованы для восстановления доступа, например, дата рождения, номер                                                             
телефона или другая личная информация.                                                            

**Геоданные**: Использование данных о местоположении пользователя для                                                             
аутентификации, например, с помощью **GPS**.                                                            

**Также важно отметить различные типы аутентификации в зависимости от                                                             
количества используемых методов:**                                                            

**Однофакторная аутентификация**: Используется только один метод.                                                            
**Многофакторная аутентификация**: Сочетает несколько методов, повышая тем                                                            
самым уровень безопасности.                                                            


**Аутентификация** часто используется в комплексе с другими процессами,                                                             
такими как **идентификация** (**определение пользователя**) и **авторизация**                                                             
(предоставление доступа к определенным ресурсам или функциям в                                                            
системе)                                                                                                                        

---

# **Authorisation, auth methods**                                                                 


**Авторизация** - процесс, в рамках которого система определяет, какие права                                                                 
и привилегии имеет аутентифицированный пользователь или система. Этот                                                                 
процесс следует за аутентификацией и обычно включает в себя присвоение                                                                
определенных прав доступа к ресурсам и функциям в системе.                                                                

Пример авторизации можно увидеть в рамках использования личного кабинета на                                                                 
каком-либо веб-сайте. После успешного ввода логина и пароля (**аутентификации**),                                                                
система "**понимает**", какие действия может выполнять пользователь, и предоставляет                                                                 
ему доступ к определенным функциям и информации. Например, в образовательной                                                                
платформе пользователь после авторизации может читать уведомления, видеть                                                                 
список доступных курсов, просматривать их и учиться.                                                                

Авторизация также защищает систему от несанкционированных                                                                 
изменений, обеспечивая, чтобы только определенные пользователи могли выполнять                                                                
определенные действия. Например, в компании только сис админ                                                                
может устанавливать программное обеспечение на рабочие компьютеры, в то                                                                
время как обычным пользователям это делать не разрешается.                                                                

Таким образом, авторизация тесно связана с **идентификацией** (установление                                                                
личности пользователя) и **аутентификацией** (подтверждение подлинности                                                                
пользователя) и является ключевым элементом в обеспечении безопасности                                                                
системы и защите конфиденциальной информации                                                                


Если уж совсем вкратце и понятным языком:                                                  

**Аутентификация** - кто ты.                                                     
**Авторизация** - что ты можешь делать.                                                             

---

# **Custom User model**                                                

Начнём с того, что всё же перепишем дефолтного пользователя, которого                                                   
предлагает **Django** нам по умолчанию. Он больше настроен на **superadmin**                                                    
что нам не особо может подходить.                                                  

начнём с моделей:                                                        

```python
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
)
from django.utils.translation import gettext_lazy

from apps.user.manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        max_length=120,
        unique=True,
        verbose_name=gettext_lazy('Email address')
    )
    first_name = models.CharField(
        max_length=50,
        verbose_name=gettext_lazy('First name')
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name=gettext_lazy('Last  name')
    )
    username = models.CharField(
        max_length=30,
        blank=True,
        null=True
    )
    phone = models.CharField(
        max_length=75,
        blank=True,
        null=True
    )
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return self.email

    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

```

Здесь мы переопределили нашу базовую модель пользователя, прописав свои                                                   
свои настройки и так же, как вы могли обратить внимание, допом указали                                                     
настройки и для админа, так как модель будет общая. Просто для админа                                                         
поля по умолчанию будут в состоянии **False**                                                

Дополнительно мы тут указываем настройку поля `username`, которое после                                            
нашего переопределения будет именно `email`. Так же указываем                                            
обязательные поля при регистрации, помимо наших всяких `email` и `password`                                             
За это отвечает атрибут `REQUIRED_FIELDS`. Его основная цель - указать нам                                             
какие дополнительные поля должны быть включены в выборку при создании                                                       
пользователя через коммандрую строку командой `createsuperuser`                                                         
Эти поля идут допом, такие поля, как `username` и `password` воспринимаются                                                   
системой **DJango**, как само собой разумеющееся.                                                        

Так же, так как мы переопределили пользователя, написав своего, необходимо                                                  
еще и менеджера для него подогнать. За это будет отвечать будущий класс                                                     
`UserManager`, в котором мы опишем как у нас должен будет создаваться                                                     
пользователь (админ, или же обычный, не важно.)                                                   

---

# **Create custom UserManager**                                                 

Штош, теперь к кастомной модели добавим и кастомного манагера:                                                 

```python
from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy


class UserManager(BaseUserManager):
    def email_validator(self, email):
        try:
            validate_email(email)
        except ValidationError as err:
            raise ValueError(
                gettext_lazy(f"{err.message}.\nPlease, enter a valid email")
            )

    def create_user(self, email, first_name, last_name, password, **extra_fields):
        if email:
            email = self.normalize_email(email)
            self.email_validator(email=email)
        else:
            raise ValueError(gettext_lazy(
                "Email is required."
            ))

        if not first_name:
            raise ValueError(gettext_lazy(
                "First name is required."
            ))

        if not last_name:
            raise ValueError(gettext_lazy(
                "Last name is required."
            ))

        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, first_name, last_name, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_verified", True)

        if not extra_fields.get("is_staff"):
            raise ValueError(
                gettext_lazy("Admin must be 'is staff'")
            )
        if not extra_fields.get("is_superuser"):
            raise ValueError(
                gettext_lazy("Admin must be a superuser")
            )

        user = self.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
            **extra_fields
        )
        user.save(using=self._db)

        return user

```

Тут мы создаём класс будущего менеджера, который будет наследоваться                                                    
от `BaseUserManager` класса. у нас будет тры метода: валидация **email**                                                  
создание обычного пользователя и создание суперюзера.                                                   

для валидатора имэйла ничего особо не выдумываем. Мы принимаем значение,                                                
пытаемся провалидировать его уже написанными инструментами **Django**,                                                   
если что-то не так - поднимаем ошибку с нужным нам значением.                                                     

При создании пользователя мы будем принимать ряд аргументов для регистрации                                                   
и не отходя от кассы проверять их на валидность, поля с паролями на совпадение                                              

если всё оке - создаём объект будущего пользователя, прокидывая в него                                                    
наши поля. Так как мы работаем с написанием своего, кастомного менеджера                                                   
мы не будем прописывать здесь никаких `User` напрямую, так как мы создаём                                                   
менеджера, нашим `User` для него будет - `self.model`                                                    

после создания объекта пользователя мы у этого объекта вызываем метод                                                      
который отвечает за сетап пароля, после чего мы у этого объекта вызываем                                              
метод `save(using=self._db)`, который данные и сохранит.                                                  

в конце возвращаем созданного пользователя.                                             

Крайне похоже будет работать и метод на создание суперюзера, только                                                     
полей немного больше.                                                                                 

Так же необходимо в настройках Джанго показать ему, что модель пользователя                                                 
должна быть не по умолчанию базовой, а именно той, что написали мы:                                                     

```python
AUTH_USER_MODEL = "user.User"
```

---

# **Custom User's Serializer**                                                   

```python
class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68,min_length=8, write_only=True)
    password2 = serializers.CharField(max_length=68, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password', 'password2']

    def validate(self, attrs):
        password = attrs.get("password", "")
        password2 = attrs.get("password2", "")

        if password != password2:
            raise serializers.ValidationError(
                PASSWORDS_DO_NOT_MATCH_ERROR
            )

        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data.get("email"),
            first_name=validated_data.get("first_name"),
            last_name=validated_data.get("last_name"),
            password=validated_data.get("password")
        )

        return user

```


Для валидации данных на создание пользователя и будущее сохранение напишем                                                   
сериализатор. Тут допом определим поля для пароля, что они должны быть только                                                  
для записи. Никакого чтения, так как это пароль, быть не должно.                                                       

Метод `validate` будет обрабатывать данные по паролю. Они должны совпадать.                                                   

Метод `create`, собственно, будет отвечать за создание пользователя.                                                    

Остаётся написать класс-отображение, который позволит нам создавать                                                       
нового пользователя:                                             


```python
class UserRegistrationGenericView(CreateAPIView):
    serializer_class = UserRegisterSerializer

    def post(self, request: Request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response(
                status=status.HTTP_201_CREATED,
                data=serializer.data
            )
        return Response(
            status=status.HTTP_400_BAD_REQUEST,
            data=serializer.errors
        )
```

Тут ничего особенного. Мы принимаем в форме данные для регистрации. Эти                                                 
данные улетают в сериализатор для валидации. Если всё хорошо, ошибок нет и                                               
данные валидные - сохраняем нового пользователя и возвращаем ответ с успешным                                              
успехом. В противном же случае возвращаем ответ с ошибками из сериализатора.                                                  


Подвязываем этот класс-отображение к `urls`:                                                     

```python
urlpatterns = [
    ...
    ...
    ...
    path("auth/register/", UserRegistrationGenericView.as_view()),  # NEW
] + router.urls
```


---

# **JWT Authentication, and Authorisation**                                                           

В целом вариантов по авторизации и аутентификации достаточно много в **Django**                                          

Крайне много различных способов для входа и прокидывания запросов по разным                                              
токенам у **Django**. Их все можно найти на офф сайте [DRF](https://www.django-rest-framework.org/api-guide/authentication/)                                                                                         

От самых обычных аутентификаций, до работы с токенами, сессиями и чем-то сторонним.                                                  

Мы будем рассматривать работу именно с `JWT` токенами.                                                                    

# **JWT principles**                                                                 

Их идея достаточно сильно отличается от дефолтных методов аутентификации.                                                   

стандартный `JWT-token` может выглядеть примерно так:                                                                     

```json
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwNjA5NDU3MSwiaWF0IjoxNzA2MDA4MTcxLCJqdGkiOiJjMjcyM2IxYjYyNDU0OTEzYTIwNTc4MDQyNWIwMmM1NCIsInVzZXJfaWQiOjN9.0pepPC9H0GiZ_UUQgU9RA2l6nnDzK3sR2vxHwdyn1fg",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA2MDA4NDcxLCJpYXQiOjE3MDYwMDgxNzEsImp0aSI6IjFmNWZjZGM2MWE0ZjRhZjY4ZWE2ODM0ZDU4ZTJlYjBkIiwidXNlcl9pZCI6M30.xkD5MSQma8fKJnmVgy5_NRlsmPdZFnY2UPxcmXNPP_g"
}
```

Если хорошенько изучить эти значения, можно увидеть, что такой токен разделён на                                                      
три значения. Разделителем выступает точка.                                                                          


Вот эти самые три значения:                                                                    

`eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9`
`eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwNjA5NDU3MSwiaWF0IjoxNzA2MDA4MTcxLCJqdGkiOiJjMjcyM2IxYjYyNDU0OTEzYTIwNTc4MDQyNWIwMmM1NCIsInVzZXJfaWQiOjN9`
`0pepPC9H0GiZ_UUQgU9RA2l6nnDzK3sR2vxHwdyn1fg`

* Первое значение - `header`                                                            
По умолчанию в **header** валяется следующее:                                                         
```json
{"alg":  "HS256", "typ": "JWT"}
```
Здесь валяется информация о типе шифрования данных, по умолчанию это как раз `HS256`                                                  
и так же о типе самого токена.                                                          

* Второе - `payloads`                                                        
Какая-то полезная нагрузка, информация, которую мы можем прокинуть допом в                                                        
наш токен. Стандартные данные, которые там можно встретить - **ID** пользователя,                                                
который получил этот токен, его **email** и так же время жизни самого токена.                                                     

```json                                                                                  
{
  "userId": 1,
  "exp": 1000,
  "email": "test.user@gmail.com"
}
```                                                                                  

Первые два значения из `JWT-token` в последствии преобразуются в последовательности                                                  
`ASCII` сомволов. Это достигается благодаря библиатеке `base64` и методу                                                          
`base64urlEncode(b'...')`                                                                 

То есть наши с вами `json` словарики из `header` и `payload` кодируются в `ASCII`                                                  
последовательность. Это работает и в обратную сторону. Эти закодированные строки                                               
можно обратно раскодировать в читаемые словарики.                                                       

Важно понимать, что данные эти не шифруются, а всего лишь кодируются. Это не защищает                                                   
их от просмотра. Но вот поменять данные эти никак не получится. Связано это с                                               
третьей сущностью - `signature`                                                                         

Третье - `signature`                                                                  
Специальная подпись. ОНа формируется следующим образом: берутся уже                                                          
закодированные данные из `header` и `payload`, объединяются между                                                    
собой в одну единую закодированную строку, после чего эта строка                                                        
уже шифруется тем алгоритмом, который как раз был прописан в `header`                                                                   
`HMAC-SHA256(header.payload, SECRET_KEY)`                                                            

При этом всём если уже после кодирования, после генерирования подписи данные                                                           
как-то поменять, то подпись уже не будет соответствовать изначальной, что логично.                                                    
Таким образом и верификация уже не пройдёт.                                                     

**Как этот токен показывает себя в деле:**                                                

Возьмём пример с авторизацией через учётную запись `google`:                                                                

Клиент должен пройти процедуру авторизации. То есть клиент вводит свои                                                  
логин и пароль в форме. Этот запрос будет проходить через сервис, на который                                             
мы этот запрос и делали. Допустим войти на какую-нибудь биржу труда через аккаунт                                             
`google`. Этот сервис перенаправляет наш запрос с данными на сервер который                                                        
работает в рамках всего инструментария компании.                                                                                                                        
Сервер в свою очередь проверяет есть ли пользователь с такими логином                                               
и паролем и если есть - отдаёт ему два токена: `access` и `refresh`

Рефреш токен дополнительно сохраняется в базе данных этого сервера.                                                     
На стороне же клиента сохраняются оба токена. Для доступа к сервисам                                                     
используется как раз первый токен - `access`, который имеет достаточно короткое                                                
время жизни(2-5 мин). Так как токен содержит информацию о пользователе, при                                                  
запросе сервис понимает какой пользователь запрашивает данные.                                                

Так же сервис может проверить корректность токена по его подписи, так как сервисы                                                    
знают тот самый единый `SECRET_KEY`, которым подпись шифруется.                                                          
Благодаря таким манипуляциям возможность прямой подмены данных каким-то третьим лицом                                                  
прктически невозможна.

**Для чего же нужен второй вид токена?** Теоритически можно было бы поставить                                                   
большое время жизни для `access` и не париться со всеми этими манипуляциями. Но,                                                 
к сожалению, злоумышленников никто не убирал и хоть шанс на получение вашего токена                                                  
крайне мал, он есть. Поэтому-то главный токен и не живёт слишком долго.                                                       
Но тогда другой вопрос: **если время жизни в пределах пяти минут. То после этих                                                        
пяти минут нужно будет по новой логиниться?** На счастье нет.                                                               

Когда время действия `access` токена заканчивается, на сервер авторизации отправляется                                             
`refresh` токен. Сервер принимает его и на его основе создаёт новые `access` и `refresh`                                                       
токены, отправляя обновлённые токены обратно клиенту, благодаря чему можно                                                           
не входя в систему каждые пять минут спокойно себе заниматься своими делами.                                                  

Сами же эти токены доступа и обновления на стороне клиента лучше всего хранить                                            
в как можно более защищённом месте, во избежание хищения этих токенов                                                    
третьими лицами.                                                                                                        

Рассмотрим наиболее распространенные и рекомендуемые подходы к хранению                                                    
этих токенов в зависимости от типа клиентского приложения:                                                    

1. **Веб-приложения (браузеры)**:                                                    
* `HTTP-Only Cookies`: Самый безопасный вариант для веб-приложений. Токен                                                     
хранится в куки, помеченных как `HTTP-Only`, что делает их недоступными                                                     
для `JavaScript` на клиентской стороне, снижая риск `XSS-атак`. Это                                                     
также обеспечивает защиту от `CSRF-атак`, если правильно настроить                                                     
атрибуты `SameSite`.                                                    

* `LocalStorage/SessionStorage`: Хотя это удобные способы, они более уязвимы                                                     
для `XSS-атак`, поскольку `JavaScript` на клиентской стороне может читать и                                                     
изменять данные в `LocalStorage` и `SessionStorage`.                                                    

2. **Мобильные и настольные приложения**:                                                    
* `Защищенное хранилище`: Используйте встроенные в `ОС` механизмы безопасного                                                     
хранения, такие как `Keychain` в `iOS` и `Keystore` в `Android`. Эти механизмы                                                     
предоставляют зашифрованное хранение для чувствительных данных.                                                    

* `Secure Enclave или Trusted Execution Environment`: Это специализированные                                                    
области в аппаратуре устройства, предназначенные для безопасного хранения                                                     
криптографических ключей и других чувствительных данных.                                                    

3. **Одностраничные приложения (SPA)**:                                                    
* `Memory-Based Storage`: Хранение токенов в памяти `JavaScript` (например, в                                                     
переменных). Это уменьшает риск постоянных `XSS-атак`, но требует тщательного                                                     
управления жизненным циклом токенов, особенно при обновлении страницы.                                                       

* `HTTP-Only Cookies`: Также подходят для `SPA`, особенно если используется                                                     
серверный рендеринг или некоторые серверные функции.                                                    

---

# **JWT creation**                                                     

Первое, что нам понадобится - библиатека для работы с `jwt` токенами.                                                   

За это у нас может отвечать библиатека `djangorestframesork-simplejwt`                                               

`pip install djangorestframework-simplejwt`                                              

После успешной установки нам понадобится добавить в приложения эту библиатеку:                                                 

```python
INSTALLED_APPS = [
    # default django apps

    # 3-rd party
    "rest_framework",
    "rest_framework_simplejwt",  # NEW
    "drf_yasg",

    # local
    "apps.todo.apps.TodoConfig",
    "apps.user.apps.UserConfig",
    "apps.api.apps.ApiConfig",
]
```

Далее в спец настройках именно для `REST_FRAMEWORK` нам необходимо прописать                                                   
вариант аутентификации:                                                             

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}
```

После чего нам необходимо будет добавить новые эндпоинты в наш `urls.py`:                                                     

```python
from rest_framework_simplejwt.views import (  # NEW
    TokenObtainPairView,  # NEW
    TokenRefreshView,  # NEW
)  # NEW

urlpatterns = [
    ...
    ...
    path("auth/register/", UserRegistrationGenericView.as_view()),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # NEW
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # NEW
] + router.urls
```

И, собственно, попробовать прокинуть запрос на вход в систему :)                                                        
Если всё окей - в качестве ответа от работы класса-отображения мы получим                                                
`access` и `refresh` токены.                                                                  

Так же, мы можем настроить более детальнее наш `JWT`. Для этого в настройках                                                 
проекта мы можем прописать следующие настройки:                                                    

```python
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "UPDATE_LAST_LOGIN": False,

    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "VERIFYING_KEY": "",
    "AUDIENCE": None,
    "ISSUER": None,
    "JSON_ENCODER": None,
    "JWK_URL": None,
    "LEEWAY": 0,

    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",

    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",

    "JTI_CLAIM": "jti",

    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),

    "TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainPairSerializer",
    "TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSerializer",
    "TOKEN_VERIFY_SERIALIZER": "rest_framework_simplejwt.serializers.TokenVerifySerializer",
    "TOKEN_BLACKLIST_SERIALIZER": "rest_framework_simplejwt.serializers.TokenBlacklistSerializer",
    "SLIDING_TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainSlidingSerializer",
    "SLIDING_TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSlidingSerializer",
}
```

Теперь, перед тестированием этого дела, мы можем обновить наши классы                                                        
специальными настройками разрешений. Нам понадобятся:                                                   

```python
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
    IsAdminUser
)
```

После чего мы можем с вами добавлять к нашим классам эти пермишны:                                                 

```python
permission_classes = [IsAuthenticated]
```

---

# **Custom JWT**                                                               

Мы так же можем переписать генерацию токена под себя, добавив туда доп                                                   
информацию о пользователе, если необходимо. Как это можно сделать?                                                     

В сериализаторах нужно будет добавить новый сериализатор для токена:                                                  

```python
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['email'] = user.email
        token['first_name'] = user.first_name

        return token
```

Тут мы наследуемся от базового сериализатора `TokenObtainPairSerializer`,                                                
после чего перегружаем метод класса `get_token()`. Тут мы сперва получаем                                                     
токен, после чего добавляем к нему нужную нам инфу. В конце токен возвращаем.                                                  


После в настройках **JWT** необходимо поменять дефолтный сериализатор на тот, что                                                   
мы написали:                                             

```json
"TOKEN_OBTAIN_SERIALIZER": "apps.api.serializers.MyTokenObtainPairSerializer",
```

Ну и так же мы можем переопределить класс-отображение для нашего токена, если                                              
захотим:                                                  


```python
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

    def post(self, request: Request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(
            status=status.HTTP_200_OK,
            data={
                "message": f"successful log-in.",
                "access_token": serializer.validated_data.get('access'),
                "refresh_token": serializer.validated_data.get('refresh')
            }
        )
```

в `urls.py` этот класс-отображение нужно будет поменять, соответственно.                                                 


Ну и добавим заодно классы-отображения для получения списка всех юзеров +                                                       
инфу об одном конкретном юзере:                                                      

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


class UserDetailGenericView(RetrieveAPIView):
    serializer_class = UserInfoSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]

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

```

И сериализаторы для них:                                                 

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
        response = self.client.get('http://127.0.0.1:8000/api/users/')
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
        response = self.client.get('http://127.0.0.1:8000/api/users/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_no_users(self):
        # Проверка на отсутствие пользователей
        User.objects.all().delete()
        self.client.force_authenticate(user=self.admin)
        response = self.client.get('http://127.0.0.1:8000/api/users/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

```
