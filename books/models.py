from django.db import models
from django.core.validators import MinValueValidator

class Book(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    genre=models.CharField(max_length=150)
    isbn=models.CharField(max_length=13, unique=True)
    available_copies=models.IntegerField(validators=[MinValueValidator(0)])
    total_copies=models.IntegerField(validators=[MinValueValidator(0)])
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["id"]
