from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from .models import Pozitie, JobUser
from django.db.models import Q


# Create your views here.
def home_page_view(request):
    return render(request, 'index.html', {})


# class PozitiiListView(ListView):
#     model = Pozitie
#     template_name = 'pozitii_list.html'
#     context_object_name = "context1"

def pozitii_list_view(request):
    return render(request, 'pozitii_list.html', {'toate_pozitiile': Pozitie.objects.all(), 'pozitii_promovate': Pozitie.objects.filter(promovat = True)[0:4]})


class PozitiiDetailView(DetailView):
    model = Pozitie
    template_name = "pozitii_detalii.html"
    context_object_name = "context2"
    pk_url_kwarg = 'id'


class PozitiiCreateView(LoginRequiredMixin, CreateView):
    model = Pozitie
    template_name = 'pozitie_create.html'
    fields = '__all__'
    success_url = reverse_lazy('pozitii_list_view')  # reverse lazy primeste numele url-ului si redirecteaza catre el

class PozitieUpdateView(LoginRequiredMixin, UpdateView):
    model = Pozitie
    # itt azt mondjuk el hogy a modositashoz kell a can_edit permission a pages applikaciohoz.
    # Az adminban allitjuk be majd a jogokat. Az osztlay kell orokolje a PermissionRequiredMixin osztalyt is es az kell elol legyen.
    template_name = 'pozitie_update.html'
    fields = '__all__'
    success_url = reverse_lazy('pozitii_list_view')

class PozitieDeleteView(LoginRequiredMixin, DeleteView):
    model = Pozitie
    template_name = 'pozitie_delete.html'
    context_object_name = "context3"
    fields = '__all__'
    success_url = reverse_lazy('pozitii_list_view')

# def my_form(request):
#
#     if request.method == 'POST':
#         form = Pozitie(request.POST)
#         context = {'form': form}
#         if form.is_valid():
#             form.save()
#             return render(request, 'pozitii_list.html', context)
#         return render(request, 'pozitie_create.html', context)


def my_form(request):
    if request.method == 'POST':
        form = Pozitie(request.POST)
        context = {'form': form}
        form.save()
        return render(request, 'pozitii_list.html', context)

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        linkedin_profile = request.POST.get('linkedin_profile')
        if not username:
            return render(request, 'signup_warning.html', {})
        if not email:
            return render(request, 'signup_warning.html', {})
        if not password:
            return render(request, 'signup_warning.html', {})
        if not linkedin_profile:
            return render(request, 'signup_warning.html', {})
        if "https://www.linkedin.com/" not in linkedin_profile:
            return render(request, 'linkedin_warning.html', {})
        if "@" not in email:
            return render(request, 'email_warning')
        if len(password) < 6:
            return render(request, 'password_warning')


        user = User.objects.create(username=username, email=email, password = password)
        JobUser.objects.create(user = user, linkedin_profile=linkedin_profile)
        return render(request, 'index.html', {})
    return render(request, 'signup.html', {})



# def search_view(request):
#     ultima_pozitie = Pozitie.objects.all()
#     query = request.GET.get('q')
#     print(query)
#     if query:
#         ultima_pozitie = Pozitie.objects.filter(denumirea_pozitiei__contains=query)
#     context = {'ultima_pozitie': ultima_pozitie,}
#     return render(request, 'results.html', context)
#     # return render(request, 'results.html')

class SearchResultsView(ListView):
    model = Pozitie
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Pozitie.objects.filter(Q(denumirea_pozitiei__icontains=query) | Q(descrierea_jobului__icontains=query)|
        Q(locatie__icontains=query) | Q(companie__icontains=query))
        return object_list
    # def get_queryset(self):
    #     return Pozitie.objects.filter(
    #         Q(denumirea_pozitiei__icontains='Backend') | Q(descrierea_jobului__icontains='candidat')
    #     )