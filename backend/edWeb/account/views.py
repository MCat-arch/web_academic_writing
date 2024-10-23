from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, JsonResponse
from .models import User
from django.views.decorators.csrf import csrf_exempt
import json 

# Create your views here.

@csrf_exempt
def login_page(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            user = User.objects.get(username = username, password = password)
           # return render(request='main.html', {'user':user})
            return JsonResponse({'message':'Login succesful'})
        except User.DoesNotExist:
            return JsonResponse({'message': 'login requaired'}, status=405)
            
    return render(request, 'login.jsx')

@csrf_exempt
def register(request):
    if request.method == 'POST':
       try:
            data = json.loads(request.body)  # Load the JSON data from the request body
            username = data.get('username')
            password = data.get('password')
            email = data.get('email')  # Handle email if needed

            # Check if all fields are provided
            if not username or not password or not email:
                return JsonResponse({'error': 'Missing fields'}, status=400)

            # Save the new user
            user = User(username=username, password=password)
            user.save()

            return JsonResponse({'message': 'User created successfully'}, status=201)
        
       except json.JSONDecodeError:
           return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    
    return JsonResponse({'error': 'Invalid request method'}, status=405)
    