from django.db import models

from django.utils import timezone


# Create your models here.
class News(models.Model):
    headline=models.TextField()
    description=models.TextField()
    image=models.ImageField(null=True,blank=True,upload_to="images/")
    category=models.CharField(max_length=20,choices=[
        ('sports', 'sports'),
        ('entertainment', 'entertainment'),
        ('politics', 'politics'),
        ('currentaffair', 'currentaffair'),
    ])
    date=models.DateField(default=timezone.now())
    author=models.CharField(max_length=30,null=True,blank=True)
    fulldescription=models.TextField(null=True,blank=True)
