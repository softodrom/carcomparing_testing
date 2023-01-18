from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve
from cars.views import home_page, index_page, compare_page, choose_compare_page ,car_page
from django.test import Client
from cars.models import Car, Image
import cars.func as func


class TestFunc(SimpleTestCase):
    #test users and login 
    def test_user(self):
        c = Client()
        response = c.get('/login/', {'username': 'tester', 'password': 'testing1password1'})
        code = response.status_code
        self.assertEqual(code, 200)
        
    def test_car_scores(self):
        car1 = {
        "brand": "Lamborghini",
        "model": "Aventador",
        "description": "Test for description",
        "engine": "V12",
        "power": "700",
        "torque": "2800",
        "cylinders": "4",
        "valves": "4",
        "transmission": "Automatic",
        "drive_type": "AWD",
        "fuel": "Petrol",
        "body": "Coupe",
        "seats": "2",
        "wheels": "22",
        "top_speed": "300",
        "acceleration": "2",
        "price": "190000",
        }
        
        car2 = {
        "brand": "Porsche",
        "model": "911 Turbo S",
        "description": "Test for description",
        "engine": "V12",
        "power": "800",
        "torque": "3200",
        "cylinders": "4",
        "valves": "2",
        "transmission": "Automatic",
        "drive_type": "AWD",
        "fuel": "Hybrid",
        "body": "Coupe",
        "seats": "2",
        "wheels": "23",
        "top_speed": "320",
        "acceleration": "1",
        "price": "150000",
        }
        
        result = func.compare(car1, car2)
        self.assertEqual(result['car1points'], 1)
        self.assertEqual(result['car2points'], 9)
        