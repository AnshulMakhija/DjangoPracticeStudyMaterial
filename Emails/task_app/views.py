from django.shortcuts import render
from .tasks import send_email_task

def send_email_view(request):
    if request.method == "POST":
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        to_email = request.POST.get("email")
        
        task = send_email_task.delay(subject, message, to_email)
        
        return render(request, "email_sent.html", {"task_id": task.id})
    
    return render(request, "send_email.html")
