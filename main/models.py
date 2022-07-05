from django.db import models

class Tovari(models.Model):
    title = models.CharField("Название", max_length=250)
    photo_1 = models.ImageField("Фото 1")
    photo_2 = models.ImageField("Фото 2")
    photo_3 = models.ImageField("Фото 3")
    photo_4 = models.ImageField("Фото 4")
    photo_5 = models.ImageField("Фото 5")
    photo_6 = models.ImageField("Фото 6")
    photo_7 = models.ImageField("Фото 7")
    photo_8 = models.ImageField("Фото 8")
    about = models.TextField("О товаре")
    price = models.CharField("Цена", max_length=20, blank=True)
    tema = models.CharField("Тема", max_length=20)
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
    def __str__(self):
        return f'{self.title} {self.photo_1} {self.photo_2} {self.photo_3} {self.photo_4} {self.photo_5} {self.photo_6} ' \
               f'{self.photo_7} {self.photo_8} {self.about} {self.price} {self.tema}'

class magasin_base(models.Model):
    title = models.CharField("Название", max_length=250)
    photo_1 = models.ImageField("Фото 1")
    photo_2 = models.ImageField("Фото 2")
    photo_3 = models.ImageField("Фото 3")
    photo_4 = models.ImageField("Фото 4")
    photo_5 = models.ImageField("Фото 5")
    photo_6 = models.ImageField("Фото 6")
    photo_7 = models.ImageField("Фото 7")
    photo_8 = models.ImageField("Фото 8")
    about = models.TextField("О товаре")
    price = models.CharField("Цена", max_length=20, blank=True)
    tema = models.CharField("Тема", max_length=20)
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
    def __str__(self):
        return f'{self.title} {self.photo_1} {self.photo_2} {self.photo_3} {self.photo_4} {self.photo_5} {self.photo_6} ' \
               f'{self.photo_7} {self.photo_8} {self.about} {self.price} {self.tema}'



class base_magasin(models.Model):
    title = models.CharField("Название", max_length=250)
    photo_1 = models.ImageField("Фото 1", blank=True)
    photo_2 = models.ImageField("Фото 2", blank=True)
    photo_3 = models.ImageField("Фото 3", blank=True)
    photo_4 = models.ImageField("Фото 4", blank=True)
    photo_5 = models.ImageField("Фото 5", blank=True)
    photo_6 = models.ImageField("Фото 6", blank=True)
    photo_7 = models.ImageField("Фото 7", blank=True)
    photo_8 = models.ImageField("Фото 8", blank=True)
    about = models.TextField("О товаре")
    price = models.CharField("Цена", max_length=20, blank=True)
    tema = models.CharField("Тема", max_length=20)
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
    def __str__(self):
        return f'{self.title} {self.photo_1} {self.photo_2} {self.photo_3} {self.photo_4} {self.photo_5} {self.photo_6} ' \
               f'{self.photo_7} {self.photo_8} {self.about} {self.price} {self.tema}'