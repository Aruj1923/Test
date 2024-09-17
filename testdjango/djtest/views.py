from django.shortcuts import render
from django.contrib.auth.models import User 
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import threading
from .models import Profile
from django.db import transaction
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@csrf_exempt
def create_user_view(request):
    # Create a new user which triggers the post_save signal
    print("Creating user...")
    User.objects.create(username="test_user2")
    print("User created!")
    return HttpResponse("User created!")




def create_user_threading(request):
    print(f"Caller thread ID: {threading.get_ident()}")
    
    # Create a new user, triggering the post_save signal
    try:
        User.objects.create(username="test_user")
    except:
        user = User.objects.get(username='test_user')
        user.delete()
        print("User Already exist We have deleted it.")
        User.objects.create(username="test_user")
    
    return HttpResponse("User created!")

@csrf_exempt
def create_user_view_profile(request):
    try:
        with transaction.atomic():
            print("Caller: Creating user...")
            # Create a user which triggers the post_save signal
            user = User.objects.create(username="test_user3")
            print("Caller: User created.")
            
            # Deliberately raise an exception to cause a rollback
            raise Exception("Something went wrong!")
    except Exception as e:
        print(f"Exception caught: {e}")
    
    # Check if the user and profile were rolled back
    user_exists = User.objects.filter(username="test_user").exists()
    profile_exists = Profile.objects.filter(user__username="test_user").exists()

    return HttpResponse(f"User exists: {user_exists}, Profile exists: {profile_exists}")




class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
    
    def __iter__(self):
        # We return an iterator that yields the length first and then the width
        yield {'length': self.length}
        yield {'width': self.width}


@api_view(['POST'])
def dimensions(request):
    print(request)
    a = request.data.get('a')
    b = request.data.get('b')
    rect = Rectangle(a, b)
    return Response(rect)
    

