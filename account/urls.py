from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.login_views , name='login_url'),
    path('register/', views.register_user, name='register_url'),
    path('logout/', views.log_out, name='logout_url')
]