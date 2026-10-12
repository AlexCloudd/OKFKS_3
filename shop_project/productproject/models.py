from django.db import models
from django.db import models
from django.contrib.auth.models import User

MAX_LENGTH = 255


class Category(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Наименование категории')
    description = models.TextField(null=True, blank=True, verbose_name='Описание категории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Collection(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Наименование коллекции')
    description = models.TextField(null=True, blank=True, verbose_name='Описание коллекции')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'


class Artist(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Имя исполнителя')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    country = models.CharField(max_length=100, null=True, blank=True, verbose_name='Страна')
    photo = models.ImageField(upload_to='artists/%Y/%m/%d/', null=True, blank=True, verbose_name='Фото исполнителя')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'


class Label(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Название лейбла')
    description = models.TextField(null=True, blank=True, verbose_name='Описание лейбла')
    country = models.CharField(max_length=100, null=True, blank=True, verbose_name='Страна')
    logo = models.ImageField(upload_to='labels/%Y/%m/%d/', null=True, blank=True, verbose_name='Логотип лейбла')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Лейбл'
        verbose_name_plural = 'Лейблы'


class Genre(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Название жанра')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class VinylFormat(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Формат')
    description = models.TextField(null=True, blank=True, verbose_name='Описание формата')
    speed = models.CharField(max_length=50, verbose_name='Скорость вращения')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Формат пластинки'
        verbose_name_plural = 'Форматы пластинок'


class Condition(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Состояние')
    description = models.TextField(null=True, blank=True, verbose_name='Описание состояния')
    grade = models.CharField(max_length=10, verbose_name='Оценка')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Состояние'
        verbose_name_plural = 'Состояния'


class Plate(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Наименование пластинки')
    description = models.TextField(null=True, blank=True, verbose_name='Описание пластинки')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    year = models.PositiveIntegerField(null=True, blank=True, verbose_name='Год выпуска')
    photo = models.ImageField(upload_to='plates/%Y/%m/%d/', null=True, blank=True, verbose_name='Изображение')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    is_exist = models.BooleanField(default=True, verbose_name='Доступна к заказу')

    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')
    collection = models.ManyToManyField(Collection, blank=True, verbose_name='Коллекции')
    artist = models.ForeignKey(Artist, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Исполнитель')
    label = models.ForeignKey(Label, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Лейбл')
    genre = models.ManyToManyField(Genre, blank=True, verbose_name='Жанры')
    vinyl_format = models.ForeignKey(VinylFormat, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Формат')
    condition = models.ForeignKey(Condition, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Состояние')

    def __str__(self):
        return f"{self.name} — {self.price} ₽"

    class Meta:
        verbose_name = 'Пластинка'
        verbose_name_plural = 'Пластинки'

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'В обработке'),
        ('confirmed', 'Подтверждён'),
        ('shipped', 'Отправлен'),
        ('delivered', 'Доставлен'),
        ('cancelled', 'Отменён'),
    ]

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name='Статус')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Общая сумма')
    
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Пользователь')

    def __str__(self):
        return f"Заказ №{self.id} - {self.user.username}"

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

class OrderItem(models.Model):
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена за единицу')
    
    order = models.ForeignKey(Order, on_delete=models.PROTECT, related_name='items')
    plate = models.ForeignKey('Plate', on_delete=models.PROTECT, verbose_name='Пластинка')

    def __str__(self):
        return f"{self.plate.name} x {self.quantity}"

    class Meta:
        verbose_name = 'Позиция заказа'
        verbose_name_plural = 'Позиции заказов'