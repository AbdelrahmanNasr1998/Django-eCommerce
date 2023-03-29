from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=32, unique=True)
    image = models.ImageField(upload_to='uploads/category/')

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey('products.Category', on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    description = models.TextField()
    price = models.FloatField()
    items = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Product_Images(models.Model):
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='product_image_obj')
    image = models.ImageField(upload_to='uploads/Product_Images/')

    def __str__(self):
        return str(self.product)

    class Meta:
        verbose_name = ("Product Image")
        verbose_name_plural = ("Product Images")