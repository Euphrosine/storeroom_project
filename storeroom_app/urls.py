from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('api/', views.api_data_view, name='api_data_view'),
    path('', views.overall_view, name='overall_page'),
    path('tables/', views.tables_view, name='tables_page'),
    path('charts/', views.crop_data_view, name='charts_page'),
    path('login/', auth_view.LoginView.as_view(template_name='storeroom_app/login.html'), name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name='storeroom_app/logout.html'), name="logout"),

]
