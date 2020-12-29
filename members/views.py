from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import SignUpFrom

# Create your views here.
class UserRegisterView(generic.CreateView):
    form_class = SignUpFrom
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
  
 #class UserEditView(generic.CreateView):
    #form_class = UserChangeForm
    #template_name = 'registration/edit_profile.html'
    #success_url = reverse_lazy('home')