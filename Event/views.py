from django.shortcuts import render
from django.http import HttpResponse
from Event.models import Details


def index(request):
    details=Details.objects.all().order_by('-date')
    return render(request,'frontend.html',{'req':details})


def create_details(request):
    if request.method == "POST":
        ename1 =request.POST.get("eventname")
        fname = request.POST.get("firstname")
        lname = request.POST.get("lastname")
        einfo = request.POST.get("event")
        date1 = request.POST.get("date")

        Details(eventname=ename1,firstname=fname,lastname =lname,info1=einfo,date=date1).save()
        return HttpResponse("Details Sucessfully Added ")
    else:
        return HttpResponse("Failed!! Something seriously Went Wrong!!Please Try Again after Fixing the Error!!!")


def delete(request):
    if request.method == "POST":
        user_delete =request.POST.get("search_id")
        Details.objects.get(id=user_delete). delete()
        return HttpResponse("Selected Details Sucessfully Deleted ")
    else:
        return HttpResponse("Failed To Delete!Something Went Wrong")

def update(request):
    if request.method == "POST":
        user_update=request.POST.get("search_name")
        ename=request.POST.get("eventname")
        fname=request.POST.get("firstname")
        lname=request.POST.get("lastname")
        einfo=request.POST.get("event")
        date=request.POST.get("date")

        Details.objects.filter(id=user_update).update(eventname=ename,firstname=fname,lastname=lname, info1=einfo,date=date )
        return HttpResponse("Updated Sucessfully")
    else:
        return HttpResponse("Update Failed! Someting Went Wrong")

def search(request):
    if request.method=="POST":
        user_search1 =request.POST.get("search_date1")
        user_search2 =request.POST.get("search_date2")

        if user_search2=='':
           q1=Details.objects.filter(date__gte=user_search1)
           return render(request,'search.html',{'data':q1})
        elif user_search1=='':
            q2=Details.objects.filter(date__lte=user_search2)
            return render(request,'search.html',{'data':q2})
        elif user_search1<user_search2:
              bydate= Details.objects.filter(date__range=[user_search1, user_search2])
              return render(request,'search.html',{'data':bydate})

        else:
              return HttpResponse("PLease DO enter valid dates")
        # if not bydate:
        #     return HttpResponse("No Events avilable for the Selected Date")
        # else:
        #     return render(request,'search.html',{'data':bydate})
    else:
        return HttpResponse("Failed!!!!")

