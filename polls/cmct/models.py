import datetime

from django.db import models
from django.utils import timezone

from ..users.models import User

app_name = __package__.split('.')[-1]

class Seed(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published')
    seeders = models.IntegerField(default=0)
    # assigned = models.ForeignKey(User, related_name='seed_as', on_delete=models.CASCADE)
    # accepted = models.ForeignKey(User, related_name='seed_ac', on_delete=models.CASCADE)

    def __str__(self):
        return f'Seed - {self.id} accept:{self.seed_ac.count()}'

class Assign(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    seed = models.ForeignKey(Seed, related_name='seed_as', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_as', on_delete=models.CASCADE)
    # users = models.ManyToManyField(User)

    def __str__(self):
        return f'Assign - {self.seed.id}'

class Accept(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    seed = models.ForeignKey(Seed, related_name='seed_ac', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_ac', on_delete=models.CASCADE)
    # users = models.ManyToManyField(User)

    def __str__(self):
        return f'Accept - {self.seed.id}:{self.user.name}'

class Secure(models.Model):
    seed = models.ForeignKey(Seed, related_name='seed_se', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_se', on_delete=models.CASCADE)
    # users = models.ManyToManyField(User)
    status = models.IntegerField(default=0)
    secure_date = models.DateTimeField('date secured')

    def __str__(self):
        return f'Secure - {self.seed.id}'

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
