from django.db import models

# Create your models here.
class Contact(models.Model):
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    email=models.EmailField()
    number=models.IntegerField(max_length=12)
    message=models.CharField(max_length=1000)
    def __str__(self):
        return self.firstname

