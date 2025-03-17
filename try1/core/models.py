from django.db import models


# Create your models here.
class Car(models.Model):
    car_name = models.CharField(max_length=100)
    speed = models.IntegerField(default=50)

    def __str__(self) -> str:
        return self.car_name + " " + str(self.speed)
