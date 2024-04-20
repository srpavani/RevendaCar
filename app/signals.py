from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver
from app.models import CarroModel, CarInvetory
from django.db.models import Sum


def car_invetory_update():
    cars_count = CarroModel.objects.all().count()#conta quantos carros cadastrados existem no bd
    cars_value = CarroModel.objects.aggregate(
        total_value = Sum('value') #soma todos os valores dos carros
    )['total_value']
    CarInvetory.objects.create(
        cars_count=cars_count,
        cars_value = cars_value
    )
    


@receiver(post_save, sender=CarroModel)
def car_post_save(sender, instance, **kwargs):
    car_invetory_update()
    
    
@receiver(post_delete, sender=CarroModel)
def car_post_delete(sender, instance, **kwargs):
    car_invetory_update()

@receiver(pre_save, sender=CarroModel)
def car_pre_save(sender, instance, **kwargs):
    if not instance.bio:
        instance.bio = "Carro bom"
        #ai_bio = get_car_ai_bio(instance.brand, instance.model, instance.model_year)
       # instance.bio = ai_bio
        


'''

a069
@receiver(pre_save, sender=CarroModel)
def car_pre_save(sender, instance, **kwargs):
    print('### PRE SAVE ###')
    print(instance)
    
    
    
@receiver(pre_delete, sender=CarroModel)
def car_pre_delete(sender, instance, **kwargs):
    print('### PRE SAVE ###')
    print(instance)
    

'''    



    