from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import pytz

def home(request):
    ist = pytz.timezone('Asia/Kolkata')
    now_ist = datetime.now(ist).strftime("%I:%M %p, %A, %d %B %Y")  # 12-hour format, day, date

    return render(request, 'home/welcome.html', {'today': now_ist})