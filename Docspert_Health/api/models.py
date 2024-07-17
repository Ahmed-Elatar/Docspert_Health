from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
import uuid







class CsvFiles(models.Model):


    file = models.FileField(upload_to='Csv_files/' ,blank=True)
    
    uploaded = models.DateTimeField(auto_now_add=True)
    auth=models.ForeignKey(User,on_delete=models.PROTECT)


    class Meta:
        ordering = ['-uploaded']
        indexes = [
        models.Index(fields=['-uploaded']),
        ]


    def __str__(self):
        return self.file.name
    

class Account(models.Model):

    id=models.UUIDField(primary_key=True , default=uuid.uuid4, editable=False)
    name = models.CharField()
    
    balance = models.DecimalField( max_digits = 10 , decimal_places=2)

    class Meta:
        ordering = ['name']
        indexes = [
        models.Index(fields=['name']),
        ]


    def __str__(self):
        return self.name
    

    

class Transfer(models.Model):


    accounts_from = models.ForeignKey(Account, related_name='transfers_from', on_delete=models.PROTECT)
    accounts_to = models.ForeignKey(Account, related_name='transfers_to', on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    trans_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-trans_time']
        indexes = [
        models.Index(fields=['-trans_time']),
        ]



    