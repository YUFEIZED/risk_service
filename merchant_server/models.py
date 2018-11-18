from django.db import models

class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    credit = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
    	return self.customer_name + ':' + str(self.credit)
