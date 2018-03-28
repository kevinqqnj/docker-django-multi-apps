from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_('Name of User'), blank=True, max_length=255)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})

class Forum(models.Model):
    name = models.CharField(_('Name of Forum'), blank=False, max_length=16)
    sync_status = models.CharField(default='ready', max_length=100)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name

class Report(models.Model):
    user = models.ForeignKey(User, related_name='Forum_user', on_delete=models.CASCADE)
    forum = models.ForeignKey(Forum, related_name='Forum_name', on_delete=models.CASCADE)
    id_in_forum = models.IntegerField(default=0)
    max_cap = models.IntegerField(default=0) # TB
    assigned_cap = models.FloatField(default=0)
    accept_cap = models.FloatField(default=0)
    salary = models.IntegerField(default=0)
    # leeching_seeding
    # doublesalary

    def __str__(self):
        return f'{self.forum.name} - {self.user.name}'

