from django.db import models
from django.urls import reverse


class CategoryCard(models.Model):
    cat_id = models.SlugField('id категории', max_length=100, db_index=True, unique=True)
    category_title = models.CharField('Название категорий', max_length=100)
    category_photo = models.CharField('URL фото категорий', max_length=100)

    def __str__(self):
        return self.cat_id

    def get_absolute_url(self):
        return reverse('catalog', kwargs={'catalog_id': self.cat_id})

    class Meta:  # Для удобства в админке
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Tovar(models.Model):
    tovar_id = models.SlugField('id товара', max_length=100, db_index=True, unique=True)
    tovar_title = models.CharField('Название товара', max_length=100)
    tovar_price = models.IntegerField('Цена товара')
    tovar_discription = models.CharField('Описание', max_length=500)
    tovar_photo = models.CharField('URL фото товара', max_length=100)
    cat = models.ForeignKey(CategoryCard,
                                to_field='cat_id',
                                unique=False,
                                on_delete=models.CASCADE)

    class Meta:  # Для удобства в админке
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.tovar_title

    def get_absolute_url(self):
        return reverse('tovar', kwargs={'catalog_id': self.cat,
                                        'tov_id': self.tovar_id})
