"""django_todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from todo.views import get_todo_list, create_an_item, edit_an_item, toggle_status
from accounts import urls as accounts_urls
from accounts.views import index

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # r is for regular expretion and ^ is for start of url and $ end of url
    url(r'^$', get_todo_list),
    url(r'^add$', create_an_item),
        # \d+ pass in digit that is biger then 9
        # ?P to tell that this is going to be an expression and
        # then we'll put it inside of angular brackets we'll put id
    url(r'^edit/(?P<id>\d+)$', edit_an_item),
    url(r'^toggle/(?P<id>\d+)$', toggle_status),
    url(r'^index/$', index, name='index'),
    url(r'^index/accounts/', include(accounts_urls))
    
]
