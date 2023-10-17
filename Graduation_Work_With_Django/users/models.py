from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models
from django.utils import timezone

from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, Group, Permission


class UserManager(BaseUserManager):
    def create_user(self, email, name, surname, lastname, password=None, is_admin=False, is_staff=False, is_active=True,):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        if not name:
            raise ValueError("User must have a name")
        if not surname:
            raise ValueError("User must have a surname")
        if not lastname:
            raise ValueError("User must have a lastname")
        user = self.model(
            email=self.normalize_email(email)
        )
        user.name = name
        user.surname = surname
        user.lastname = lastname
        user.set_password(password)  # change password to hash
        user.admin = is_admin
        user.staff = is_staff
        user.active = is_active
        user.save(using=self._db)
        return user

    def create_staffuser(self, email,  name, surname, lastname, password=None):
        user = self.create_user(
            email,
            name,
            surname,
            lastname,
            password=password,
            is_staff=True,
        )
        return user

    def create_superuser(self, email, name, surname, lastname, password=None):
        user = self.create_user(
            email,
            name,
            surname,
            lastname,
            password=password,
            is_staff=True,
            is_admin=True,
        )
        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True, verbose_name="e-mail")
    name = models.CharField(max_length=255, verbose_name="Имя")
    surname = models.CharField(max_length=255, verbose_name="Фамилия")
    lastname = models.CharField(max_length=255, verbose_name="Отчество")

    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'surname', 'lastname']  # Email & Password are required by default.



    list_display = ('email', 'name',)
    search_fields = ('name', 'email')

    objects = UserManager()

    def get_full_name(self):
        # The user is identified by their email address
        return self.email
    def get_full(self):
        return self.name + ' ' + self.surname
    def get_short_name(self):
         # The user is identified by their email address
         return self.email


    def __str__(self):              # __unicode__ on Python 2
         return self.surname +' ' + self.name  +' ' + self.lastname +' ' + self.email

    class Meta:
        verbose_name = "пользователя"
        verbose_name_plural = "Пользователи"

    @staticmethod
    def has_perm(perm, obj=None):
        return True

    @staticmethod
    def has_module_perms(app_label):
         # "Does the user have permissions to view the app `app_label`?"
         # Simplest possible answer: Yes, always
         return True

    @property
    def is_staff(self):
         # "Is the user a member of staff?"
         return self.staff

    @property
    def is_superuser(self):
         # "Is the user a admin member?"
         return self.admin

    @property
    def is_active(self):
         # "Is the user active?"
         return self.active
