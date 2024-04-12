from django.contrib import admin
from app.models import CarroModel, Brand


class BrandAdmin(admin.ModelAdmin):
    list_display=('name',)
    search_fields=('name',)  

class carAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand','factory_year', 'model_year', 'value')
    search_fields=('model','brand')
    
    
    
admin.site.register(Brand,BrandAdmin)
admin.site.register(CarroModel, carAdmin)