from django.db import models

# Create your models here.


class Books(models.Model):
    studentid = models.CharField(max_length=14)
    book_name = models.CharField(max_length=50)
    branch_name = models.CharField(max_length=50)

    def __str__(self):
            return self.book_name
