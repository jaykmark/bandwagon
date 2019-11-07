from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from .models import Artist, Band, BandMember, Invite

from .forms import ArtistForm, BandForm
from django.contrib.auth.decorators import login_required
# -------------------  BAND ------------------- #

# Detail

def band_detail(req,pk):
    band = Band.objects.get(id=pk)
    invites =  Invite.objects.filter(band=pk)
    members = BandMember.objects.filter(band=pk)
    invites = filter(lambda invite: invite.sender != True,invites)
    context = {"band":band,"invites":invites,"members":members}
    return render(req,'band_detail.html',context)


def artist_detail(req,pk):
    artist = Artist.objects.get(id=pk)
    context = {"artist":artist}
    return render(req, 'artist_detail.html', context)

# -------- LISTS ---------- #

def band_list(req):
    bands = Band.artist.all()
    context = {"bands":bands}
    return render(req, 'band_list.html', context)

# Create
@login_required
def band_create(req):
    if req.method == 'POST':
        form = BandForm(req.POST)
        if form.is_valid():
            band = form.save(commit = False)
            band.owner = Artist.objects.get(user = req.user)
            band.save()
            return redirect('band_list.html', pk=band.pk)
    else:
        form = BandForm()
        context = {'form':form, 'header':"Add New Band"}
        return render(req, 'band_form.html', context)

# Update

def band_edit(req, pk, band_pk):
    band = Band.objects.get(id=band_pk)
    if req.method == 'POST':
        form = BandForm(req.POST, instance=band)
        if form.is_valid():
            band = form.save()
            return redirect('band_detail.html', pk=band.pk)
    else:
        form = BandForm(instance=band)
        context = {'form':form, 'header':f"Edit {band.name}"}
        return render(req, 'band_form.html', context)

# Delete

def band_delete(req, pk, band_pk):
    Band.objects.get(id=band_pk).delete()
    return redirect('band_list', pk=pk)

# ------------------- Artist -------------------- #

# Detail

def artist_detail(req,pk):
    artist = Artist.objects.get(id=pk)
    context = {"artist":artist}
    return render(req, 'artist_detail.html', context)

# List

def artist_list(req):
    artists = Artist.objects.all()
    context = {"artists":artists}
    return render(req, 'artist_list.html', context)

# Create

def artist_create(req):
    artist = Artist.objects.get(id=req.user.id)
    if req.method == 'POST':
        form = ArtistForm(req.POST,instance = artist)
        if form.is_valid():
            artist = form.save(commit = False)
            artist.user = req.user
            artist.save()
            return redirect('artist_detail', pk=artist.pk)
    else:
       
        if artist is not None:
            form = ArtistForm(instance = artist)
        else:
            form = ArtistForm()
        context = {'form':form, 'header':"Add New Artist"}
        return render(req, 'artist_form.html', context)

# Update


def artist_edit(req, pk):
    artist = Artist.objects.get(id=pk)
    if req.method == 'POST':
        form = ArtistForm(req.POST, instance=artist)
        if form.is_valid():
            artist = form.save()
            return redirect('artist_detail', pk=artist.pk)
    else:
        form = ArtistForm(instance=artist)
        context = {'form':form, 'header':f"Edit {artist.stage_name}"}
        return render(req, 'artist_form.html', context)

# Delete

def artist_delete(req, pk):
    Artist.objects.get(id=pk).delete()
    return redirect('artist_list')

# -------------------------------------------- INVITES
@login_required
def add_bandmember(req,invite_pk):
    invite = Invite.objects.get(id=invite_pk)
    member = BandMember()
    member.artist = invite.artist
    member.band = invite.band
    member.save()
    invite.delete()
    return redirect('band_detail',pk=invite.band.id)
    
@login_required
def decline_invite(req,invite_pk):
     invite = Invite.objects.get(id=invite_pk)
     band_id = invite.band.id
     invite.delete()
     return redirect('band_detail',pk=band_id)

@login_required
def createInvite(req,band_pk,sender):

# Sender Property: True = Artist; False = Band
  