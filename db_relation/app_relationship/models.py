from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class AuthorProfile(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE, related_name='profile')
    biography = models.TextField()
    birth_date = models.DateField()

    def __str__(self):
        return f"profile of {self.author}"

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    genres = models.ManyToManyField(Genre, related_name='books', blank=True)

    def __str__(self):
        return f"{self.title} (by {self.author})"

