from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page , name="main_page"),
    path('category/<int:id>/', views.category_detail, name='category_detail' ),
    path('news/<int:id>/', views.news_detail, name='news_detail' ),
    path('news/comment/', views.create_coment, name='create_coment' ),
    path('news/likes', views.create_status, name='create_status')
]