from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from .models import Artist, Band
# Create your views here.
def band_detail(req,pk):
    band = Band.objects.get(id=pk)
    context = {"band":band}
    return render(req,'band_detail.html',context)
