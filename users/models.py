from django.db import models
from django.contrib import admin
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager
from api.models import Event, EventTag

# Create your models here.
class CustomUser(AbstractBaseUser, PermissionsMixin):
  username = None
  email = models.CharField(max_length=254, unique=True)
  name = models.CharField(max_length=50)
  password = models.CharField(max_length=200)
  liked_events = models.ManyToManyField(Event, blank=True)
  fav_tags = models.ManyToManyField(EventTag, blank=True)

  is_staff = models.BooleanField(default=False)
  is_active = models.BooleanField(default=True)
  is_superuser = models.BooleanField(default=False)
  
  USERNAME_FIELD = 'email'
  EMAIL_FIELD = 'email'
  REQUIRED_FIELDS = ['password']

  objects = CustomUserManager()

  # @admin.display
  # def get_liked_events(self):
  #   return str(self.liked_events.set())
  
  # @admin.display
  # def get_fav_tags(self):
  #   return str(self.fav_tags.set())

  def __str__(self):
    return self.email



