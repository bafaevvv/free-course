from django.urls import path
from . import views

app_name = 'course'

urlpatterns = [
      path('', views.index, name='index'),
      path('<int:course_id>/', views.course_detail, name='course_detail'),  
      path('course/', views.course, name='course'),
      path('category/', views.category, name='category'),
      path('category_detail/<pk>/', views.category_detail, name='category_detail'),
]