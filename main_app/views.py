from django.shortcuts import render, redirect
from django.http import HttpResponse # #Views
from django.views import View # <- View class to handle requests
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
#Models
from .models import List

# Auth
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User



# Create your views here.

# Here we will be creating a class called Home and extending it from the View class
class Home(TemplateView):
    template_name = "home.html"
    # Here we are adding a method that will be ran when we are dealing with a GET request
    # def get(self, request):
    #     # Here we are returning a generic response
    #     # This is similar to response.send() in express
    #     return HttpResponse("Home")

@method_decorator(login_required, name='dispatch')
class ListsList(TemplateView):
    template_name = "lists_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["list"] = List.objects.filter(user=self.request.user)
# def lists_index(request):
#     lists = List.objects.all()
    # lists = List.objects.filter(user=self.request.user)
        # 
        return context

class ListCreate(CreateView, LoginRequiredMixin):
    model: List
    fields = '__all__'
    template_name= "list_create.html"
    success_url = "/lists/"
    # def form_valid(self, form):
    # # Assign the logged in user (self.request.user)
    # form.instance.user = self.request.user  # form.instance is the cat
    # # Let the CreateView do its job as usual
    # return super().form_valid(form)

