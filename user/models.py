from django.db import models
from django.contrib.auth.models import User

class userProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(
        max_length =20,
        choices = [('admin', 'Admin'), ('customer', 'Customer')],
        default = 'customer'
    )

    gender = models.CharField(
        max_length = 10,
        choices = [('male', 'Male'),('female','Female')],
        blank = True,
        null = True
    )
    country = models.CharField(max_length=100, blank=True, null=True)

    def __str(self):
        return f"{self.role}-{self.user.username}"
