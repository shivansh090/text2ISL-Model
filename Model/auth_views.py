from django.http import JsonResponse
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk
from django.contrib.staticfiles import finders
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
import json

@csrf_exempt
def api_signup_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        form = UserCreationForm(data)
        if form.is_valid():
            user = form.save()
            token, _ = Token.objects.get_or_create(user=user)  # Generate a token for the new user
            return JsonResponse({'status': 'success', 'message': 'User created successfully', 'token': token.key}, status=201)
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Only POST requests allowed'}, status=405)

@csrf_exempt
def api_login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)

        if user:
            token, _ = Token.objects.get_or_create(user=user)  # Generate or get token
            return JsonResponse({'status': 'success', 'message': 'User logged in successfully', 'token': token.key}, status=200)
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid credentials'}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Only POST requests allowed'}, status=405)

@csrf_exempt
def api_logout_view(request):
    if request.method == 'POST':
        token = request.META.get('HTTP_AUTHORIZATION').split()[1] if 'HTTP_AUTHORIZATION' in request.META else None
        if token:
            try:
                token_obj = Token.objects.get(key=token)
                token_obj.delete()  # Delete token to log out user
                return JsonResponse({'status': 'success', 'message': 'User logged out successfully'}, status=200)
            except Token.DoesNotExist:
                return JsonResponse({'status': 'error', 'message': 'Invalid token'}, status=400)
        else:
            return JsonResponse({'status': 'error', 'message': 'Token required for logout'}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Only POST requests allowed'}, status=405)
