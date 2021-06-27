from django.db import models


# Create your models here.
class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    email_address = models.EmailField(max_length=100)
    subscription_type = models.CharField(max_length=5)

    def __str__(self):
        return self.customer_name
