from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.urls import reverse_lazy


class AccountCreateView(CreateView):
    model = User  
    form_class = UserCreationForm
    success_url = reverse_lazy('account:hello_world')
    template_name = "detail.html"
    