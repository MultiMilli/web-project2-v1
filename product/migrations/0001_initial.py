# Generated by Django 3.2.11 on 2022-08-22 21:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FilterBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name_plural': 'Brand filter',
            },
        ),
        migrations.CreateModel(
            name='FilterCountry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name_plural': 'Country filter',
            },
        ),
        migrations.CreateModel(
            name='FilterMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name_plural': 'Material filter',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Product Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='product_images')),
                ('image1', models.ImageField(blank=True, upload_to='product_images')),
                ('image2', models.ImageField(blank=True, upload_to='product_images')),
                ('image3', models.ImageField(blank=True, upload_to='product_images')),
                ('name', models.CharField(max_length=256)),
                ('price', models.IntegerField(default=0)),
                ('product_code', models.IntegerField(default=0)),
                ('exist', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True)),
                ('country', models.CharField(blank=True, max_length=64)),
                ('brand_name', models.CharField(blank=True, max_length=64)),
                ('gender', models.CharField(blank=True, max_length=12)),
                ('mechanism', models.CharField(blank=True, max_length=64)),
                ('case_material', models.CharField(blank=True, max_length=64)),
                ('waterproof', models.CharField(blank=True, max_length=64)),
                ('warranty', models.CharField(blank=True, default=12, max_length=64)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.productcategory')),
            ],
            options={
                'verbose_name_plural': 'Products',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
