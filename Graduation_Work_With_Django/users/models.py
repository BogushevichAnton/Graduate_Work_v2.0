from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models
from django.utils import timezone

from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, Group, Permission

from Subdivisions.models import Subdivisions



class Positions(models.Model):
    positions = models.CharField(max_length=255, verbose_name="Наименование должности")

    list_display = ('positions', )
    search_fields = ['positions', ]

    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"

        permissions = [
            ("users.position_add", "Добавление должностей"),
            ("users.position_change", "Изменение должностей"),
            ("users.position_delete", "Удаление должностей"),
            ("users.position_id", "Просмотр должности"),

            ("users.position_all", "Просмотр всех должностей в таблице"),
        ]

    def __str__(self):
        return self.positions


class UserManager(BaseUserManager):
    def create_user(self, email, name, surname, lastname, password=None):
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
        user.fullname = surname + ' ' + name + ' ' + lastname
        user.set_password(password)  # change password to hash

        user.is_staff = True
        user.is_active = True
        user.is_superuser = True

        user.save(using=self._db)
        return user

    #def create_staffuser(self, email,  name, surname, lastname, password=None):
        #user = self.create_user(
            #email,
           # name,
            #surname,
            #lastname,
            #password=password,
            #is_staff=True,
        #)
        #return user

    def create_superuser(self, email, name, surname, lastname, password=None):
        user = self.create_user(
            email,
            name,
            surname,
            lastname,
            password=password,
        )
        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True, verbose_name="e-mail")
    name = models.CharField(max_length=50, verbose_name="Имя")
    surname = models.CharField(max_length=50, verbose_name="Фамилия")
    lastname = models.CharField(max_length=50, verbose_name="Отчество")
    subdivision = models.ForeignKey(Subdivisions, on_delete = models.SET_DEFAULT, default=1, verbose_name='Подразделение', blank=True)
    fullname = models.CharField(max_length=255, verbose_name="Полное имя", default='Нет полного имени')

    position = models.ForeignKey(Positions, on_delete = models.SET_DEFAULT, verbose_name='Должность', blank=True, default=10)
    # default - должность с наименованием "нет должности"

    is_staff = models.BooleanField(u'staff status', default=False,
                                   help_text=u'Designates whether the user can log into this admin '
                                             'site.')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'surname', 'lastname']  # Email & Password are required by default.
    list_display = ('id', 'email', 'name', 'surname', 'lastname','position', 'subdivision')
    search_fields = ['email', 'name', 'surname', 'lastname', 'subdivision' ]
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
         return self.surname +' ' + self.name  +' ' + self.lastname + ' Подразделение: ' + self.subdivision.abbreviation

    class Meta:
        verbose_name = "Пользователя"
        verbose_name_plural = "Пользователи"

        permissions = [
            ("users.user_id", "Просмотр пользователей"),
            ("users.user_delete", "Удаление пользователей"),

            ("users.user_all", "Просмотр всех пользователей в таблице"),
        ]

