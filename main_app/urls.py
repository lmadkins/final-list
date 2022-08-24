from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
    path('lists/', views.Lists.as_view(), name="lists_list"),
    path('lists/new', views.ListCreate.as_view(), name="list_create"),
]