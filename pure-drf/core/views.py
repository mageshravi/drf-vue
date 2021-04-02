import json
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.contrib.auth import authenticate, login

@ensure_csrf_cookie
def set_csrf_cookie(request):
    return JsonResponse({'detail': 'CSRF cookie set'})

@require_POST
def api_login(request):
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')
    if username is None or password is None:
        return JsonResponse({
            'errors': {
                '__all__': 'Please enter both username and password'
            }
        }, status=400)
    # endif

    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({'detail': 'Success'})
    # endif

    return JsonResponse({'detail': 'Invalid credentials'}, status=400)
