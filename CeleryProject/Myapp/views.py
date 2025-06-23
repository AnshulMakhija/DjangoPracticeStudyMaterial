from django.shortcuts import render
from Celery.celery import add
from .tasks import sub
from celery.result import AsyncResult

# Create your views here.
# delay() is used to run the task in the background
def index(request):
    result = add.delay(4, 4)
    sub.delay(40, 4)
    return render(request, 'Myapp/home.html', {'result': result})
    
# apply_async() 
"""def index(request):
    print("Results : ")
    result = add.apply_async(args=[4, 4])
    print(result)
    result1 = sub.apply_async(args=[40, 4])
    print(result1)
    return render(request, 'Myapp/home.html')
"""

def check_result(request, task_id):
    result1 = AsyncResult(task_id)
    return render(request, 'Myapp/result.html', {'result': result1})

def about(request):
    return render(request, 'Myapp/about.html')

def contact(request):
    return render(request, 'Myapp/contact.html')
