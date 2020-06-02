from django.shortcuts import render

# Create your views here.
def home(request):
    import json
    import requests
    #import datetime

    api_requests = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=1&API_KEY=DD6F3AF3-415F-446C-BDBE-721221738FE8")
    api = json.loads(api_requests.content)
    #date = datetime.datetime.strptime(api[0]['DateObserved'], '%Y-%m-%d')
    #date.strftime('%d-%m-%Y')
# Python try-except routine
    #try:
        #api = json.loads(api_requests.content)
    #except Exception as e:
        #api = "420-Error"

    return render(request, 'home.html', {'api': api})

def about(request):
    return render(request, 'about.html', {})
