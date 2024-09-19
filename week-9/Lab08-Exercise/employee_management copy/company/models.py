# company/models.py
from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=155)
    manager_id = models.IntegerField(null=True) # Change from ForeignKey to IntegerField

    class Meta:
        unique_together = ["id", "manager_id"] # Add unique contraint เพราะต้องการให้ employee 1 คนเป็น manager ได้ department เดียวเท่านั้น
    
    
class Position(models.Model):
    name = models.CharField(max_length=155)
    description = models.TextField(null=True, blank=True)
    department = models.ForeignKey(
        "company.Department",
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )
    
    def __str__(self):
        return str(self.name)