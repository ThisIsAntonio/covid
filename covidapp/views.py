from django.shortcuts import render
import requests
import json

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
	"x-rapidapi-key": "bcb0709fb7mshb6146f28cd5833dp113160jsn0c26bce49e89",
	"x-rapidapi-host": "covid-193.p.rapidapi.com"
}

data = requests.get(url, headers=headers)
response = data.json()
# print(response)


# Create your views here.
def helloworldview(request):
    string = "Everyone"
    context2 = {}
    
    mylistitems = ['item1', 'item2', 'item3']
    context =   { 
                    'string': string ,
                    'mylistitems': mylistitems 
                }
    return render(request, 'helloworld.html', context)

def covidview(request):
    
    title = "Covid 19 Worldwide Data"
    noofresults = int(response['results'])
    myList = []
    for x in range(0, noofresults):
        # print(response['response'][x]['country'])
        myList.append(response['response'][x]['country'])
    
    # Initializing default values
    selectedCountry = None
    new = active = critical = recovered = total = death = countryName = None
    
    # Process the POST request
    if request.method == 'POST':
        selectedCountry = request.POST.get('selectedCountry', None)
        print(f"Selected Country: {selectedCountry}")
        
        # Search the selected country and show it via API
        for x in range(0, noofresults):
            if selectedCountry == response['response'][x]['country']:
                countryName = response['response'][x]['country']
                new = response['response'][x]['cases']['new']
                active = response['response'][x]['cases']['active']
                critical = response['response'][x]['cases']['critical']
                recovered = response['response'][x]['cases']['recovered']
                total = response['response'][x]['cases']['total']
                death = int(total) - int(active) - int(recovered)

    # Create context with the required data
    context = {
        'title': title,
        'myList': myList,
        'new': new,
        'active': active,
        'critical': critical,
        'recovered': recovered,
        'total': total,
        'death': death,
        'countryName': countryName
    }
    
    return render(request, 'covid.html', context)