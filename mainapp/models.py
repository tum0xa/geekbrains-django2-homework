from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(verbose_name="Название категории", max_length=64, unique=True)
    slug = models.SlugField(verbose_name="Url катергории", max_length=255, default="category")
    is_active = models.BooleanField(verbose_name='активна', default=True)
    description = models.TextField(verbose_name="Описание категории", blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Название товара", max_length=128, unique=True)
    slug = models.SlugField(verbose_name="Url товара", max_length=255, default="product")
    full_description = models.TextField(verbose_name="Подробное описание", blank=True)
    short_description = models.CharField(verbose_name="Краткое описание товара", max_length=255, blank=True)

    image = models.ImageField(verbose_name="Основное изображение", upload_to='product_images', blank=True, max_length=255)
    image_zoom = models.ImageField(verbose_name="Большое изображение", upload_to='product_images', blank=True)

    image_1 = models.ImageField(verbose_name="Изображение 1", upload_to='product_images', blank=True)
    image_2 = models.ImageField(verbose_name="Изображение 2", upload_to='product_images', blank=True)
    image_3 = models.ImageField(verbose_name="Изображение 3", upload_to='product_images', blank=True)
    image_4 = models.ImageField(verbose_name="Изображение 4", upload_to='product_images', blank=True)

    image_1_big = models.ImageField(verbose_name="Изображение 1 Большое", upload_to='product_images', blank=True)
    image_2_big = models.ImageField(verbose_name="Изображение 2 Большое", upload_to='product_images', blank=True)
    image_3_big = models.ImageField(verbose_name="Изображение 3 Большое", upload_to='product_images', blank=True)
    image_4_big = models.ImageField(verbose_name="Изображение 4 Большое", upload_to='product_images', blank=True)

    text_alt = models.CharField(verbose_name="Текст изображения", max_length=128, default="image")
    discount = models.DecimalField(verbose_name="Скидка", max_digits=2, decimal_places=0, default=0)
    old_price = models.DecimalField(verbose_name="Цена", max_digits=8, decimal_places=2, default=0)
    age = models.CharField(verbose_name="Возрастная категория", max_length=3, default='3+')
    quantity = models.PositiveIntegerField(verbose_name="Наличие", default=0)
    ratting = models.FloatField(verbose_name="Рейтинг", default=0)

    @property
    def price(self):
        result = self.old_price*(1 - self.discount/100)
        return result

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name


class Banner(models.Model):
    name = models.CharField(verbose_name="Название баннера", max_length=128, unique=True)
    text_top = models.CharField(verbose_name="Текст на баннере (верхняя строка)", max_length=15, blank=True)
    text_bottom = models.CharField(verbose_name="Текст на баннере (нижняя строка)", max_length=15, blank=True)
    text_discount = models.CharField(verbose_name="Текст на баннере (Размер скидки)", max_length=15, blank=True)
    text_button = models.CharField(verbose_name="Текст на кнопке", max_length=15, blank=True)
    image = models.ImageField(verbose_name="Изображение", upload_to='product_images', blank=True)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(verbose_name="Название организации", max_length=255, unique=True)
    phone = models.CharField(verbose_name="Номер телефона", max_length=20, blank=True, default="-")

    def __str__(self):
        return self.name


class Contact(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Имя", max_length=50, unique=True)
    number = models.CharField(verbose_name="Номер телефона", max_length=20, blank=True, default="-")
    email = models.EmailField(verbose_name="E-mail", blank=True, default="-")
    is_main = models.BooleanField(verbose_name="Основной", default=False)


class Address(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Название", max_length=255)
    city = models.CharField(verbose_name="Город", max_length=50)
    street = models.CharField(verbose_name="Улица", max_length=50)
    building = models.SmallIntegerField(verbose_name="Номер здания, дома")
    office = models.SmallIntegerField(verbose_name="Номер офиса", blank=True)

