from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from news.models import NewsStory
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.shortcuts import render

# Create your views here.
class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

class ProfileView(generic.DetailView):
    model = CustomUser
    template_name = "users/profile.html"
    context_object_name = 'user'
    # form_class = CustomUserCreationForm
    # success_url = reverse_lazy('profile')
    # template_name = 'users/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.order_by('pub_date')[:4]
        context['all_stories'] = NewsStory.objects.order_by('pub_date')
        return context
    