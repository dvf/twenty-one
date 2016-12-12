from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Cannot create a User without an Email')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    GENDER_CHOICES = (
        ('m', 'Male',),
        ('f', 'Female',),
        ('o', 'Other',),
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    email = models.EmailField(unique=True, max_length=200)
    date_of_birth = models.DateField(null=True, blank=True)

    # Determines if the user has an active account
    is_active = models.BooleanField(default=True)
    # Determines if the user is staff or not (may log into admin)
    is_staff = models.BooleanField(default=False)
    # Determines if the user is a superuser
    is_superuser = models.BooleanField(default=False)

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    # Social Stuff from Facebook etc.
    education = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    # Activity
    last_seen_ip = models.GenericIPAddressField(null=True, blank=True)
    last_seen_time = models.DateTimeField(null=True, blank=True)

    # Initial Fields
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email
