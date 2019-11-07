from django import forms
from .models import Band, Artist

class ArtistForm(forms.ModelForm):
    
    class Meta:
        model = Artist
        fields = ('first_name', 'last_name', 'stage_name','description','photo_url','zip_code')


class BandForm(forms.ModelForm):

    class Meta:
        model = Band
        fields = ('name','description','photo_url','zip_code','desired_number')



