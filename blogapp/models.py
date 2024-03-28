from django.db import models
from django.contrib.auth.models import AbstractUser
from django_ckeditor_5.fields import CKEditor5Field
# Create your models here.


class Author(AbstractUser):
    profile_image = models.ImageField(
        upload_to='profile_image/', default='profile_image/default__person.jpg')


class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title


class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(
        to=Author, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=200)
    content = CKEditor5Field('Content', config_name='extends', blank=True)
    read_by = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(
        to=Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def read(self):
        self.read_by += 1
        self.save()
