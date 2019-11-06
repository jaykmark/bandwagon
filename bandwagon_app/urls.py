from django.urls import path
from . import views

urlpatterns = [
    path('band/<int:pk>/', views.band_detail, name = 'band_detail'),
    path('artist/<int:pk>/', views.artist_detail, name = 'artist_detail'),
    path('', views.artist_list, name = 'artist_list'),
    path('artist/<int:pk>/edit/', views.artist_edit, name = 'artist_edit'),
    path('band/<int:pk>/edit/', views.band_edit, name = 'band_edit'),
    path('artist/<int:pk>/delete/', views.artist_delete, name = 'artist_delete'),
    path('band/<int:pk>/delete/', views.band_delete, name = 'band_delete')
]
