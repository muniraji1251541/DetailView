from django.db import models
from django.urls import reverse

# Create your models here.

class Trainer(models.Model):
    name=models.CharField(max_length=50)
    sub=models.CharField(max_length=50)
    inst=models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def det_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})
    

class Student(models.Model):
    name=models.CharField(max_length=50)
    age=models.PositiveIntegerField()
    tri=models.ForeignKey(Trainer,on_delete=models.CASCADE,related_name='students')

    def __str__(self):
        return self.name