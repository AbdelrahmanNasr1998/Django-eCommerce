# Generated by Django 4.1.7 on 2023-02-21 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_images'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product_images',
            options={'verbose_name': 'Product Image', 'verbose_name_plural': 'Product Images'},
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
