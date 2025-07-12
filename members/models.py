from django.db import models
from django.core.validators import EmailValidator

class Member(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True, validators=[EmailValidator()])
    membership_date=models.DateField(auto_now_add=True)
    is_active=models.BooleanField(default=True)

    def __sr__(self):
        return self.name

    class Meta:
        ordering=['id']
