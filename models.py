from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=100)
    department=models.CharField(max_length=50)
    position=models.CharField(max_length=50)
    hire_date=models.DateField()
    
    def _str_(self):
        return self.name