from django.contrib.auth import views
# from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView
from accounts.forms import CustomLoginForm

urlpatterns = [
    path('signup/', views.Signup.as_view(), name="signup"),
    path('login/', views.LoginView.as_view( authentication_form=CustomLoginForm), name="login"),
    path('', include('allauth.urls')),
    path('', include('django.contrib.auth.urls')),
    # path("password_reset/", views.password_reset_request, name="password_reset"),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
    # template_name="admin/accounts/password/password_reset_confirm.html"), name='password_reset_confirm'),
    # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
    # template_name='admin/accounts/password/password_reset_done.html'), name='password_reset_done'),
    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
    # template_name='admin/accounts/password/password_reset_complete.html'), name='password_reset_complete'),
    # path('password-reset/', views.PasswordResetView.as_view(), name='password_reset'),path('password-reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # path('admin/', admin.site.urls),
    # # include the built-in auth urls for the built-in views
    # path('accounts/', include('allauth.urls')),
    # path('accounts/', include('django.contrib.auth.urls')),
    # path(
    #     'change_password/',
    #     auth_views.PasswordChangeView.as_view(
    #         template_name='/change_password.html',
    #         success_url = '/'
    #     ),
    #     name='change_password'
    # ),
    # path('password_reset/',
    #      auth_views.PasswordResetView.as_view(
    #          template_name='password_reset.html',
    #          subject_template_name='password_reset_subject.txt',
    #          email_template_name='password_reset_email.html',
    #          # success_url='/login/'
    #      ),
    #      name='password_reset'),
    # path('password_reset_done/',
    #      auth_views.PasswordResetDoneView.as_view(
    #          template_name='password_reset_done.html'
    #      ),
    #      name='password_reset_done'),
    # path('password-reset-confirm/<uidb64>/<token>/',
    #      auth_views.PasswordResetConfirmView.as_view(
    #          template_name='password_reset_confirm.html'
    #      ),
    #      name='password_reset_confirm'),
    # path('password-reset-complete/',
    #      auth_views.PasswordResetCompleteView.as_view(
    #          template_name='password_reset_complete.html'
    #      ),
    #      name='password_reset_complete'),
]