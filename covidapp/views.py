from django.shortcuts import render

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

