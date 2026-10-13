from django.urls import path

from . import views

app_name = 'practice'

urlpatterns = [
    path('', views.index, name='index'),
    path('recipes/', views.activity_list, {'kind': 'recipe'}, name='recipes'),
    path('recipes/<slug:slug>/', views.activity_detail, {'kind': 'recipe'}, name='recipe'),
    path('master-classes/', views.activity_list, {'kind': 'masterclass'}, name='masterclasses'),
    path('master-classes/<slug:slug>/', views.activity_detail, {'kind': 'masterclass'}, name='masterclass'),
    path('tasks/', views.activity_list, {'kind': 'task'}, name='tasks'),
    path('tasks/<slug:slug>/', views.activity_detail, {'kind': 'task'}, name='task'),
]
