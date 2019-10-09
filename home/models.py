from django.db import models
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save

class Product(models.Model):
    # product_id=models.AutoField
    
    des=models.CharField(max_length=50)
    
    # user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.des
class Product2(models.Model):
    # product_id=models.AutoField
    
    des=models.CharField(max_length=50)
    
    # user=models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.des