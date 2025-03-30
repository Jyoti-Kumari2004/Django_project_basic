"""
URL configuration for try1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from core.views import home, sucess, trail
from vege.views import delete_recepie, recepie, update_recepie
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from todo.views import delete_todo, home_todo, table_todo, update_todo

urlpatterns = [
    path("", home, name="home"),
    path("recepie/", recepie, name="recepie"),
    path("delete_recepie/<id>", delete_recepie, name="delete_recepie"),
    path("update_recepie/<id>", update_recepie, name="update_recepie"),
    path("sucess_page/", sucess, name="sucess_page"),
    path("trail_page/", trail, name="trail_page"),
    path("todo/", home_todo, name="home_todo"),
    path("delete_todo/<id>", delete_todo, name="delete_todo"),
    path("update_todo/<id>", update_todo, name="update_todo"),
    path("table_todo/", table_todo, name="update_todo"),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
