from django.db import models
from base.models import BaseModel
from django.utils.text import slugify


class Category(BaseModel):
    name = models.CharField(max_length=100)  # test expects "name"
    slug = models.SlugField(unique=True, null=True, blank=True)
    category_image = models.ImageField(upload_to="categories", null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class ColorVariant(BaseModel):
    color_name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.color_name


class SizeVariant(BaseModel):
    size_name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.size_name


class Product(BaseModel):
    title = models.CharField(max_length=100)  # test expects "title"
    slug = models.SlugField(unique=True, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    price = models.IntegerField()
    product_description = models.TextField(null=True, blank=True)
    color_variant = models.ManyToManyField(ColorVariant, blank=True)
    size_variant = models.ManyToManyField(SizeVariant, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_images")
    image = models.ImageField(upload_to="product")

    def __str__(self):
        return f"{self.product.title} Image"
