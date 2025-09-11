from django.db import models


# Create your models here.
class Products(models.Model):
    prod_name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.IntegerField()
    size = models.DecimalField(max_digits=3, decimal_places=2)
    image = models.ImageField(upload_to='media/', null="Nothing")

    def __str__(self):
        return f"Product Name: {self.prod_name}, Price : {self.price}, Quantity :{self.quantity}, Size : {self.size}"
