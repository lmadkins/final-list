from django.shortcuts import render, redirect
from django.http import HttpResponse # #Views
from django.views import View # <- View class to handle requests
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin


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