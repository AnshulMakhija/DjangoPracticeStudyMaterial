from django.shortcuts import render
from .forms import StudentForm, TeacherForm

# Create your views here.
def student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = StudentForm()
    return render(request, 'ModelInheritance/student.html', {'form': form})


def teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TeacherForm()
    return render(request, 'ModelInheritance/teacher.html', {'form': form})
