def band_detail(req,pk):
    band = Band.objects.get(id=pk)
    invites =  Invite.objects.filter(band=pk)
    members = BandMember.objects.filter(band=pk)
    invites = filter(lambda invite: invite.sender != True,invites)
    context = {"band":band,"invites":invites,"members":members}
    return render(req,'band_detail.html',context)
