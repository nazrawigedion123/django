from django.shortcuts import render
from django.http.response import HttpResponse
from .import models

from django.shortcuts import render
from .forms import DestinationForm, ScheduleForm
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import destination





# Create your views here.
def simple_view(request):
    return HttpResponse("simple view")
def list_destination(request):
    all_destination= models.destination.objects.all()
    context={'destination':all_destination}
    form = ScheduleForm(request.POST,  request.FILES)
    if request.method == 'POST':
       print('in post')

      #  template = loader.get_template('myapp/schedule_appointment.html')

       if form.is_valid():
           print('valid')
           form.save()

       else:
           print('isnt saved')
           form = ScheduleForm()
    context.update({'form':form})
    
    
    

    
    
    return render(request, 'myapp/list.html',  context=context)




   
        



def delete(request, id):
  member = destination.objects.get(id=id)
  member.delete()
  


def table(request):
    all_destination = models.destination.objects.all()
    context = {'destination': all_destination}
    
    

    
    return render(request, 'myapp/table.html', context=context)


def destination_view(request):
    
    if request.method == 'POST':
        print ('in post')
        form = DestinationForm(request.POST,  request.FILES)
        
        if form.is_valid():
            print('valid')
            form.save()
        
            
            
    else:
        print('isnt saved')
        form = DestinationForm()
    return render(request, 'myapp/destination.html', {'form': form})


def delete(request, id):
  member = destination.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('home'))


def update(request, id):
  des = destination.objects.get(id=id)
  template = loader.get_template('myapp/update.html')
  context = {
      'destinat': des,
  }
  return HttpResponse(template.render(context, request))


def updaterecord(request, id):
  
  image = request.POST['image']
  description = request.POST['description']
  des = destination.objects.get(id=id)
  des.image=image
  des.description=description
  des.save()
  return HttpResponseRedirect(reverse('home'))




    





