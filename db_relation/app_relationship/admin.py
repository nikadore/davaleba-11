from django.contrib import admin
from .models import Author, AuthorProfile, Book, Genre

admin.site.register(Author)
admin.site.register(AuthorProfile)
admin.site.register(Book)
admin.site.register(Genre)