from django.contrib import admin

# Register your models here.
from .models import Car, Image, Comment

admin.site.register(Car)
admin.site.register(Image)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'car', 'rating', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body', 'rating')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)