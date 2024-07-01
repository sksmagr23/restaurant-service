from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='food_images/', blank=True, null=True)
    rating = models.PositiveSmallIntegerField(default=0, choices=[(i, i) for i in range(6)])

    def _str_(self):
        return self.name