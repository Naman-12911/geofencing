from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from account.managers import CustomUserManager
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import AbstractUser, Group, Permission


AUTH_PROVIDERS = {'email': 'email'}
class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    phone_no = models.CharField(unique=True,  null=True,max_length=10)
    name = models.CharField(max_length=100,null=True)
    user = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    auth_provider = models.CharField(max_length=255, blank=False, null=False, default=AUTH_PROVIDERS.get('email'))
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Set a unique related_name
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups'
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',  # Set a unique related_name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    USERNAME_FIELD = 'email'
    objects = CustomUserManager() 
    REQUIRED_FIELDS = []
    def __str__(self):
        return self.email
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }