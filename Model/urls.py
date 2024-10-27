# urls.py
from django.urls import path
from .auth_views import api_signup_view, api_login_view, api_logout_view
from .animation_views import ApiAnimationView

urlpatterns = [
    path('api/signup/', api_signup_view, name='api_signup'),
    path('api/login/', api_login_view, name='api_login'),
    path('api/logout/', api_logout_view, name='api_logout'),
    path('api/animation/', ApiAnimationView.as_view(), name='api_animation'),  # Note the use of as_view()
]