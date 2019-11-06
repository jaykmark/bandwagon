from django.urls import path
from . import views

urlpatterns = [
    path('band/<int:pk>', views.band_detail, name = 'show_band'),
]
