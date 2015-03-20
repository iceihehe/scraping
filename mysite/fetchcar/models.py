from django.db import models

# Create your models here.

class Brand(models.Model):

	name = models.CharField(max_length=30)


class CarType(models.Model):

	name = models.CharField(max_length=30)
	brand = models.ForeignKey(Brand)


class Car(models.Model):

    city = models.CharField(max_length=30, null=True)
    car_type = models.ForeignKey(CarType, null=True)
    reg_time = models.DateField(null=True)
    mileage = models.IntegerField(null=True)
    price = models.IntegerField(null=True)

    def __unicode__(self):
        return "<{}\t{}\t{}>".format(self.brand, self.car_type, self.price)
