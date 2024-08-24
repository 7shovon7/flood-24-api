from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.db.models.functions import Lower


class UserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('User must have an email address')
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, password, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)
    
    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True, **extra_fields)
    
    
class LowercaseEmailField(models.EmailField):
    """
    Override EmailField to convert emails to lowercase before saving.
    """
    def to_python(self, value):
        """
        Convert email to lowercase.
        """
        value = super(LowercaseEmailField, self).to_python(value)
        if isinstance(value, str):
            return value.lower()
        return value


class User(AbstractBaseUser, PermissionsMixin):
    class Meta:
        constraints = [
            models.UniqueConstraint(
                Lower('email'),
                name='user_email_ci_uniqueness',
            ),
        ]
        
    # ROLE_CHOICES = [ (r, r) for r in settings.K_CUSTOM_USER_ROLES ]

    email = LowercaseEmailField(unique=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    full_name = models.CharField(max_length=100)
    # user_role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=settings.K_CUSTOMER, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    objects = UserManager()
    
    def __str__(self) -> str:
        return f"{self.full_name} ({self.email})"
