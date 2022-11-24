from django.db import models

class details(models.Model):
    email= models.CharField(max_length=300, unique=True)
    password= models.TextField()
    phone=models.TextField()
    def __str__(self):
        return self.email
    

# Create your models here.
