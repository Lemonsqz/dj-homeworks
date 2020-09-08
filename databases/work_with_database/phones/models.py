from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    id = models.AutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    price = models.IntegerField(null=True)
    image = models.ImageField(null=True, blank=True)
    release_date = models.DateField(null=True)
    lte_exists = models.BooleanField(null=True)
    slug = models.TextField(blank=True, null=True)

    def name_slug(self):
        return slugify(self.name)


