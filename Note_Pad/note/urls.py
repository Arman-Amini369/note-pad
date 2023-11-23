from django.urls import path, re_path
from . import views

app_name = "note"

urlpatterns = [
    path('', views.index, name="home"),
    path('detail/<int:note_id>', views.detail, name="detail"),
    path('create/', views.create, name="create"),
    path('delete/<int:note_id>', views.delete, name="delete"),
    path('edit/<int:note_id>', views.edit, name="edit"),
    path('contact/', views.contact, name="contact"),
    path('user_info/', views.user_info, name="user_info"),
]