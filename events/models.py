from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Volunteer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=200, null=True, blank=True)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    user_rank = models.IntegerField(default=0)
    user_points = models.IntegerField(default = 0)
    user_coins = models.IntegerField(default = 0)
    user_icon = models.ImageField(default='profile1.png', null=True, blank=True)
    user_datecreated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.user_name is not None:

            return self.user_name
        else:
            return "default"

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    TYPE = ('Event', 'Event'), ('Story', 'Story')

    content_name = models.CharField(max_length=200, null=True)
    content_author = models.ForeignKey(Volunteer, null=True, on_delete=models.SET_NULL)
    content_date = models.DateTimeField(auto_now_add=True)
    content_date_start = models.DateTimeField(null=True, blank=True)
    content_date_end = models.DateTimeField(null=True, blank=True)
    content_social_description = models.CharField(max_length=1000, null=True)
    content_image = models.ImageField(default='profile1.png', null=True, blank=True)
    tags = models.ManyToManyField(Tag)
    full_story = models.CharField(max_length=10000, null=True, blank=True)
    post_type = models.CharField(max_length=200, null=True, choices=TYPE)
    attending = models.ManyToManyField(User)
    


    def __str__(self):
        return self.content_name



class Comment(models.Model):
    message = models.CharField(max_length=300, null=True)
    author = models.ForeignKey(Volunteer, null=True, on_delete=models.CASCADE)
    post = models.ManyToManyField(Post)

