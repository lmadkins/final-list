from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
    # path('password-reset/', views.PasswordResetView.as_view(), name='password_reset'),path('password-reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
    path('lists/', views.Lists.as_view(), name="lists_list"),
    path('lists/new', views.ListCreate.as_view(), name="list_create"),
]