from django import forms 
from app.models import CarroModel

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

    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value is not None and value < 20000:
            self.add_error('value', 'O valor mínimo do carro deve ser R$20.000')
        return value

    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year is not None and factory_year < 2000:
            self.add_error('factory_year', 'A data de fabricação não pode ser anterior a 2000')
        return factory_year