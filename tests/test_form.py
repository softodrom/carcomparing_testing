from django.test import TestCase

from cars.forms import CommentForm

class CommentFormTests(TestCase):
    def test_name_starting_lowercase(self):
        form = CommentForm(data={'name': 'joe'})

        self.assertEqual(form.errors['name'], ["Should start with an uppercase letter"])

    def test_name_ending_full_stop(self):
        form = CommentForm(data={'name': "Joe."})

        self.assertEqual(form.errors['name'], ["Should not end with a full stop", "Should contain only letters (a-z/A-Z)"])

    def test_name_contains_invalid_characters(self):
        form = CommentForm(data={'name':'J#oe'})

        self.assertEqual(form.errors['name'], ["Should contain only letters (a-z/A-Z)"])

    def test_a_invalid_email(self):
        form = CommentForm(data={'email': "mom@you"})

        self.assertEqual(form.errors['email'], ["Enter a valid email address."])

    def test_rating_not_in_the_range(self):
        form = CommentForm(data={'rating': 11})

        self.assertEqual(form.errors['rating'], ["Rating should be between 1 and 10"])