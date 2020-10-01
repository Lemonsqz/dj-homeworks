from django.db import models
from django.shortcuts import reverse


class Product(models.Model):
    name = models.CharField(max_length=50, null=True)
    img = models.FileField(upload_to='products/%Y/%m/%d/')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail", kwargs={
            'slug': self.slug
        })


class Review(models.Model):
    text = models.TextField(null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return ' ' + self.text[:50]
