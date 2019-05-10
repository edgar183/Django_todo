# Django to do project. 

- sudo pip3 install django==1.11
  - Install Django LT support version

- django-admin startproject django_todo .
  - Start new project with name django_todo in root dir

- django-admin startapp todo
  - Start app in django project. the app have its own views. it is component to project.

- python3 manage.py runserver $IP:$C9_PORT
  - To start server. This commant can be added to .bash_aliases file alias run="python3 ~/workspace/manage.py runserver $IP:$C9_PORT"

1. Create a view in views.py to be do somthing. renders html
1. The view needs to be imported and added to url.py file to be displaied in browser. 
1. In settings.py add new line in INSTALLED_APPS  the name of the app (todo)

- python3 manage.py migrate
- python3 manage.py createsuperuser
    - creare admin in admin panel that can be accessted by url/admin

- .sqliterc file in root of workspace to handle .headers on .mode column every time we are using sqlite3 in terminal.

## Modal/Table in db
- create new modal in modals.py
    - in terminal python3 manage.py makemigrations
    - python3 manage.py migrate this will create new table in DB
    - register new modal in admin.py file to use it in admin panel

## Test
 When runing tests the class needs to start with test_* and command is python3 manage.py test
 - to check coverage of thest need to install sudo pip3 install coverage
 - coverage run manage.py test
 - coverage run --source=todo manage.py test to see only the todo tests
 - coverage report generates the report 

## Deployment to Heroku
1. sudo pip3 install gunicorn
2. install PostgreSQL sudo pip3 install psycopg2
3. create app from bash heroku create "app name" --region eu
4. create DB heroku addons:create heroku-postgresql:hobby-dev
5. to parse the DB url sudo pip3 install dj_database_url 
6. chenge DATABASE url in settings.py to DATABASES = {'default': dj_database_url.parse("p***")}
7. 