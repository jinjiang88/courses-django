from django.shortcuts import render, redirect
from .models import Course

def index(request):
    courses = Course.objects.all()
    context = {
    "courses" : courses,
    }
    return render(request, 'courses_app/index.html', context)
def process(request):
    Course.objects.create(name=request.POST['name'], description=request.POST['description'])
    return redirect('/')
def destroy(request, cid):
    minusCourse = Course.objects.get(id=cid)
    name = minusCourse.name
    description = minusCourse.description
    cid = minusCourse.id
    context = {
        "name" : name,
        "description" : description,
        "cid" : cid
    }
    return render(request, 'courses_app/destroy.html', context)
def delete(request, cid):
    Course.objects.get(id=cid).delete()
    return redirect("/")
