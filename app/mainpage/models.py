from django.db import models
from django.utils import timezone


class Order(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    phone = models.CharField(max_length=20)  # Предполагается, что номер телефона - это строка фиксированной длины
    desc = models.TextField()  # TextField подходит для длинного текста

    def __str__(self):
        return f"Заявка от {self.phone}"


