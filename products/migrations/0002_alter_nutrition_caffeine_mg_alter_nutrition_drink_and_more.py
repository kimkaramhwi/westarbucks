# Generated by Django 4.0.2 on 2022-02-11 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nutrition',
            name='caffeine_mg',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='nutrition',
            name='drink',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.drink'),
        ),
        migrations.AlterField(
            model_name='nutrition',
            name='one_serving_kca',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='nutrition',
            name='protein_g',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='nutrition',
            name='saturated_fat_g',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='nutrition',
            name='size',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.size'),
        ),
        migrations.AlterField(
            model_name='nutrition',
            name='sodium_mg',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='nutrition',
            name='sugars_g',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
