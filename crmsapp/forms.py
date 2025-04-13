from django import forms
from .models import Administrator
from .models import caruser
from .models import car

class AdministratorForm(forms.ModelForm):
    class Meta:
        model = Administrator
        fields =[
            "adminuname",
            "adminpwd",
            ]


class caruserForm(forms.ModelForm):
    class Meta:
        model = caruser
        fields =[
            "username",
            "password",
            "fname",
            "useremail",
            "mobno",
            ]

class carForm(forms.ModelForm):
    class Meta:
        model = car
        fields =[
            "username",
            "regno",
            "model",
            "year",
            "km",
	    "noacc",
            "opos",
            "mileage",
            "noseat",
            "enginetype",
            "expprice",
            "transmission",
            "status",
            ]

