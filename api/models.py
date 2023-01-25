from django.db import models

# Create your models here.
class Event(models.Model):
  name = models.CharField(max_length=200)
  date = models.DateField(auto_now=False, auto_now_add=False)
  ticket_price = models.IntegerField(default=0)
  address = models.CharField(max_length=100)
  likes = models.IntegerField(default=0)

  def __str__(self):
    return self.name

