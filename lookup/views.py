from django.shortcuts import render

# Create your views here.
def home(request):
    import json
    # http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=1&API_KEY=DD6F3AF3-415F-446C-BDBE-721221738FE8
    return render(request, 'home.html', {})

def about(request):
    return render(request, 'about.html', {})
