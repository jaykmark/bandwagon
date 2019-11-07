from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from .models import Artist, Band

from .forms import ArtistForm, BandForm

# -------------------  BAND ------------------- #

# Detail

def band_detail(req,pk):
    band = Band.objects.get(id=pk)
    invites =  Invite.objects.filter(band=pk)
    members = BandMember.objects.filter(band=pk)
    invites = filter(lambda invite: invite.sender != True,invites)
    context = {"band":band,"invites":invites,"members":members}
    return render(req,'band_detail.html',context)

<<<<<<< HEAD

def artist_detail(request,pk):
    artist = Artist.objects.get(id=pk)
    context = {"artist":artist}
    return render(request, 'artist_detail.html', context)

# -------- LISTS ---------- #
=======
# List
>>>>>>> 6c26bd01a1b7e16fa13df366ffc117cd057676fd

def band_list(request):
    bands = Band.artist.all()
    context = {"bands":bands}
    return render(request, 'artist_list.html', context)

# Create

def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save(commit = False)
            band.owner = Artist.objects.get(user = request.user)
            band.save()
            return redirect('band_list.html', pk=band.pk)
    else:
        form = BandForm()
        context = {'form':form, 'header':"Add New Band"}
        return render(request, 'band_form.html', context)

# Update

def band_edit(request, pk, band_pk):
    band = Band.objects.get(id=band_pk)
    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            band = form.save()
            return redirect('band_detail.html', pk=band.pk)
    else:
        form = BandForm(instance=band)
        context = {'form':form, 'header':f"Edit {band.name}"}
        return render(request, 'band_form.html', context)

# Delete

def band_delete(request, pk, band_pk):
    Band.objects.get(id=band_pk).delete()
    return redirect('band_list', pk=pk)

# ------------------- Artist -------------------- #

# Detail

def artist_detail(request,pk):
    artist = Artist.objects.get(id=pk)
    context = {"artist":artist}
    return render(request, 'artist_detail.html', context)

# List

def artist_list(request):
    artists = Artist.objects.all()
    context = {"artists":artists}
    return render(request, 'artist_list.html', context)

# Create

def artist_create(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            artist = form.save(commit = False)
            artist.user = request.user
            artist.save()
            return redirect('artist_detail', pk=artist.pk)
    else:
        form = ArtistForm()
        context = {'form':form, 'header':"Add New Artist"}
        return render(request, 'artist_form.html', context)

# Update

def artist_edit(request, pk):
    artist = Artist.objects.get(id=pk)
    if request.method == 'POST':
        form = ArtistForm(request.POST, instance=artist)
        if form.is_valid():
            artist = form.save()
            return redirect('artist_detail', pk=artist.pk)
    else:
        form = ArtistForm(instance=artist)
        context = {'form':form, 'header':f"Edit {artist.stage_name}"}
        return render(request, 'artist_form.html', context)

# Delete

def artist_delete(request, pk):
    Artist.objects.get(id=pk).delete()
    return redirect('artist_list')
