from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all_emp', views.all_emp, name='all_emp'),
    path('add_emp', views.add_emp, name='add_emp'),
    path('delete_emp/', views.delete_emp, name='delete_emp'),
    path('update_list/', views.update_list, name='update_list'),
    path('update_emp/<int:emp_id>/', views.update_emp, name='update_emp')
]

