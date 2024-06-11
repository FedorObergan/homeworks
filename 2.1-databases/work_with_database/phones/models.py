from django.db import models
from django.template.defaultfilters import slugify


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=50, null=False)
    price = models.IntegerField(null=False)
    image = models.CharField(max_length=100)
    release_date = models.DateField(max_length=50, null=False)
    lte_exists = models.BooleanField(null=False)
    slug = models.SlugField(blank=True, unique=True)

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
