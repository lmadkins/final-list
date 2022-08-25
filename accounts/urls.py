from django.contrib.auth import views
from django.urls import path, include
from . import views


urlpatterns = [
    path('signup/', views.Signup.as_view(), name="signup"),
    path('', include('allauth.urls')),
    path('', include('django.contrib.auth.urls')),
    # path('password-reset/', views.PasswordResetView.as_view(), name='password_reset'),path('password-reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # path('admin/', admin.site.urls),
    # # include the built-in auth urls for the built-in views
    # path('accounts/', include('allauth.urls')),
    # path('accounts/', include('django.contrib.auth.urls')),
]