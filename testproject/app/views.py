from django.shortcuts import render,redirect
from .models import Users,CompaniesSorted,CandidateUsers
from django.contrib import messages
from django.shortcuts import render
import pandas as pd
# Create your views here.

def signup(request):
    if 'user' not in request.session:
        if request.method == "POST":
            username = request.POST['username']
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            user = Users(username=username, name=name, email=email,password=password)
            user.save()
            return redirect("login")
        else:
            return render(request, 'signup.html')
    else:
        return redirect("uploaddata")
    
def login(request):
    if 'user' not in request.session:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            if Users.objects.filter(username=username,password=password).exists():
                request.session["user"] = username
                return render(request, "uploaddata.html")
        else:
            return render(request, 'login.html')
    else:
        return redirect("uploaddata")

def logout(request):
    if 'user' in request.session:
        del request.session["user"]
        return redirect("login")


def users(request):
    if 'user' in request.session:
        if request.method == "POST":
            name = request.POST['name']
            email = request.POST['email']
            user = CandidateUsers(name=name, email=email)
            user.save()
            messages.success(request, 'New User Added.')
            return redirect("users")

        else:
            alldata = CandidateUsers.objects.all()
            context = {
                "alldata":alldata
            }

            return render(request, 'allusers.html',context)
    else:
        return redirect("login")
    
def querrybuilder(request):
    if 'user' in request.session:
        if request.method == "POST":
            name = request.POST["name"]
            industry = request.POST["industry"]
            year_founded = request.POST["year_founded"]
            locality = request.POST["locality"]
            country = request.POST["country"]
            current_employee_estimate = request.POST["current_employee_estimate"]
            total_employee_estimate = request.POST["total_employee_estimate"]
            data = CompaniesSorted.objects.filter(name=name,industry=industry,year_founded=year_founded,locality=locality,country=country,current_employee_estimate=current_employee_estimate,total_employee_estimate=total_employee_estimate)
            total =  0
            for i in data:
                total+=1
            messages.success(request, total)
        alldata = CompaniesSorted.objects.all()
        return render(request, "querybuilder.html",{"alldata":alldata})
    else:
        return redirect("login")





def upload_csv(request):
    if request.method == 'POST' and request.FILES['file']:
        csv_file = request.FILES['file']
        chunk_size = 1  
        for chunk in pd.read_csv(csv_file, chunksize=chunk_size):
            records = chunk.to_dict(orient='records')
            CompaniesSorted.objects.bulk_create([CompaniesSorted(number=record['Unnamed: 0'],name=record['name'],domain=record['domain'],year_founded=record['year founded'],industry=record['industry'],size_range=record['size range'],locality=record['locality'],country=record['country'],linkedin_url=record['linkedin url'],current_employee_estimate=record['current employee estimate'],total_employee_estimate=record['total employee estimate']) for record in records])

        return render(request, "uploaddata.html")
    
    return render(request, "uploaddata.html")