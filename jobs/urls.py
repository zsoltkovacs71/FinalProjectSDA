from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.home_page_view, name='home'),
    path('pozitii/', views.pozitii_list_view, name='pozitii_list_view'),
    path('pozitii_detalii/<int:id>', views.PozitiiDetailView.as_view(), name='pozitii_detalii_view'),
    path('pozitii_create/', views.PozitiiCreateView.as_view(), name='pozitii_create_view'),
    path('pozitii_delete/<int:pk>', views.PozitieDeleteView.as_view(), name='pozitie_delete_view'),
    path('pozitii_update/<int:pk>', views.PozitieUpdateView.as_view(), name='pozitie_update_view'),
    path('signup/', views.signup, name='signup'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
]
