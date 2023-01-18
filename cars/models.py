from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Car(models.Model):
    id = models.IntegerField(primary_key=True)
    car_brand = models.CharField(max_length=20)
    car_model = models.CharField(max_length=20)
    car_description = models.CharField(max_length=70)
    engine_type = models.CharField(max_length=20)
    power = models.IntegerField()
    tourque = models.IntegerField()
    no_of_cylinder = models.IntegerField()
    valves_per_cylinder = models.IntegerField()
    transmission_type = models.CharField(max_length=20)
    drive_type = models.CharField(max_length=20)
    fuel_type = models.CharField(max_length=20)
    body_type = models.CharField(max_length=20)
    seating_capacity = models.IntegerField()
    wheel_size = models.IntegerField()
    top_speed = models.IntegerField()
    acceleration_to_100 = models.IntegerField()
    price = models.IntegerField()
    main_img = models.CharField(default=None, max_length=150)
    
    class Meta:
        managed = True
        db_table = 'cars_car'
    
    def __str__(self):
        return f"{self.car_brand} {self.car_model}"



class Image(models.Model):
    id = models.IntegerField
    link = models.CharField(max_length=150)
    car_id = models.ForeignKey('Car', on_delete=models.CASCADE)

    class Meta:
        db_table = 'car_image'

class Comment(models.Model):
    car = models.ForeignKey('Car', on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    body = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']
        db_table = 'car_comment'
    
    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
