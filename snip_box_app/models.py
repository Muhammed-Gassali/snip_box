from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tag(models.Model):
    # the title should be unique
    title = models.CharField(max_length=500,unique=True)

class ShortNote(models.Model):
    # foreign key relation to tag model
    tag_relation = models.ForeignKey(Tag,on_delete=models.CASCADE)
    # foreign key relation to default user model
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    # The note field should be assigned as a text field since it has no length limitation
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

