# Django Telusko
Here you can find two applications, first one is a simple django based calculator (using forms and POST requests), and the second app is TRAVELLO website.
### If you want to run the project you must create migrations for each apps:
``` bash
     $ python manage.py makemigrations my_app
     $ python manage.py makemigrations travello
     $ python manage.py migrate
```
### By Rustam-Z

## MY NOTES:
- my_app = the name of app
- my_project = the name of project
- python manage.py help
- Creating a virtual environment and creating a Django project:
``` bash
python -m venv my_env
.\my_env\Scripts\activate
pip install Django
django-admin startproject my_project
python manage.py startapp my_app
```
- include my_app/urls.py in the ROOT urls.py
- Create migratioins
``` bash 
python manage.py migrate
python manage.py sqlmigrate my_app 0001
python manage.py makemigrations my_app
```
#### Create a folder 'templates', then go to 'settings.py' and in TEMPLATES->DIRS add 
``` python 
[os.path.join(BASE_DIR, 'templates')],
```
- After change my_app/views.py for rendering 'index.html'
``` python
return render(request, 'index.html')
```
- in index.html <from action='add' method='POST'> then go to my_app/urls.py add path('add', views.add, name='add'), then in views.py describe the function and render.html:
 ``` python
 def add(request):
      val1=request.POST["num1"]
      val2=request.POST["num2"]
      res=int(val1)+int(val2)
      return render(request, 'result.html', {'result':res})
```
- in index.html do not forget to include {% csrf_token %} for security 

#### INFO! MVT/MTV Model-View-Template, Data-Logic-Layout -- We have Model(DataBase) and Template(with DTL Django template language), data from user comes as object and who   will link this? urls is linking, so the main logic is in the views.

- static file creation in settings.py
``` python
  STATIC_URL='/static/' 
  STATICFILES_DIRS=[os.path.join(BASE_DIR, 'static')]
  STATIC_ROOT=os.path.join(BASE_DIR, 'assets')
  ==>OR<==
  STATIC_URL = '/static/'
  STATIC_DIR = os.path.join(BASE_DIR, 'static')
  STATICFILES_DIRS = [STATIC_DIR]
```
``` bash
python manage.py collectstatic
```
- change the directory and names in .html files:
``` html
  {% load static %}
  <img src="{% static "my_app/example.jpg" %}" alt="My image">
```
#### use blocks, for loop, if/else statement of Django into .html after creating a MODEL in next steps 
1. Django ORM->App<-->DataBase is being created automaticly
2. Download PostgreSQL and PGAdmin 4: Password: Rr87654321 and 0999
3. then create a database in PG admin, do not forget NAME!
4. go to settings.py->DATABASES change into
``` python
  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'telusko', 
        'USER': 'postgres',
        'PASSWORD': '********',
        'HOST': 'localhost',
      }
  }
 ```
5. how to connect Python with PostgreSQL? pip install psycopg2
6. THEN CREATE A MODEL IN models.py CharField, ImageField ...
7. add an app in list of INSTALLED_APPS

``` bash 
python manage.py makemigrations
python manage.py sqlmigrate my_app 0001
python manage.py migrate
```
#### ADMIN PANEL admin.py -> steps
1. Haha, Good Job :) Do not forget to register models in admin.py:
  ``` python
    from .models import [ClassName-it is ur model]
    admin.site.register(ClassName)
 ```
2. ``` bash
python manage.py createsuperuser
```
3. For the Images we must create a path for media, it is the location of media file added from Admin panel
``` python
  MEDIA_URL = '/media/'
  MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```
4. in root urls.py add following
``` python
  from django.conf import settings
  from django.conf.urls.static import static
  urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  ```
5. in .html we must use smth.smth.url in the end 
6. travello/views.py
``` python
  from django.shortcuts import render
  from travello.models import Destination
  def index(request):
      dests = Destination.objects.all()
      return render(request, "index.html", {'dests' : dests} )
  ```
#### USER REGISTRATION with forms: id--password--name--mail-> register.html
1. 
``` html
  <form action="register" method="POST">
      {% csrf_token %}
      <input type="text" name="first_name" placeholder="First name">
      ... ...
  </form>
```
2. ORM of Django has the build in model for User-> accounts/views.py
``` python
  from django.contrib.auth.models import User, auth
  if request.method=='POST':
        first_name = request.POST['first_name']
        ... ...
  ```
        


