from django.db import models

# Create your models here.
class EventTag(models.Model):
  name = models.CharField(max_length=100)
  
  def __str__(self) -> str:
    return self.name


class EventType(models.Model):
  name = models.CharField(max_length=100)

  def __str__(self) -> str:
    return self.name



class Event(models.Model):
  name = models.CharField(max_length=200)
  description = models.CharField(max_length=500, null=True, blank=True)
  date = models.DateField(auto_now=False, auto_now_add=False)
  ticket_price = models.IntegerField(default=0)
  address = models.CharField(max_length=100, null=True, blank=True)
  likes = models.IntegerField(default=0)

  tags = models.ManyToManyField(EventTag, blank=True)
  type = models.ForeignKey(EventType, on_delete=models.CASCADE, null=True, blank=True)

  def __str__(self) -> str:
    return self.name

