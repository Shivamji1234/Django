from django.db import models



# Create your models here.


class feedback(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    details=models.CharField(max_length=600,default='SOME STRING')
    date=models.DateField()
    
    def __str__(self):
        return self.name
