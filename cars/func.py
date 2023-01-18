from django.http.response import HttpResponse
from cars.models import Car, Image
import datetime

#get all data from a car model
def get_car(car):
    count = 0
    data = dict()
    carres = Car.objects.get(car_model=car)
    print(carres.id)
    car_id = Image.objects.filter(car_id_id=carres.id)
    
    print(carres.car_model)
    for im in car_id:
        link = im.link
        break

    data = {
        "brand": carres.car_brand,
        "model": carres.car_model,
        "description": carres.car_description,
        "engine": carres.engine_type,
        "power": carres.power,
        "torque": carres.tourque,
        "cylinders": carres.no_of_cylinder,
        "valves": carres.valves_per_cylinder,
        "transmission": carres.transmission_type,
        "drive_type": carres.drive_type,
        "fuel": carres.fuel_type,
        "body": carres.body_type,
        "seats": carres.seating_capacity,
        "wheels": carres.wheel_size,
        "top_speed": carres.top_speed,
        "acceleration": carres.acceleration_to_100,
        "price": carres.price,
        "image": link,
    }
    return data

def compare(car1,car2):
    car1points = 0
    car2points = 0
    data = dict()
    
    #power point
    if(car1['power'] > car2['power']):
        car1points += 1
    else:
        car2points += 1
        
    #torque point
    if(car1['torque'] > car2['torque']):
        car1points += 1
    else:
        car2points += 1
        
    #cylinders point
    if(car1['cylinders'] > car2['cylinders']):
        car1points += 1
    else:
        car2points += 1
        
    #valves point
    if(car1['valves'] > car2['valves']):
        car1points += 1
    else:
        car2points += 1
        
    #transmission point
    if(car1['transmission'] == "Automatic" and car2['transmission'] == "Manual"):
        car1points += 1
    elif(car1['transmission'] == "Manual" and car2['transmission'] == "Automatic"):
        car2points += 1
    
    #drive type point
    if(car1['drive_type'] == "AWD" and car2['drive_type'] != "AWD"):
        car1points += 1
    elif(car1['drive_type'] != "AWD" and car2['drive_type'] == "AWD"):
        car2points += 1
    elif(car1['drive_type'] == "RWD" and car2['drive_type'] != "RWD"):
        car1points += 1
    elif(car1['drive_type'] != "RWD" and car2['drive_type'] == "RWD"):
        car2points += 1
    
    #fuel point
    if(car1['fuel'] == "Hybrid" and car2['fuel'] != "Hybrid"):
        car1points += 1
    elif(car1['fuel'] != "Hybrid" and car2['fuel'] == "Hybrid"):
        car2points += 1
    elif(car1['fuel'] == "Petrol" and car2['fuel'] != "Petrol"):
        car1points += 1
    elif(car1['fuel'] != "Petrol" and car2['fuel'] == "Petrol"):
        car2points += 1
        
    #seating point
    if(car1['seats'] > car2['seats']):
        car1points += 1
    else:
        car2points += 1
        
    #wheel point
    if(car1['wheels'] > car2['wheels']):
        car1points += 1
    else:
        car2points += 1
        
    #top speed point
    if(car1['top_speed'] > car2['top_speed']):
        car1points += 1
    else:
        car2points += 1
        
    #acceleration point
    if(car1['acceleration'] < car2['acceleration']):
        car1points += 1
    else:
        car2points += 1
        
    #price point
    if(car1['price'] < car2['price']):
        car1points += 1
    else:
        car2points += 1
        
    print("car1 points: " + str(car1points))
    print("car2 points: " + str(car2points))
    
    data = {
        "car1points": car1points,
        "car2points": car2points,
    }
        
    return data
    
    
