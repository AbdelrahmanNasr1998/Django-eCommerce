# Generated by Django 4.1.7 on 2023-02-23 10:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_newuser_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=128)),
                ('phone_number', models.PositiveIntegerField(max_length=16)),
                ('street_name', models.CharField(max_length=64)),
                ('building_number', models.PositiveIntegerField(max_length=8)),
                ('apartment_number', models.PositiveIntegerField(max_length=8)),
                ('city', models.CharField(max_length=32)),
                ('landmark', models.CharField(max_length=32)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]