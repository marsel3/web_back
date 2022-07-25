from django.urls import path
from . import views


urlpatterns = [
    path('', views.WebCatalog.as_view(), name='home'),
    path('catalog/', views.catalog, name='catalog'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('catalog/<slug:catalog_id>/', views.WebTovars.as_view(), name='catalog'),
    path('catalog/<slug:catalog_id>/<slug:tov_id>/', views.tovar_card, name='tovar'),
]

