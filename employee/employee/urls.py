"""
URL configuration for employee project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from work.views import Employee,BookView,Booklist,PersonView,Personlist,Book_detailedView,Student,Book_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/', Employee.as_view()),
    path('book/',BookView.as_view()),
    path('booklist/',Booklist.as_view(), name="book-al"),
    path('person/',PersonView.as_view()),
    path('personlist/',Personlist.as_view()),
    path('bkdetail/<int:pk>',Book_detailedView.as_view(), name='book-det'),
    path('student/',Student.as_view()),
    path('bookdel/<int:pk>/remove',Book_delete.as_view(),name='book-del')
]
