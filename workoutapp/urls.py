from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name = 'index'),
    path('login_user/', views.login_user, name = 'login'),
    path('logout_user/', views.logout_user, name = 'logout'),
    path('register_user/', views.register_user, name='register_user'),
    path('home/', views.home, name='home'),
    path('create_plan/', views.createPlan, name='create_plan'),
    path('my_plan/', views.myPlan, name='my_plan'),
    path('delete_plan/<str:field_id>', views.deletePlan, name='delete_plan'),
]