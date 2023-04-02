from django.db import models


class Phone(models.Model):
    id = models.CharField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    image = models.CharField()
    release_date = models.CharField()
    lte_exists = models.CharField()
    slug = models.SlugField(max_length=50)

    # TODO: Добавьте требуемые поля

