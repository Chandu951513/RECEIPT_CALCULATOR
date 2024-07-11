from django.db import models

# Create your models here.
class ammount(models.Model):
    basic_ammount=models.CharField(max_length=10)
    saving_amount=models.CharField(max_length=10)
    ammount_saved=models.CharField(max_length=100)
    result_amount=models.CharField(max_length=100)
    
