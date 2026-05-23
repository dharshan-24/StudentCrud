from django.shortcuts import render
from django.http import JsonResponse
from .models import Student
import json
from django.views.decorators.csrf import csrf_exempt
#Create
@csrf_exempt
def add_student(request):
    if request.method == "POST":
        data=json.loads(request.body)

        student=Student.objects.create(name=data["name"],age=data["age"],course=data["course"])

        return JsonResponse({"Message":"Student Added"})
    return JsonResponse({"message":"only post method allowed"})
#Read

def get_student(request):
    student=list(Student.objects.values())
    return JsonResponse(student,safe=False)
#Update

@csrf_exempt
def update_student(request,id):
    if request.method=="PUT":
        student=Student.objects.get(id=id)
        data=json.loads(request.body)
        student.name=data["name"]
        student.age=data["age"]
        student.course=data["course"]

        student.save()
        return JsonResponse({"message":"student Updated Successfully"})
#Delete
@csrf_exempt
def delete_student(request,id):
    if request.method == "DELETE":
        student=Student.objects.get(id=id)
        student.delete()

        return JsonResponse({"message":"Student Deleted"})
