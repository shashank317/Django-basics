
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.singup, name='signup'),
    path('signup/', views.singup, name='signup'),
    path('loginn/', views.loginn, name='login'),
    path('todo/', views.todo, name='todo'),
    path('edit_todo/<int:srno>/', views.edit_todo, name='edit_todo'),
    path('delete_todo/<int:srno>/', views.delete_todo, name='delete_todo'),
    path('toggle_todo/<int:srno>/', views.toggle_todo, name='toggle_todo'),
    path('signout/', views.signout, name='signout'),
]
