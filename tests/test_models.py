from cars.models import Car, Comment
from django.test import TestCase

class CarModelTests(TestCase):
    def test_method_string(self):
        car = Car.objects.get(id=1)
        expected_string = f"{car.car_brand} {car.car_model}"
        self.assertEqual(str(car), expected_string)

class CommentModelTests(TestCase):
    def test_method_string(self):
        comment = Comment.objects.all().first()
        expected_string = f"Comment {comment.body} by {comment.name}"
        self.assertEqual(str(comment), expected_string)