from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    gender_choices = (
        ('M','Male'),
        ('F','Female')
    )

    first_name = models.CharField(max_length=100,default='User_first_name')
    last_name = models.CharField(max_length=100,default='user_last_name')
    age = models.IntegerField(default=18)
    gender = models.CharField(choices=gender_choices,max_length=6)
    
class Retro (models.Model):
    team_choices = (
        ('Front-end','Front-end'),
        ('Back-end','Back-end'),
        ('Product','Product'),
        ('Support','Support'),
        ('Sale','Sale'),
        ('Managers','Managers')
    )
    person = models.ForeignKey(Profile,on_delete=models.CASCADE)
    position = models.CharField(choices=team_choices,max_length=10)
    Sprint_Number = models.IntegerField ()
    retro_date = models.DateTimeField (default=timezone.now)

    # class Meta :
    #     def __str__(self):
    #         return self.person

class RetroNote (models.Model):
    vote_choices = (
        ('Agree','Agree'),
        ('Disagree','Disagree')
    )

    retro = models.ForeignKey(Retro,on_delete=models.CASCADE,default=0)
    likes = models.TextField (max_length=250)
    learns = models.TextField(max_length=250)
    lacks = models.TextField(max_length=250)
    mad = models.TextField(max_length=250)
    glad = models.TextField(max_length=250)
    sad = models.TextField(max_length=250)
    vote = models.CharField(choices=vote_choices,max_length=10)