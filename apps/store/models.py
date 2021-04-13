from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200)

    title = models.CharField(max_length=80)
    subtitle = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True, null=True)

    price=models.DecimalField(decimal_places=2, max_digits=1000)

    
    def __str__(self):
        return self.title