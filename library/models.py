from django.db import models

# Create your models here.

class Books(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.CharField(max_length=50)
    pages = models.IntegerField()
    year = models.IntegerField()

class Meta:
        verbose_name_plural = "Books"

def __str__(self):
    return self.title
