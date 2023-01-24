from django.urls import path, include
from . import views
from django_registration.backends.activation.views import RegistrationView
from .forms import AppRegistrationForm

urlpatterns = [
    path('register/', RegistrationView.as_view(form_class=AppRegistrationForm), name="django_registration_register"),
    path('', include("django_registration.backends.activation.urls")),
    path('', include("django.contrib.auth.urls")),
    path('profile/', views.profile, name="profile"),

]