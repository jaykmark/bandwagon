from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name = 'landing'),
    path('profile/', views.profile, name = 'profile'),

    path('artists/', views.artist_list, name = 'artist_list'),
    path('artists/search/',views.artist_search, name = 'artist_search'),
    path('artists/new/', views.artist_create, name = 'artist_create'),
    path('artists/<int:pk>/', views.artist_detail, name = 'artist_detail'),
    path('artists/<int:pk>/edit/', views.artist_edit, name = 'artist_edit'),
    path('artists/<int:pk>/delete/', views.artist_delete, name = 'artist_delete'),

    path('bands/',views.band_list,name='band_list'),
    path('bands/search',views.band_search,name='band_search'),
    path('bands/new/', views.band_create, name = 'band_create'),
    path('bands/<int:pk>/', views.band_detail, name = 'band_detail'),
    path('bands/<int:pk>/edit/', views.band_edit, name = 'band_edit'),
    path('bands/<int:pk>/delete/', views.band_delete, name = 'band_delete'),
    
    path('api/v1/invite/apply/<int:band_pk>',views.apply_to_band,name='apply_to_band'),
    path('api/v1/invite/new/<int:band_pk>/<int:artist_pk>',views.invite_artist,name='invite_artist'),
    path('api/v1/invite/<int:invite_pk>/confirm',views.add_bandmember,name='add_bandmember'),
    path('api/v1/invite/<int:invite_pk>/decline',views.decline_invite,name='decline_invite'),
    path('api/v1/bandmembers/remove/<int:band_pk>/<int:artist_pk>',views.remove_bandmember,name='remove_bandmember')
]
