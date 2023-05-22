from django.db import models


class Weapon(models.Model):
    """Модель оружия"""
    title = models.CharField(max_length=50, unique=True, verbose_name="Название")
    description = models.CharField(max_length=100, verbose_name="описание")
    caliber = models.CharField(max_length=10, null=True, blank=True, verbose_name="Калибр")
    barrel_length = models.IntegerField(default=2000, null=True, blank=True,
                                        verbose_name="Длина ствола")
    weight = models.IntegerField(default=2000, null=False, blank=False, verbose_name="Вес")
    price = models.IntegerField(default=2000, null=False, blank=False, verbose_name="Цена")
    # brand = models.ForeignKey()

    CHOICES = (
        ('FR', 'Огнестрельное'),
        ('SA', 'Холодное'),
    )

    type = models.CharField(max_length=50, choices=CHOICES, verbose_name="Тип")

    image = models.ImageField(upload_to="image/gun/", null=False, blank=False,
                              verbose_name="Изображение")

    class Meta:
        verbose_name = "Оружие"
        verbose_name_plural = "Оружие"

    def __str__(self):
        return self.title

