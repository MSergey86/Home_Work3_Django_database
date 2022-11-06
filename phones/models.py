from django.db import models


class Phone(models.Model):

    id = models.PositiveIntegerField(primary_key=True, verbose_name='id')
    name = models.CharField(max_length=100, verbose_name='name')
    price = models.DecimalField(verbose_name='price', max_digits=10, decimal_places=2)
    image = models.URLField(max_length=200, verbose_name='image')
    release_date = models.DateField(auto_now=False, auto_now_add=False, verbose_name='release_date')
    lte_exists = models.BooleanField(default=True)
    slug = models.SlugField(max_length=150, unique=True)