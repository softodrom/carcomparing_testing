from django.test import SimpleTestCase
from django.urls import reverse, resolve
from cars.views import home_page, index_page, compare_page, choose_compare_page ,car_page, login_page

class TestUrls(SimpleTestCase):
    def test_index_url(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, index_page)
        
    def test_compare_url(self):
        url = reverse('compare')
        self.assertEqual(resolve(url).func, compare_page)

    def test_choose_compare_page_url(self):
        url = reverse('choose compare page')
        self.assertEqual(resolve(url).func, choose_compare_page)
        
    def test_car_url(self):
        url = reverse('car')
        self.assertEqual(resolve(url).func, car_page)
        
    def test_car_url(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func, login_page)

        
    


        