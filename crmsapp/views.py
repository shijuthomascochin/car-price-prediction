from django.shortcuts import render
from .models import Administrator
from .forms import AdministratorForm
from .models import caruser
from .forms import caruserForm
from .models import car
from .forms import carForm
from django.shortcuts import (get_object_or_404,render,HttpResponseRedirect)
from django.http import HttpResponse
import pandas as pd
import array as arr
from sklearn.linear_model import LinearRegression



# Create your views here.
def test(request):
    return render(request, "test.html")

# Create your views here.
def index(request):
    return render(request, "index.html")


def admin_login(request):
    context = {}
    if request.method == 'POST':
          username = request.POST['adminuname']
          password = request.POST['adminpwd']
          user = Administrator.objects.raw("SELECT * FROM crmsapp_Administrator WHERE adminuname = %s and adminpwd=%s", [username,password])
          if user is not None:
              if user:
                  return render(request,'ahome.html', {})
              else:
                  # Return a 'disabled account' error message
                  return HttpResponse("You're account is disabled.")
          else:
              # Return an 'invalid login' error message.
              print ( "invalid login details " + username + " " + password )
              return render(request,'alogin.html', {})
    else:
          # the login is a  GET request, so just show the user the login form.
          form = AdministratorForm(request.POST or None)
          context['form']= form
          return render(request,'alogin.html', context)

# Create your views here.
def alogin(request):
    context ={}
    form = AdministratorForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form']= form

    return render(request, "alogin.html",context)


# Create your views here.
def ahome(request):
    return render(request, "ahome.html")


def insert(request):
    context ={}
    form = AdministratorForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form']= form
    return render(request, "insert.html", context)


def list(request):
    context ={}
    context["dataset"] = Administrator.objects.all()
    return render(request, "list.html",context)


def cinsert(request):
    context ={}
    form = caruserForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form']= form
    return render(request, "cinsert.html", context)


def clist(request):
    context ={}
    context["dataset"] = caruser.objects.all()
    return render(request, "clist.html",context)


def user_login(request):
    context = {}
    if request.method == 'POST':
          username = request.POST['username']
          password = request.POST['password']
          user = caruser.objects.raw("SELECT * FROM crmsapp_caruser WHERE username = %s and password=%s", [username,password])
          if user is not None:
              if user:
                  request.session['uname'] = username
                  return render(request,'uhome.html', {})
              else:
                  # Return a 'disabled account' error message
                  return HttpResponse("You're account is disabled.")
          else:
              # Return an 'invalid login' error message.
              print ( "invalid login details " + username + " " + password )
              return render(request,'ulogin.html', {})
    else:
          # the login is a  GET request, so just show the user the login form.
          form = caruserForm(request.POST or None)
          context['form']= form
          return render(request,'ulogin.html', context)


def update_user_view(request, id):
    context ={}
    obj = get_object_or_404(caruser, id = id)
    form = caruserForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)
    context["form"] = form
    return render(request, "update_user_view.html", context)



# Create your views here.
def register(request):
    context ={}
    form = caruserForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form']= form

    return render(request, "register.html", context)

def addcar(request):
    context ={}
    form = carForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form']= form

    return render(request, "addcar.html", context)

def carlist(request):
    context ={}
    uname = request.session['uname']
    context["dataset"] = car.objects.raw("SELECT * FROM crmsapp_car WHERE username = %s", [uname])
    return render(request, "carlist.html",context)

def update_car_view(request, id):
    context ={}
    obj = get_object_or_404(car, id = id)
    form = carForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/carlist")
    context["form"] = form
    return render(request, "update_car_view.html", context)



def alistcar(request):
    context ={}
    context["dataset"] = car.objects.raw("SELECT * FROM crmsapp_car")
    return render(request, "acarlist.html",context)

def adelete_car(request,id):
    c=car.objects.get(id=id)
    c.delete()
    context ={}
    context["dataset"] = car.objects.raw("SELECT * FROM crmsapp_car")
    return render(request, "acarlist.html",context)

def aupdate_car(request,id):
    c=car.objects.get(id=id)
    c.update()
    context ={}
    context["dataset"] = car.objects.raw("SELECT * FROM crmsapp_car")
    return render(request, "acarlist.html",context)

def findcar(request):
    context ={}
    if request.method == 'POST':
          price = request.POST['price']
          car = caruser.objects.raw("SELECT * FROM crmsapp_car where expprice>=%s", [price])
          if car is not None:
              context['dataset'] = car
              return render(request,'findcarresult.html', context)
    return render(request, "findcar.html",context)

def predict(request):
    context ={}
    if request.method == 'POST':
        km = request.POST['km']
        cars = pd.read_csv('data/mycar.csv')
        ohe_cars = pd.get_dummies(cars[['Car_Name']])
        X = pd.concat([cars[['Year', 'mileage','Kms_Driven']], ohe_cars], axis=1)
        y = cars['Selling_Price']
        regr = LinearRegression()
        regr.fit(X, cars['Selling_Price'])
        predictedCO2 = regr.predict([[2012, 20,km,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]])
        print(predictedCO2)
        context['km'] = predictedCO2
        print(predictedCO2[0])
        car = caruser.objects.raw("SELECT * FROM crmsapp_car where expprice>=%s", [predictedCO2[0]])
        if car is not None:
            context['dataset'] = car
            return render(request, "findcarkm.html",context)
    return render(request, "findcark.html",context)

def predictcarfrompprice(request):
    context ={}
    if request.method == 'POST':
        fpprice = request.POST['fpprice']
        tpprice = request.POST['tpprice'] 		
        cars = pd.read_csv('data/mycar.csv')
        ohe_cars = pd.get_dummies(cars[['Car_Name']])
        #X = pd.concat([cars[['Present_Price','mileage']], ohe_cars], axis=1)
        #y = cars['reg no']
        #regr = LinearRegression()
        #regr.fit(X, cars['reg no'])
        #predictedCO2 = regr.predict([[int(pprice),int(mi),0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]])
        #print(predictedCO2)
        #context['no'] = predictedCO2
        result = cars[cars["Present_Price"] >= int(fpprice)]
        result = result[result["Present_Price"] <= int(tpprice)]
        print(result)
        #car = caruser.objects.raw("SELECT * FROM crmsapp_car where expprice>=%s", [predictedCO2[0]])
        if result is not None:
            resulthtml=result.to_html()
            context['data'] = resulthtml
            return render(request, "findcarnamedata.html",context)
    return render(request, "findcarname.html",context)



def predictcarfromppriceold(request):
    context ={}
    if request.method == 'POST':
        fpprice = request.POST['fpprice']
        tpprice = request.POST['tpprice'] 		
        cars = pd.read_csv('data/mycar.csv')
        ohe_cars = pd.get_dummies(cars[['Car_Name']])
        X = pd.concat([cars[['Present_Price','mileage']], ohe_cars], axis=1)
        y = cars['reg no']
        regr = LinearRegression()
        regr.fit(X, cars['reg no'])
        predictedCO2 = regr.predict([[int(pprice),int(mi),0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]])
        print(predictedCO2)
        context['no'] = predictedCO2
        print(predictedCO2[0])
        #car = caruser.objects.raw("SELECT * FROM crmsapp_car where expprice>=%s", [predictedCO2[0]])
        #if car is not None:
            #context['dataset'] = car
            #return render(request, "findcarkm.html",context)
    return render(request, "findcarname.html",context)



def predictwithinput(request):
    context ={}
    if request.method == 'POST':
        yr = request.POST['yr']
        mi = request.POST['mi']
        km = request.POST['km']
        cars = pd.read_csv('data/mycar.csv')
        ohe_cars = pd.get_dummies(cars[['Car_Name']])
        X = pd.concat([cars[['Year', 'mileage','Kms_Driven']], ohe_cars], axis=1)
        y = cars['Selling_Price']
        regr = LinearRegression()
        regr.fit(X, cars['Selling_Price'])
        predictedCO2 = regr.predict([arr.array('i',[int(yr), int(mi),int(km),0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0])])
        print(predictedCO2)
        result = cars[cars["Selling_Price"] >= predictedCO2[0]]
        result.drop('username', inplace=True, axis=1)
        result.drop('reg no', inplace=True, axis=1)
        result.drop('Owner', inplace=True, axis=1)
        result.drop('no accidents', inplace=True, axis=1)
        resulthtml=result.to_html()
        context['data'] = resulthtml
        #print(result)
        print(predictedCO2[0])
        car = caruser.objects.raw("SELECT * FROM crmsapp_car where expprice>=%s", [predictedCO2[0]])
        if car is not None:
            context['dataset'] = car
            return render(request, "predictcarresult.html",context)
    return render(request, "predictcar.html",context)







