from django.views import View
from django_project.models import Ticket
from django.shortcuts import render, redirect
import datetime
dates=[]

class Home(View):
    def get(self, request):
        return render(request, 'home.html')

    def post(self, request):
        #store new input as datetime object in "database"
        
        newDate = datetime.datetime.strptime(request.POST["datetime"],
                                             '%Y-%m-%dT%H:%M')
        location = request.POST["location"]
      
        ticketInfo = Ticket(datetime=request.POST["datetime"], location=location)
        ticketInfo.save()

        #extract all objects from database, compose tuples of formatted outputs
        formattedDates = []
        for i in dates:
            formattedDates.append((i.strftime("%A"), i.strftime("%B %d"),
                                   i.strftime("%Y"), i.strftime("%H:%M")))
        return render(request, "ticket_list.html", {})
class TicketList(View):
    def get(self,request):
      tickets= list(Ticket.objects.all())
      print (tickets,"tickets!")
      return render(request,'ticket_list.html',{"ticketlist": tickets})
from django.views import View
from django_project.models import Ticket
from django.shortcuts import render, redirect
import datetime
dates=[]

class Home(View):
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        #store new input as datetime object in "database"

        newDate = datetime.datetime.strptime(request.POST["datetime"],
                                             '%Y-%m-%dT%H:%M')
        location = request.POST["location"]

        ticketInfo = Ticket(datetime=request.POST["datetime"], location=location)
        ticketInfo.save()

        return redirect("/ticket_list/", {})

class TicketList(View):
    def get(self,request):
      tickets= list(Ticket.objects.all())
      print (tickets)
      return render(request,'ticket_list.html',{"ticketlist": tickets})
