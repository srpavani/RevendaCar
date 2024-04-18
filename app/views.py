from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import redirect, render
from app.models import CarroModel
from app.forms import CarModelForm
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView 
#from app.forms import CarForm

class CarListView(ListView):
    model = CarroModel
    template_name = 'cars.html'
    context_object_name = 'cars'
    
    def get_queryset(self):
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if search:
            cars = cars.filter(model__icontains=search)
        return cars    
            
          
class NewCarCreateView(CreateView):
    model = CarroModel
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url= '/cars/'
    
class CarDetailView(DetailView):
    model = CarroModel
    template_name = 'car_detail.html'
    
    
class CarUpdateView(UpdateView):
    model=CarroModel 
    form_class = CarModelForm
    template_name = 'car_update.html'
    success_url = '/cars/'  
    
    
    
    
    

        



''' USANDO O FORM ANTIGO


class NewCarView(View):
    def get(self, request):
        new_car_form = CarModelForm()
        return render(request, 'new_car.html', {'new_car_form':new_car_form})
    
    def post(self, request):
        new_car_form = CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
        return render(request, 'new_car.html', {'new_car_form':new_car_form})
        

class CarsView(View):
  def get(self, request):
    cars = CarroModel.objects.all().order_by('model')
    search = request.GET.get('search')
    if search:     
        cars = cars.filter(model__icontains=search)
    return render(request, 'cars.html', {'cars':cars})    


def cars_view(request):
    cars = CarroModel.objects.all().order_by('model')
    search = request.GET.get('search')
    if search:     
        cars = cars.filter(model__icontains=search)
    return render(request, 'cars.html', {'cars':cars})



def new_car_view(request):
    if request.method =='POST':
        new_car_form = CarForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
    else:
        new_car_form = CarForm()
    return render(request, 'new_car.html', {'new_car_form':new_car_form})

'''
#to na aula 57