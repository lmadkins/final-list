from django.shortcuts import render, redirect
from django.http import HttpResponse # #Views
from django.views import View # <- View class to handle requests
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.views.generic.detail import DetailView
#Models
from .models import List
from .models import ListItem
# Auth
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin


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
        context["lists"] = List.objects.filter(user=self.request.user)
        return context

# class ListDetail(DetailView):
#     # model: List
#     model: ListItem
#     template_name: "list_detail.html"

def list_detail(request, id):
    # context={}
    # list = ListItem.objects.get()
    # return render(request, {'list':  list})
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["list"] = List.objects.filter(user=self.request.user)
        return context
#         return render(request,'list_detail.html', {
#         'list': list
# })
        list = List.objects.filter(user=self.request.user)
    item = ListItem.objects.all()
    return render(request, 'list_detail.html', {
        'list': 'list',
        'items': item
})

# class ListCreate(LoginRequiredMixin,  CreateView):
#     model: List
#     fields = ['name', 'details', 'created_at', 'user', 'type']
#     template_name= "list_create.html"

    # def form_valid(self, form):
    # # Assign the logged in user (self.request.user)
    # form.instance.user = self.request.user  # form.instance is the cat
    # # Let the CreateView do its job as usual
    # return super().form_valid(form)


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
