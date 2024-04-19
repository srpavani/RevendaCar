from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver
from app.models import CarroModel


@receiver(post_save, sender=CarroModel)
def car_post_save(sender, instance, **kwargs):
    print('### POST SAVE ###')    
    print(instance)

@receiver(post_delete, sender=CarroModel)
def car_post_delete(sender, instance, **kwargs):
    print('### POST SAVE ###')      
    print(instance)


'''
@receiver(pre_save, sender=CarroModel)
def car_pre_save(sender, instance, **kwargs):
    print('### PRE SAVE ###')
    print(instance)
    
    
    
@receiver(pre_delete, sender=CarroModel)
def car_pre_delete(sender, instance, **kwargs):
    print('### PRE SAVE ###')
    print(instance)
    

'''    



    