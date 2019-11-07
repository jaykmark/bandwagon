from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Artist(models.Model):
  first_name = models.CharField(max_length = 50)
  last_name = models.CharField(max_length = 50)
  stage_name = models.CharField(max_length = 100)
  description = models.TextField()
  photo_url = models.TextField()
  zip_code = models.CharField(max_length = 5)
  user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'artist_detail')

  def __str__(self):
    return self.stage_name


class Band(models.Model):
  name = models.CharField(max_length = 100)
  description = models.TextField()
  photo_url = models.TextField()
  zip_code = models.CharField(max_length = 5)
  desired_number = models.PositiveIntegerField()
  owner = models.ForeignKey(Artist, on_delete = models.CASCADE, related_name = 'bands')

  def __str__(self):
    return self.name


class BandMember(models.Model):
  band = models.ForeignKey(Band, on_delete = models.CASCADE, related_name = 'members')
  artist = models.ForeignKey(Artist, on_delete = models.CASCADE)

  def __str__(self):
    return f'{self.band} - {self.artist}'


class Invite(models.Model):
  band = models.ForeignKey(Band, on_delete = models.CASCADE, related_name = 'invites')
  artist = models.ForeignKey(Artist, on_delete = models.CASCADE, related_name = 'applications')
  confirmation = models.BooleanField(default = False)
  # Sender Property: True = Artist; False = Band
  sender = models.BooleanField()

  def __str__(self):
    return f'{f"{self.artist.stage_name} --> {self.band.name}" if self.sender == True else f"{self.band.name} --> {self.artist.stage_name}"} confirmed = {self.confirmation}'

