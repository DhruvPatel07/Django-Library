from django.db import models

# Create your models here.


class Books(models.Model):
    book_name = models.CharField(max_length=50)
    Author_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")

    def __str__(self):
            return self.book_name
