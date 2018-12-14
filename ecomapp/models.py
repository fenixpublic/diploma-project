from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=100)
    slug = models.SlugField()

    def __str__(self):
        return self.name


def img_folder(instance, filename):
    filename = instance.slug + '.' + filename.split('.')[-1]
    return '{}/{}'.format(instance.slug, filename)


class Product(models.Model):

    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.TextField()
    image = models.ImageField(upload_to=img_folder)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title
