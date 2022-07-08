from django.db import models
from django.contrib.auth.models import User
# Create your models here.

'''class workoutTable(models.Model):
    CATEGORY = (
        ("chest", "Chest"),
        ("shoulder", "Shoulder"),
        ("legs", "Legs"),
    )
    
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    desc = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.category'''
    
class itemTable(models.Model):
    
    #category = models.ForeignKey(workoutTable, null=True, on_delete=models.CASCADE)
    exercise = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.exercise
    
class planTable(models.Model):
    
    DAYS = (
        ("sunday", "sunday"),
        ("monday", "monday"),
        ("tuesday", "tuesday"),
        ("wednesday", "wednesday"),
        ("thursday", "thursday"),
        ("friday", "friday"),
    )
    #big_id = models.BigAutoField(primary_key = True)
    day = models.CharField(null=True, max_length=10, choices=DAYS)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    #category = models.ForeignKey(workoutTable, null=True, on_delete=models.CASCADE)
    exercise = models.ForeignKey(itemTable, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.day
