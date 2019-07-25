from django.shortcuts import HttpResponse

from .tasks import celery_task

def celery_view(request):
    for counter in range(2):
        celery_task.delay(counter)
    return HttpResponse("FINISH PAGE LOAD")