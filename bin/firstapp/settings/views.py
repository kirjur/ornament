from django.shortcuts import render
from django.shortcuts import render_to_response
from settings.models import Settings


# Create your views here.



def settings(request,settings_id=1):
    return render_to_response('settings.html', {'settings': Settings.objects.all()})
