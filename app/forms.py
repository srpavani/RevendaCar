from django import forms 
from app.models import CarroModel, Brand

'''
class CarForm(forms.Form):
  model = forms.CharField(max_length=200)
  brand = forms.ModelChoiceField(Brand.objects.all())
  factory_year = forms.IntegerField()
  model_year = forms.IntegerField()
  plate = forms.CharField(max_length=10)
  value = forms.FloatField()
  photo = forms.ImageField()
  
  def save(self):
      car = CarroModel(
          model = self.cleaned_data['model'],
          brand = self.cleaned_data['brand'],
          factory_year = self.cleaned_data['factory_year'],
          plate = self.cleaned_data['plate'],
          value = self.cleaned_data['value'],
          photo = self.cleaned_data['photo'],
      )
      car.save()
      return car
  '''
class CarModelForm(forms.ModelForm):
     class Meta:
         model = CarroModel
         fields = '__all__'