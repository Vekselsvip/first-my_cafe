from django.db import models
from uuid import uuid4
from os import path
from django.core.validators import RegexValidator


class CategoryDish(models.Model):
    name = models.CharField(unique=True, max_length=50, db_index=True)
    is_visible = models.BooleanField(default=True)
    position = models.PositiveIntegerField(unique=True)

    class Meta:
        ordering = ('position',)

    def __str__(self):
        return f'{self.name}: {self.position}'


class Dish(models.Model):

    def get_file_name(self, filename):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join('images/dishes', filename)

    name = models.CharField(max_length=50, unique=True)
    photo = models.ImageField(upload_to=get_file_name)
    dish_order = models.PositiveSmallIntegerField()
    is_visible = models.BooleanField(default=True)
    is_special = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    ingredients = models.CharField(max_length=100, default='.')
    desc = models.CharField(max_length=150, unique=True)
    category = models.ForeignKey(CategoryDish, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}: {self.price}'


class ModelFormRegistration(models.Model):
    mobile_regex = RegexValidator(regex=r'^(/d{3}[- .]?){2}/d{4}$', message='Phone is format xxx xxx xxxx')
    name = models.CharField(max_length=50, db_index=True)
    email = models.EmailField()
    date = models.DateTimeField()
    count_of_people = models.PositiveIntegerField()
    message = models.TextField(max_length=150, blank=True)
    is_processed = models.BooleanField(default=False)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return f'{self.name}, {self.email}'


class ModelFormMessage(models.Model):
    name = models.CharField(max_length=15, db_index=True)
    email = models.EmailField()
    subject = models.CharField(max_length=20)
    message = models.TextField(max_length=200)
    is_processed = models.BooleanField(default=False)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return f'{self.name}, {self.email}'


class HeroSection(models.Model):

    def get_file_name(self, filename):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join('images/hero', filename)

    title = models.CharField(max_length=50, db_index=True)
    description = models.TextField(max_length=200)
    image = models.ImageField(upload_to=get_file_name)

    def __str__(self):
        return self.title


class AboutSection(models.Model):

    def get_file_name(self, filename):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return path.join('images/AboutSection', filename)

    title_1 = models.CharField(max_length=30)
    title_2 = models.CharField(max_length=30)
    desc_1 = models.TextField(max_length=150)
    desc_2 = models.TextField(max_length=150, blank=True)
    desc_3 = models.TextField(max_length=150, blank=True)
    feature_1 = models.TextField(max_length=100)
    feature_2 = models.TextField(max_length=100, blank=True)
    feature_3 = models.TextField(max_length=100, blank=True)
    image = models.ImageField(upload_to=get_file_name, default='')
    link = models.CharField(max_length=50, default='')

    def __str__(self):
        return f'{self.title_1} {self.title_2}'
