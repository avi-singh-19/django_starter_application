from django.shortcuts import render
import datetime


# Create your views here.
def index(request):
    now = datetime.datetime.now()
    return render(request, "christmas/index.html", {
        "christmas": now.month == 12 and now.day == 25,
        "time_left": int((datetime.datetime(now.year, 12, 25) - now).days)
    })
