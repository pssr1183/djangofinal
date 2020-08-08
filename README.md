# Django Telusko
Here you can find two applications, first one is a simple django based calculator (using forms and POST requests), and the second app is TRAVELLO website.
### If you want to run the project you must create migrations for each apps:
``` bash
     $ python manage.py makemigrations my_app
     $ python manage.py makemigrations travello
     $ python manage.py migrate
```
#### By Rustam-Z

## MY NOTES:
---
- my_app = the name of app
- my_project = the name of project
- python manage.py help
---

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
=======================================================
6. Create a folder 'templates' and then go to 'settings.py'
and in TEMPLATES->DIRS write [os.path.join(BASE_DIR, 'templates')],
7. After change my_app//views.py for rendering 'index.html' -> 
return render(request, 'index.html')
8. in index.html <from action='add' method='POST'> then go to my_app//urls.py and add path('add', views.add, name='add'), then in views.py describe the function and render .html:
  def add(request):
      val1=request.POST["num1"]
      val2=request.POST["num2"]
      res=int(val1)+int(val2)
      return render(request, 'result.html', {'result':res})
9. in index.html do not forget to include {% csrf_token %} for security 
=======================================================
10. MVT/MTV Model-View-Template, Data-Logic-Layout -- We have Model(DataBase) and Template(with DTL Django template language), data from user comes as object and who   will link this? urls is linking, so the main logic is in the views.
11.1. static file creation: settings.py->
  STATIC_URL='/static/' 
  STATICFILES_DIRS=[os.path.join(BASE_DIR, 'static')]
  STATIC_ROOT=os.path.join(BASE_DIR, 'assets')
  ==>OR<==
  STATIC_URL = '/static/'
  STATIC_DIR = os.path.join(BASE_DIR, 'static')
  STATICFILES_DIRS = [STATIC_DIR]
11.2. python manage.py collectstatic
11.3. change the directory and names in .html files:
  {% load static %}
  <img src="{% static "my_app/example.jpg" %}" alt="My image">
12. use blocks, for loop, if/else statement of Django into .html after creating a MODEL in steps 13.x.
=======================================================
13.1. Django ORM->App<-->DataBase is being created automaticly
13.2. Download PostgreSQL and PGAdmin 4: Password: Rr87654321 and 0999
13.3. then create a database in PG admin, do not forget NAME!
13.4. go to settings.py->DATABASES change into:
  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'telusko', 
        'USER': 'postgres',
        'PASSWORD': 'Rr87654321',
        'HOST': 'localhost',
      }
  }
13.5. how to connect Python with PostgreSQL? pip install psycopg2
13.6. THEN CREATE A MODEL IN models.py
  CharField, ImageField ...
13.7. add an app in list of INSTALLED_APPS
13.8.1. python manage.py makemigrations
13.8.2. python manage.py sqlmigrate my_app 0001 [ it crates a table]
13.8.3. python manage.py migrate
14.1. ADMIN PANEL admin.py -> steps
  Haha, Good Job :) Do not forget to register models in admin.py:
    from .models import [ClassName-it is ur model]
    admin.site.register(ClassName)
14.2. python manage.py createsuperuser
15.1. For the Images we must create a path for media, it is the location of media file added from Admin panel
  MEDIA_URL = '/media/'
  MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
15.1.2 in root urls.py add following ->
  from django.conf import settings
  from django.conf.urls.static import static
  urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
15.3. in .html we must use smth.smth.url in the end 
16. travello/views.py->
  from django.shortcuts import render
  from travello.models import Destination
  def index(request):
      dests = Destination.objects.all()
      return render(request, "index.html", {'dests' : dests} )
=======================================================
17. USER REGISTRATION with forms: id--password--name--mail-> register.html
  <form action="register" method="POST">
      {% csrf_token %}
      <input type="text" name="first_name" placeholder="First name">
      ... ...
  </form>
18. ORM of Django has the build in model for User-> accounts/views.py
  from django.contrib.auth.models import User, auth
  if request.method=='POST':
        first_name = request.POST['first_name']
        ... ...
        


