from django.http import HttpResponse
from django.shortcuts import redirect,render
from work.models import student
def StudentAdmission(request):
    AllData=student.objects.all()
    if request.method=="POST":
        firstName=request.POST.get("txtFirstName")
        lastName=request.POST.get("txtFirstName")
        course=request.POST.get("txtCourse")
        percentage=request.POST.get("txtPercentage")
        Data=student()
        Data.FirstName=firstName
        Data.LastName=lastName
        Data.Course=course
        Data.Percentage=percentage
        Data.save()
        return render(request,"Student.html",{"Recordset":AllData})
    else:
        return render(request, "Student.html", {"Recordset": AllData})
# def DeleteData(request,pk):
#     Data=student.objects.get(id=pk)
#     Data.delete()
#     return redirect("savestudent")

# def Editdata(request,pk):
#     if request.method=="POST":
#         firstName = request.POST.get("txtFirstName")
#         lastName = request.POST.get("txtFirstName")
#         course = request.POST.get("txtCourse")
#         percentage = request.POST.get("txtPercentage")
#         Data = student.objects.get(id=pk)
#         Data.FirstName = firstName
#         Data.LastName = lastName
#         Data.Course = course
#         Data.Percentage = percentage
#         Data.save()
#         return redirect("savestudent")
#     else:
#         Data=student.objects.get(id=pk)
#         return render(request,"EditStudent.html",{"Data":Data})

from django.shortcuts import render
from work.forms import studentform
def index(request):
    student = studentform()
    return render(request, "index.html", {'form': student})
