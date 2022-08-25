from django.shortcuts import render, redirect
from django.http import HttpResponse # #Views
from django.views import View # <- View class to handle requests

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView

from django.utils.decorators import method_decorator

from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# from django.conf import settings
# from django.contrib.auth.forms import PasswordResetForm
# from django.contrib.auth.models import User
# from django.contrib.auth.tokens import default_token_generator
# from django.core.mail import BadHeaderError, send_mail
# from django.db.models import Q
# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from django.template.loader import render_to_string
# from django.utils.encoding import force_bytes
# from django.utils.http import urlsafe_base64_encode


# Create your views here.
class Signup(View):
    template_name= "registration/signup.html"
    # show a form to fill out
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    # on form submit, validate the form and login the user.
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("lists_list")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)

def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/lists/')
    return render_to_response('login.html', context_instance=RequestContext(request))

# class Login(View):
#     template_name= "registration/login.html"
#     # show a form to fill out
#     def get(self, request):
#         form = CustomLoginForm()
#         context = {"form": form}
#         return render(request, "registration/login.html", context)
#     # on form submit, validate the form and login the user.
#     def post(self, request):
#         form = CustomLoginForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect("lists_list")
#         else:
#             context = {"form": form}
#             return render(request, "registration/login.html", context)


# def password_reset_request(request):
#     if request.method == "POST":
#         domain = request.headers['Host']
#         password_reset_form = PasswordResetForm(request.POST)
#         if password_reset_form.is_valid():
#             data = password_reset_form.cleaned_data['email']
#             associated_users = User.objects.filter(Q(email=data))
#             # You can use more than one way like this for resetting the password.
#             # ...filter(Q(email=data) | Q(username=data))
#             # but with this you may need to change the password_reset form as well.
#             if associated_users.exists():
#                 for user in associated_users:
#                     subject = "Password Reset Requested"
#                     email_template_name = "admin/accounts/password/password_reset_email.txt"
#                     c = {
#                         "email": user.email,
#                         'domain': domain,
#                         'site_name': 'Interface',
#                         "uid": urlsafe_base64_encode(force_bytes(user.pk)),
#                         "user": user,
#                         'token': default_token_generator.make_token(user),
#                         'protocol': 'http',
#                     }
#                     email = render_to_string(email_template_name, c)
#                     try:
#                         send_mail(subject, email, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)
#                     except BadHeaderError:
#                         return HttpResponse('Invalid header found.')
#                     return redirect("/core/password_reset/done/")
#     password_reset_form = PasswordResetForm()
#     return render(request=request, template_name="admin/accounts/password/password_reset.html",
#                   context={"password_reset_form": password_reset_form})
 