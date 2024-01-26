from celery import shared_task


# dummy task to test celery is working
@shared_task
def sum(a, b):
    return a + b
