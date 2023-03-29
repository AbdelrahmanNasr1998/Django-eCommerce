from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.db import models
import datetime

class CustomAccountManager(BaseUserManager):
    def create_user(self, email, username, password, **other_fields):
        if not email:
            raise ValueError(_('You must provide an email address'))
        # convert all in lowercase
        email = self.normalize_email(email)
        user = self.model(email=email, username=username,
                          **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')
        return self.create_user(email, username, password, **other_fields)

class NewUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=16, unique=True)
    email = models.EmailField(_('email address'), max_length=32, unique=True)
    start_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_block = models.BooleanField(default=False)

    objects = CustomAccountManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', ]

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = ("User")
        verbose_name_plural = ("Users")

class Address(models.Model):
    user = models.ForeignKey('users.NewUser', on_delete=models.CASCADE)
    full_name = models.CharField(max_length=128)
    phone_number = models.PositiveIntegerField()
    street_name = models.CharField(max_length=64)
    building_number = models.PositiveIntegerField()
    apartment_number = models.PositiveIntegerField()
    city = models.CharField(max_length=32)
    landmark = models.CharField(max_length=32)

    def __str__(self):
        return str(self.user)

class Favorite(models.Model):
    user = models.ForeignKey('users.NewUser', on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)

class Cart(models.Model):
    user = models.ForeignKey('users.NewUser', on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    items = models.PositiveIntegerField()
    price = models.FloatField()

    def __str__(self):
        return str(self.user)
