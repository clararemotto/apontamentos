from django.urls import path
from .views import index, add_activity

urlpatterns = [
    path('', index, name='index'),
    path('add', add_activity, name='add'),
    
]
