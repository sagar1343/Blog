from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
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
    content = RichTextField(null=True, blank=True)
    read_by = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(
        to=Category, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title

    def read(self):
        self.read_by += 1
        self.save()
