from django.urls import path
from views import *

urlpatterns = [
    path('test/', create_user_view , name='test'),
]