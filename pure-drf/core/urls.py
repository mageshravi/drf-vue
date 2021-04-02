from . import views
from django.urls.conf import path

urlpatterns = [
    path('set-csrf/', views.set_csrf_cookie, name='set-csrf'),
    path('login/', views.api_login, name='login'),
]
