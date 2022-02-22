from django.shortcuts import render
from api.models import AppDB
# Create your views here.



def forside(request):
    db = AppDB.objects.all()
    db = db[::-1]

    verdier = {
        "db": db,
    }
    return render(request, 'front.html', verdier)
