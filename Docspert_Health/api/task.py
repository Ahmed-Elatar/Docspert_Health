from celery import shared_task

from time import sleep
from .models import *


@shared_task
def my_task( reader):

    for row in reader:
        record=Account.objects.filter(id=row['ID']).first()
        if record == None:
            Account.objects.create(id=row['ID'] , name = row['Name'] , balance = row['Balance']  )
        else:
            record.balance= row['Balance']
            record.save()

        print(row['Name'])
    

    return "Task DONE"

