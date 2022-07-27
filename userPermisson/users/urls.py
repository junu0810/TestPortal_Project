from django.urls import path
from .views import AccountCreateView, hello_world


urlpatterns = [
    path('hello_world', hello_world, name='hello_world'),
    path('create/', AccountCreateView.as_view(), name='create'),  # class엔 as_view()를 붙여주어야 한다.
    path('login/', LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),
]