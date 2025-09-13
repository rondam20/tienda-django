from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True, blank=True)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ["name"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=3, default="COP")  # COP, MXN, USD...
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


SIZES = [("XS","XS"),("S","S"),("M","M"),("L","L"),("XL","XL"),("XXL","XXL")]

class StockItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="stock_items")
    size = models.CharField(max_length=4, choices=SIZES)
    quantity = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ("product", "size")
        verbose_name = "Stock por talla"
        verbose_name_plural = "Stock por talla"

    def __str__(self):
        return f"{self.product.name} - {self.size} ({self.quantity})"
