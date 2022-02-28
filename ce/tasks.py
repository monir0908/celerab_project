# Create your tasks here
from celery import shared_task
import datetime

# @shared_task
# def add(x, y):
#     return x + y


# @shared_task
# def mul(x, y):
#     return x * y


@shared_task
def celery_testing_func():
    print("Celery Working")
    sum = 0
    for i in range(1, 3):
        sum = sum + i
    print("Sum of first 2 natural number :", sum)
    print("The function ran on :", datetime.datetime.now())    
    return None

@shared_task
def celery_beat_testing_func():
    print("Celery Working with Beat")
    sum = 0
    for i in range(1, 6):
        sum = sum + i
    print("Sum of first 5 natural number :", sum)
    print("The scheduled function ran on :", datetime.datetime.now())     
    return None