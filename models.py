from django.db import models

# Create your models here.

class MenuItem(models.Model):
    name = models.CharField(max_length = 255)
    price = models.IntegerField()
    
    def __str__(self):
        
        return self.name


class Reservation(models.Model):
    first_name = models.CharField(max_length =255)
    last_name = models.CharField(max_length =255)
    guest_count = models.IntegerField()
    reservation_time = models.DateField(auto_now =True)
    comments = models.CharField(max_length = 1000)

    def __str__(self):
        
        return self.first_name + '' + self.last_name


