from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView, \
    TemplateView
from .models import Weapon


class AllWeaponsView(ListView):
    """Предстовление вывода всего оружия"""
    model = Weapon
    template_name = 'index.html'
    paginate_by = 5


class WeaponDetailView(DetailView):
    """Предстовление вывода оружия по id"""
    model = Weapon
    template_name = 'weapons/weapon_detail.html'


class Contact(TemplateView):
    template_name = 'contact.html'
