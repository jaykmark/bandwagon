from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from .models import Artist, Band, BandMember, Invite

from .forms import ArtistForm, BandForm
from django.contrib.auth.decorators import login_required

# Landing
def landing(req):
    return render(req, 'landing.html')

# Profile
def profile(req):  
    if req.user:
        if Artist.objects.filter(user=req.user.id).exists():
            user_artist = Artist.objects.get(user=req.user.id)
            return redirect('artist_detail', pk = user_artist.pk)
        else: 
            return redirect('artist_create')

# Artist Views
def artist_list(req):
    artists = Artist.objects.all()
    context = {"artists":artists}
    return render(req, 'artist_list.html', context)

def artist_detail(req,pk):
    admin = False
    user_bands = None
    if req.user:
        user_artist = Artist.objects.get(user=req.user)
        user_bands = Band.objects.filter(owner = user_artist.id)
        if pk == user_artist.id:
            admin = True
    
    artist = Artist.objects.get(id=pk)
    invites = Invite.objects.filter(artist = pk)
    
    filtered_invites = filter(lambda invite: invite.sender == False,invites)
    print(filtered_invites)
    bands = BandMember.objects.filter(artist=pk)
    context = {"artist":artist,"bands":bands,"user_bands":user_bands, "user_artist":user_artist,"admin":admin,"invites": filtered_invites}
    return render(req, 'artist_detail.html', context)

def artist_create(req):
    if req.method == 'POST':
        form = ArtistForm(req.POST)
        if form.is_valid():
            artist = form.save(commit = False)
            artist.user = req.user
            artist.save()
            return redirect('artist_detail', pk=artist.pk)
    else: 
        form = ArtistForm()
        context = {'form':form, 'header':"Create Artist"}
        return render(req, 'artist_form.html', context)

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

def artist_delete(req, pk):
    Artist.objects.get(id=pk).delete()
    return redirect('artist_list')


# ---------------------- BANDS
def band_list(req):
    bands = Band.objects.all()
    context = {"bands":bands}
    return render(req, 'band_list.html', context)

def band_detail(req,pk):
    band = Band.objects.get(id=pk)
    admin = False
    if band.owner.user == req.user:
        admin = True
    invites =  Invite.objects.filter(band=pk)
    members = BandMember.objects.filter(band=pk)
    desired_members =  band.desired_number - len(members)
    invites = filter(lambda invite: invite.sender == True,invites)
    context = {"band":band,"invites":invites,"members":members,"admin":admin,"desired_members":desired_members}
    return render(req,'band_detail.html',context)

@login_required
def band_create(req):
    if req.method == 'POST':
        form = BandForm(req.POST)
        if form.is_valid():
            band = form.save(commit = False)
            band.owner = Artist.objects.get(user = req.user)
            band.save()
            return redirect('band_detail', pk=band.pk)
    else:
        form = BandForm()
        context = {'form':form, 'header':"Create Band"}
        return render(req, 'band_form.html', context)

@login_required
def band_edit(req, pk):
    band = Band.objects.get(id=pk)
    if req.method == 'POST':
        form = BandForm(req.POST, instance=band)
        if form.is_valid():
            band = form.save()
            return redirect('band_detail.html', pk=pk)
    else:
        form = BandForm(instance=band)
        context = {'form':form, 'header':f"Edit {band.name}"}
        return render(req, 'band_form.html', context)

@login_required
def band_delete(req, pk, band_pk):
    Band.objects.get(id=band_pk).delete()
    return redirect('band_list', pk=pk)


# -------------- Search
def artist_search(req):
    query = req.GET['query']
    print(query)
    artists = Artist.objects.all()
    filtered_artists = []
    for artist in artists:
        if query.lower() in artist.stage_name.lower():
            filtered_artists.append(artist)
    data = serializers.serialize('json',filtered_artists)
    return JsonResponse({"artists":data})

def band_search(req):
    query = req.GET['query']
    print(query)
    bands = Band.objects.all()
    filtered_bands = []
    for band in bands:
        if query.lower() in band.name.lower():
            filtered_bands.append(band)
    data = serializers.serialize('json',filtered_bands)
    return JsonResponse({"bands":data})



# -------------------------------------------- BandMembers and Invites
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
def apply_to_band(req,band_pk):
    invite = Invite()
    invite.band = Band.objects.get(id=band_pk)
    invite.artist = Artist.objects.get(user=req.user.id)
    invite.sender = True
    invite.save()
    return redirect('band_detail',pk=band_pk)

@login_required 
def invite_artist(req,band_pk,artist_pk):
    invite = Invite()
    invite.band = Band.objects.get(id=band_pk)
    invite.artist = Artist.objects.get(id=artist_pk)
    invite.sender = False
    invite.save()
    return redirect('artist_detail',pk=artist_pk)

@login_required
def remove_bandmember(req,band_pk,artist_pk):
    band_member = BandMember.objects.filter(band = band_pk)
    band_member = band_member.filter(artist = artist_pk)
    band_member.delete()
    return redirect('band_detail',pk=band_pk)
# Sender Property: True = Artist; False = Band
