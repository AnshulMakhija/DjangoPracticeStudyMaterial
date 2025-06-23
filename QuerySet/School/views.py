from django.shortcuts import render
from django.db.models import Q
from .models import student, teacher

# Create your views here.
def student_data(request):
    #students = student.objects.all()
    #students = student.objects.filter(roll_no = 2)
    #students = student.objects.exclude(roll_no = 2)
    #students = student.objects.order_by("-roll_no") # Sorting the data in descending order
    #students = student.objects.order_by("roll_no") # Sorting the data
    #students = student.objects.order_by("?") # Random sorting
    #students = student.objects.order_by("roll_no").reverse()[:5]
    #students = student.objects.values()
    #students = student.objects.values("roll_no","name")
    #students = student.objects.dates("date","month")
    #students = student.objects.dates("date","year") #year ke place pr "week", "day" bhi add...
    #students = student.objects.datetimes("") # same as dates
    #students = student.objects.none() # empty queryset 
    #students = student.objects.using('default') # Using the default database
    
    query1 = student.objects.values_list("name","age","standard", named=True)
    query2 = teacher.objects.values_list("name","age","standard", named=True)
    #students = query2.union(query1, all= True)
    #students = query2.intersection(query1)
    #students = query2.difference(query1)
    
    #students = student.objects.filter(roll_no = 2) & student.objects.filter(name = "Rahul")
    #students = student.objects.filter(roll_no=2, name="Rahul")
    #students = student.objects.filter(Q(roll_no=2) & Q(name="Rahul"))
    
    #students = student.objects.filter(roll_no = 2) | student.objects.filter(name = "Rahul")
    #students = student.objects.filter(Q(roll_no=2) | Q(name="Rahul"))
    
    '''{% for student in students %}
        <tr>
            <td>{{student.roll_no}}</td>
            <td>{{student.name}}</td>
            <td>{{student.age}}</td>
            <td>{{student.marks}}</td>
            <td>{{student.standard}}</td>
        </tr>
        {% endfor %}'''
    
    # ----------------------------------------------------------------------------------------
    # These function doesnt return any query and are not iterable
    #students = student.objects.get(pk=1) 
    #students = student.objects.first()
    #students = student.objects.last()
    #students = student.objects.latest("name")
    #students = student.objects.earliest("name")
    
    #students = student.objects.create(name="Mille",roll_no=3,age=19,marks=60,standard=4)
    #students, created = student.objects.get_or_create(name="Cecelia",roll_no=4,age=15,marks=90,standard=4) # if the student is not present then it will be created
    #students = student.objects.filter(roll_no=2).update(marks=45)
    #students, created = student.objects.update_or_create(roll_no=4, defaults={'name': 'Enzo'})
    
    #This bulk doesnt work in inheritance or you can say Many to Many relationship
    # both bulk create and bulk update
    '''
    stu_obj = [
        student(name="kelly",roll_no=5,age=29,marks=60,standard=5),
        student(name="Sarah",roll_no=6,age=12,marks=44,standard=2),
        student(name="Hunt",roll_no=7,age=17,marks=89,standard=5),
        student(name="Shane",roll_no=8,age=22,marks=70,standard=8)
    ]
    
    students = student.objects.bulk_create(stu_obj)'''
    
    #students = student.objects.in_bulk([1,2])
    '''delete and bulk delete
    del_student = student.objects.get(pk=1)
    students = del_student.delete()
    
    delete in bulk
    students = student.objects.filter(marks=50).delete()
    students = student.objects.all().delete()
    '''
    
    #students = student.objects.filter(name__exact='shane') # exact is used for exact match (case sensitive)
    #students = student.objects.filter(name__iexact='shane') # iexact is used for case insensitive match
    #students = student.objects.filter(name__contains='u') # contains is used for substring match
    #students = student.objects.filter(name__icontains='u') # icontains is used for case insensitive substring match
    #students = student.objects.filter(id__in=[3,4])
    #students = student.objects.filter(marks__gt=60) # greater than
    #students = student.objects.filter(marks__gte=60) # greater than or equal to
    #students = student.objects.filter(marks__lt=60) # less than
    #students = student.objects.filter(marks__lte=60) # less than or equal to
    #students = student.objects.filter(name__startswith='s') # startswith is used for prefix match
    #students = student.objects.filter(name__istartswith='s') # istartswith is used for case insensitive prefix match
    #students = student.objects.filter(name__endswith='e')
    #students = student.objects.filter(name__iendswith='e')
       
    print(students)
    print()
    #print(students[1])
    #print(students.query)
    #print(created)
    print()
    return render(request, 'School/home.html', {'students': students})