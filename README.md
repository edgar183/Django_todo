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