from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.contrib.auth.models import UserManager as BaseUserManager
from PIL import Image


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_cooker', False)
        extra_fields.setdefault('is_customer', False)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        if user.is_cooker:
            cooker_group, _ = Group.objects.get_or_create(name='Cooker')
            user.groups.add(cooker_group)
        if user.is_customer:
            customer_group, _ = Group.objects.get_or_create(name='Customer')
            user.groups.add(customer_group)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    is_cooker = models.BooleanField('Статус кондитера', default=False)
    is_customer = models.BooleanField('Статус заказчика', default=False)
    # add related_name argument to resolve clashes with reverse relation names
    groups = models.ManyToManyField(Group, blank=True, related_name='users_in_group')

    objects = UserManager()

    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name='users_with_permission',
        verbose_name=('user permissions')
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=100, default='Россия')
    city = models.CharField(max_length=100, default='Москва')
    phone = models.CharField(max_length=11, null=True)
    description = models.TextField(null=True)
    image = models.ImageField(default='profile_pics/default.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} профиль'

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)