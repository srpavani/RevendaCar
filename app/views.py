from django.http import HttpResponse
from django.shortcuts import redirect, render
from app.models import CarroModel
from app.forms import CarModelForm
#from app.forms import CarForm


def cars_view(request):
    cars = CarroModel.objects.all().order_by('model')
    search = request.GET.get('search')
    if search:     
        cars = cars.filter(model__icontains=search)
    return render(request, 'cars.html', {'cars':cars})


def new_car_view(request):
    if request.method =='POST':
        new_car_form = CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
    else:
        new_car_form = CarModelForm()
    return render(request, 'new_car.html', {'new_car_form':new_car_form})



''' USANDO O FORM ANTIGO
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