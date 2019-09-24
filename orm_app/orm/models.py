from django.db import models
from django.contrib import admin
from.models import Author

# Create new model for Author
#     Author should have properties for first_name and last_name
#     Create a new model for Post
#     Post should have properties for title, content, date_posted, and author -- date_posted should automatically populate with current date on create -- author should be a foreign key that points back to the Author of the post(s)


from django.utils import timezone

class Author(models.Model):
    author_text = models.CharField(max_length=200)
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)




class Post(models.Model):
    post_text = models.ForeignKey(Author, on_delete=models.CASCADE)
    title_text = models.CharField(max_length=200)
    content_text=models.CharField(max_length=200)
    date_posted=models.CharField(max_length=200)

