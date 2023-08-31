from django.db import models

# Create your models here.
class Week(models.Model):
    week = models.CharField(max_length=10)
        
    def __str__(self) -> str:
        return self.week

class Day(models.Model):
    day = models.CharField(max_length=20)
    week = models.ForeignKey(Week, on_delete=models.PROTECT)
    
    def __str__(self) -> str:
        return self.day

class Meal(models.Model):
    meal = models.TextField()
    day = models.ForeignKey(Day, on_delete=models.PROTECT)
    week = models.ForeignKey(Week, on_delete=models.PROTECT)
    
    class Meta:
        verbose_name_plural = "meals"
    
    def __str__(self) -> str:
        return self.meal
