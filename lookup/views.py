from django.shortcuts import render

# Create your views here.
def home(request):
    import json
    import requests
    #import datetime
    if request.method == "POST":
        zipcode = request.POST['zipcode']
        api_requests = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=1&API_KEY=DD6F3AF3-415F-446C-BDBE-721221738FE8")
        #api = json.loads(api_requests.content)
        #date = datetime.datetime.strptime(api[0]['DateObserved'], '%Y-%m-%d')
        #date.strftime('%d-%m-%Y')
    # Python try-except routine
        try:
            api = json.loads(api_requests.content)
        except Exception as e:
            api = "420-Error"
    # Python code removed from home.html
        if api[0]['Category']['Number'] == 1:
            category_description = '(0 - 50): Air quality is satisfactory, and air pollution poses little or no risk.'
            category_colour = 'good'
        elif api[0]['Category']['Number'] == 2:
            category_description = '(51 to 100): Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution.'
            category_colour = 'moderate'
        elif api[0]['Category']['Number'] == 3:
            category_description = '(101 to 150): Members of sensitive groups may experience health effects. The general public is less likely to be affected.'
            category_colour = 'UnhealthySensitiveGroups'
        elif api[0]['Category']['Number'] == 4:
            category_description = '(151 to 200): Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects.'
            category_colour = 'unhealthy'
        elif api[0]['Category']['Number'] == 5:
            category_description = '(201 to 300): Health alert: The risk of health effects is increased for everyone.'
            category_colour = 'veryunhealthy'
        elif api[0]['Category']['Number'] == 6:
            category_description = '(301 and higher): Health warning of emergency conditions: everyone is more likely to be affected.'
            category_colour = 'hazardous'

        return render(request, 'home.html', {'api': api,
                                'category_description':category_description,
                                'category_colour': category_colour})
    else:
        api_requests = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=1&API_KEY=DD6F3AF3-415F-446C-BDBE-721221738FE8")
    # Python try-except routine
        try:
            api = json.loads(api_requests.content)
        except Exception as e:
            api = "420-Error"
    # Python code removed from home.html
        if api[0]['Category']['Number'] == 1:
            category_description = '(0 - 50): Air quality is satisfactory, and air pollution poses little or no risk.'
            category_colour = 'good'
        elif api[0]['Category']['Number'] == 2:
            category_description = '(51 to 100): Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution.'
            category_colour = 'moderate'
        elif api[0]['Category']['Number'] == 3:
            category_description = '(101 to 150): Members of sensitive groups may experience health effects. The general public is less likely to be affected.'
            category_colour = 'UnhealthySensitiveGroups'
        elif api[0]['Category']['Number'] == 4:
            category_description = '(151 to 200): Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects.'
            category_colour = 'unhealthy'
        elif api[0]['Category']['Number'] == 5:
            category_description = '(201 to 300): Health alert: The risk of health effects is increased for everyone.'
            category_colour = 'veryunhealthy'
        elif api[0]['Category']['Number'] == 6:
            category_description = '(301 and higher): Health warning of emergency conditions: everyone is more likely to be affected.'
            category_colour = 'hazardous'

        return render(request, 'home.html', {'api': api,
                                'category_description':category_description,
                                'category_colour': category_colour})

def about(request):
    return render(request, 'about.html', {})
