from django.shortcuts import render
import requests

url = "https://covid-193.p.rapidapi.com/countries"

headers = {
	"x-rapidapi-key": "bcb0709fb7mshb6146f28cd5833dp113160jsn0c26bce49e89",
	"x-rapidapi-host": "covid-193.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())


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
    context = {}
    return render(request, 'covid.html', context)