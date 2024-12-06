from django.urls import path
from activity.views import index, add_activity

urlpatterns = [
    path('', index),
    path('add', add_activity)
]
