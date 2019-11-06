from django.contrib import admin

from .models import Artist, Band, BandMember, Invite

# Register your models here.
admin.site.register(Artist)
admin.site.register(Band)
admin.site.register(BandMember)
admin.site.register(Invite)