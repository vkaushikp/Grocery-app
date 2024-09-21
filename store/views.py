from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.generic import ListView
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView, BSModalLoginView, BSModalReadView, BSModalDeleteView, BSModalFormView
from .forms import GroceryItemForm, LoginForm, RegistrationForm
from django.urls import reverse_lazy
from .serializers import GrocerySerializer
from .models import GroceryItem
from .utils import generate_category
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
import logging

logger = logging.getLogger(__name__)

class RegistrationView(BSModalCreateView):
    form_class = RegistrationForm
    template_name = 'registration.html'
    success_message = 'Success: You were successfully registered.'
    success_url = reverse_lazy('index')

class LoginView(BSModalLoginView):
    model = User
    template_name = 'login.html'
    form_class = LoginForm
    success_message = 'Success: You were successfully logged in.'
    extra_context = dict(success_url=reverse_lazy('index'))

class GroceryItemCreateView(BSModalCreateView):
    model = GroceryItem
    template_name = 'create_grc.html'
    form_class = GroceryItemForm
    success_message = 'Success: Grocery Item was created.'
    success_url = reverse_lazy('index')
    serializer_class = GrocerySerializer

    def form_valid(self, form):
        if GroceryItem.objects.filter(name=form.instance.name, user=self.request.user).exists():
            messages.error(self.request, 'This item already exists.', 'danger')
            self.request.session['form_data'] = form.data
            return redirect('index')
        form.instance.user = self.request.user
        form.instance.category = generate_category(form.instance.name)
        serializer = self.serializer_class(form.instance)
        print(serializer.data)
        return super().form_valid(form)

class UpdateGroceryItemView(BSModalUpdateView):
    model = GroceryItem
    template_name = 'update_grc.html'
    form_class = GroceryItemForm
    success_message = 'Success: Grocery Item was updated.'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        if GroceryItem.objects.filter(name=form.instance.name, user=self.request.user).exists():
            messages.error(self.request, 'This item already exists.', 'danger')
            self.request.session['form_data'] = form.data
            return redirect('index')
        return super().form_valid(form)

class ViewGroceryItemView(BSModalReadView):
    model = GroceryItem
    template_name = 'view_grc.html'
    context_object_name = 'item'

class DeleteGroceryItemView(BSModalDeleteView):
    model = GroceryItem
    template_name = 'delete_grc.html'
    success_message = 'Success: Grocery Item was deleted.'
    success_url = reverse_lazy('index')

class IndexView(ListView):
    model = GroceryItem
    template_name = 'index.html'
    context_object_name = 'grocery_items'

    def get_queryset(self):
        return GroceryItem.objects.filter(user=self.request.user)
    
def logout_view(request):
    logout(request)
    return redirect('login')
