from django.db import models

# class Image(models.Model):
#     caption = models.CharField(max_length=50)
#     name = models.CharField(max_length=50) 
#     image = models.ImageField(upload_to='img/%y')
#     price = models.PositiveBigIntegerField(default=0)
    
#     def __str__(self):
#         return self.caption

class Pizza(models.Model):
    name = models.CharField(max_length=50) 
    caption = models.CharField(max_length=250)
    image = models.ImageField(upload_to='img/%y')
    price = models.BigIntegerField()
    
    def __str__(self):
        return self.name