from django.db import models

# Create your models here.


class Car(models.Model):

    city = models.CharField(max_length=30)
    brand = models.CharField(max_length=30)
    car_type = models.CharField(max_length=30)
    reg_time = models.DateField()
    mileage = models.IntegerField()
    price = models.IntegerField()

    def __unicode__(self):
        return "<{}\t{}\t{}>".format(self.brand, self.car_type, self.price)
