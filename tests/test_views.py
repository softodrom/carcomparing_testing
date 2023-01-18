from http import HTTPStatus
from django.http import response
from django.contrib.auth.models import User
from django.test import TestCase
from cars.forms import CommentForm
from cars.models import Car, Comment, Image

class LogInTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'unittest',
            'password': 'password1'}
        User.objects.create_user(**self.credentials)

    def test_login(self):
        response = self.client.post('/login/', self.credentials, follow=True)

        self.assertTrue(response.context['user'].is_active)

class LogOutTest(TestCase):
    def setUp(self):
        self.client.login(username='test', password='testing1pass')
    
    def test_logout(self):
        self.client.logout()

        response = self.client.get('/index/')

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/index/")


class IndexViewTests(TestCase):
    def setUp(self):
        self.client.login(username='test', password='testing1pass')
    
    def tearDown(self):
        self.client.logout()

    def test_redirects_if_not_logged_in(self):
        self.client.logout()
        response = self.client.get("/index/")

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/index/")

    def test_get(self):
        response = self.client.get("/index/")

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "<h1 class='main'>Pick your cars and see which suits you better.</h1>", html=True)

    def test_view_uses_correct_template(self):
        response = self.client.get("/index/")

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'index.html')

    def test_view_response_context(self):
        response = self.client.get("/index/")

        self.assertIsInstance(response.context['cars'][0], Car)
        self.assertEqual(len(response.context['cars']),9)

class CarViewTests(TestCase):
    def setUp(self):
        self.client.login(username='test', password='testing1pass')
    
    def tearDown(self):
        self.client.logout()

    def test_redirects_if_not_logged_in(self):
        self.client.logout()
        response = self.client.get("/car/Cayenne")

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/car/Cayenne")

    def test_get(self):
        response = self.client.get("/car/Cayenne")

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "<h1 class='display-3'><b>Porsche Cayenne</b></h1>", html=True)
        self.assertContains(response, "<button id='comment_btn' type='button' class='btn btn-info'>Read/Leave a comment</button>", html=True)
    
    def test_view_uses_correct_template(self):
        response = self.client.get("/car/Cayenne")

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'car.html')

    def test_view_response_context(self):
        response = self.client.get("/car/Cayenne")

        self.assertIsInstance(response.context['images'][0], Image)
        self.assertIsInstance(response.context['car'],Car)
        self.assertEqual(len(response.context['images']), 3)

class CommentFormViewTests(TestCase):
    def setUp(self):
        self.client.login(username='test', password='testing1pass')
    
    def tearDown(self):
        self.client.logout()
    
    def test_redirects_if_not_logged_in(self):
        self.client.logout()
        response = self.client.get("/car_comments/Cayenne/")

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/login/?next=/car_comments/Cayenne/")
    
    def test_get(self):
        response = self.client.get("/car_comments/Cayenne/")

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "<h1>Porsche Cayenne</h1>", html=True)
        self.assertContains(response, "<h2>2 comments</h2>", html=True)
        self.assertContains(response, "<i name='rating'>Average Rating: <b style='color: darkgoldenrod;'>8.5/10</b></i>", html=True)
    
    def test_success_post(self):
        response = self.client.post("/car_comments/Cayenne/", data={'name': 'Joe', 'email':'joe.winston@gmail.com', 'body':'Great car!', 'rating':7})

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "<div class='alert alert-success' role='alert'>Your comment is awaiting moderation</div>", html=True)

    def test_fail_post(self):
        response = self.client.post("/car_comments/Cayenne/", data={'name': 'joe', 'email':'joewinston@gm', 'body':'Great car!', 'rating':-1})

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "Should start with an uppercase letter", html=True)
        self.assertContains(response, "Enter a valid email address.", html=True)
        self.assertContains(response, "Rating should be between 1 and 10", html=True)
        
    def test_view_uses_correct_template(self):
        response = self.client.get("/car_comments/Cayenne/")

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'car_comments.html')

    def test_view_response_context(self):
        response = self.client.get("/car_comments/Cayenne/")

        self.assertIsInstance(response.context['comments'][0], Comment)
        self.assertIsInstance(response.context['car'],Car)
        self.assertIsInstance(response.context['comment_form'], CommentForm)
        self.assertEqual(response.context['average_rating'], 8.5)
        self.assertEqual(len(response.context['comments']), 2)