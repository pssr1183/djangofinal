from django.shortcuts import render
from travello.models import Destination

# Create your views here.   

def index(request):
    dest1 = Destination()
    dest1.name = 'Moscow'
    dest1.desc = 'The city which never sleeps'
    dest1.image = 'destination_1.jpg'
    dest1.price = 888

    dest2 = Destination()
    dest2.name = 'California'
    dest2.desc = 'Welcome to Silicon Valley!'
    dest2.image = 'destination_2.jpg'
    dest2.price = 777

    dest3 = Destination()
    dest3.name = 'London'
    dest3.desc = "Harry Potter's World"
    dest3.image = 'destination_3.jpg'
    dest3.price = 999

    dests=[
        dest1, dest2, dest3,
    ]


    
    return render(request, "index.html", {'dests' : dests} )
