from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.


class Currency(models.Model):
    Наименование = models.CharField(max_length=30, primary_key=True)
    Код = models.CharField(max_length=3, unique=True)
    За_единица = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    Лева = models.DecimalField(max_digits=10, decimal_places=5)

    class Meta:
        ordering = ('Наименование',)

    def __str__(self):
        return self.Наименование