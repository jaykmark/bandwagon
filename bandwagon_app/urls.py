from django.urls import path
from . import views

urlpatterns = [
    path('bands/<int:pk>/', views.band_detail, name = 'band_detail'),
    path('artists/<int:pk>/', views.artist_detail, name = 'artist_detail'),
    path('', views.artist_list, name = 'artist_list'),
    path('artists/<int:pk>/edit/', views.artist_edit, name = 'artist_edit'),
    path('bands/<int:pk>/edit/', views.band_edit, name = 'band_edit'),
    path('artists/<int:pk>/delete/', views.artist_delete, name = 'artist_delete'),
    path('bands/<int:pk>/delete/', views.band_delete, name = 'band_delete'),
    path('artists/new', views.artist_create, name = 'artist_create'),
    path('bands/new', views.band_create, name = 'band_create'),
    path('api/v1/invite/<int:invite_pk>/confirm',views.add_bandmember,name='add_bandmember'),
    path('api/v1/invite/<int:invite_pk>/decline',views.decline_invite,name='decline_invite')
]
