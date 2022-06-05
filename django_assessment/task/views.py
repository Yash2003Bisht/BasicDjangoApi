from django.shortcuts import redirect, render
from .models import Records
from django.utils import timezone
from django.http import JsonResponse

def create_new_record(request):
    if request.method == "POST":
        note = Records(name=request.POST["name"], description=request.POST["desc"], email=request.POST["email"], createdAt = timezone.now())
        note.save()
        return redirect(display_all_record)
    return render(request, "task/index.html")

def display_all_record(request):
    jsondata = {
        "data": [{"id":data.id, "name": data.name, "description": data.description, "email": data.email, "createdAt": data.createdAt} for data in Records.objects.all()]
        }
    return JsonResponse(jsondata, json_dumps_params={'indent': 2})
