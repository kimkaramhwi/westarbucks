from django.db import models

class Category(models.Model):
    menu = models.ForeignKey('menu', on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    class Meta:
        db_table = 'categories'

class Menu(models.Model):
    name = models.CharField(max_length=40)

    class Meta:
        db_table = 'menu'  


class Drink(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    korean_name = models.CharField(max_length=40)
    english_name = models.CharField(max_length=40)
    description = models.TextField()

    class Meta:
        db_table = 'drinks'

class Allergy_Drink(models.Model):
    allergy = models.ForeignKey('Allergy', on_delete=models.CASCADE)
    drink     = models.ForeignKey('Drink', on_delete=models.CASCADE)

    class Meta:
        db_table = 'allergy_drink'

class Allergy(models.Model):
    name     = models.CharField(max_length=40, default="")
    drink_set = models.ManyToManyField(Drink, through=Allergy_Drink)

    class Meta:
        db_table = 'allergy'

class Nutrition(models.Model):
    one_serving_kca = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    sodium_mg = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    saturated_fat_g = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    sugars_g = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    protein_g = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    caffeine_mg = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    drink = models.ForeignKey('Drink', on_delete=models.CASCADE, null=True)
    size = models.ForeignKey('Size', on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'nutritions'

class Image(models.Model):
    image_url = models.CharField(max_length=1000)
    drink     = models.ForeignKey('Drink', on_delete=models.CASCADE)

    class Meta:
        db_table = 'images'

class Size(models.Model):
    name     = models.CharField(max_length=40)
    size_ml = models.CharField(max_length=40, null=True)
    size_fluid_ounce = models.CharField(max_length=40, null=True)

    class Meta:
        db_table = 'sizes'