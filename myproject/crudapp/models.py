from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.FloatField()
    description=models.TextField()
    image=models.ImageField(upload_to='products/')
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'product name: {self.name} price: {self.price} '