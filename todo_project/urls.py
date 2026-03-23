from django.contrib import admin
from django.urls import path, include
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo.urls')),
    path('complete/<int:id>/', views.complete_task, name='complete'),
    path('delete/<int:id>/', views.delete_task, name='delete'),
]