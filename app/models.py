from django.db import models

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name= models.CharField(max_length=200)
    def __str__(self):
        return self.name
    

class CarroModel(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200, blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand')
    factory_year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    plate = models.CharField(max_length=10, blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    photo = models.ImageField(upload_to='app/', null=False)
    
    def __str__(self):
        return self.model

    