from .models import Comment
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body', 'rating')
    
    def clean_name(self):
        name = self.cleaned_data['name']
        invalid_characters = ['!', '@', "#"]
        if not name:
            return name
        
        if not name[0].isupper():
            self.add_error('name', "Should start with an uppercase letter")
        
        if name.endswith('.'):
            self.add_error('name', "Should not end with a full stop")
        
        if not name.isalpha():
            self.add_error('name', "Should contain only letters (a-z/A-Z)")
        return name

    def clean_rating(self):
        rating = self.cleaned_data['rating']
        if not rating:
            return rating

        if rating not in range(1,10):
            self.add_error('rating', "Rating should be between 1 and 10")

        return rating