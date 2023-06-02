from django.db import models

# Create your models here.
class student(models.Model):
    FirstName=models.CharField(max_length=30)
    LastName=models.CharField(max_length=30)
    Course=models.CharField(max_length=30)
    Percentage=models.IntegerField()

    def __str__(self):
        return self.FirstName+""+self.LastName
