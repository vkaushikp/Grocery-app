from .models import GroceryItem
from django.contrib.auth.models import User
from bootstrap_modal_forms.forms import BSModalModelForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin


class GroceryItemForm(BSModalModelForm):
    class Meta:
        model = GroceryItem
        exclude = ['created_at', 'updated_at','user','category']

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class RegistrationForm(PopRequestMixin, CreateUpdateAjaxMixin,
                             UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']