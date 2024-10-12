from django.db import models
"""
CustomUser model extends the AbstractUser model provided by Django's authentication framework.
Additional fields:
- date_of_birth: DateField to store the user's date of birth (optional).
- city: CharField to store the user's city (optional).
- college: CharField to store the user's college (optional).
- team: CharField to store the user's team (optional).
The AbstractUser model includes the following fields:
- username: CharField for the username.
- first_name: CharField for the first name.
- last_name: CharField for the last name.
- email: EmailField for the email address.
- password: CharField for the password.
- groups: ManyToManyField for the groups the user belongs to.
- user_permissions: ManyToManyField for the user-specific permissions.
- is_staff: BooleanField indicating whether the user can log into the admin site.
- is_active: BooleanField indicating whether the user account is active.
- is_superuser: BooleanField indicating whether the user has all permissions.
- last_login: DateTimeField for the last login time.
- date_joined: DateTimeField for the date the user joined.
"""
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    """
    CustomUser extends the AbstractUser model to include additional fields.

    Attributes:
        date_of_birth (DateField): The user's date of birth. Optional.
        city (CharField): The city where the user resides. Optional.
        college (CharField): The college the user attends or attended. Optional.
        team (CharField): The team the user is associated with. Optional.
    """
    date_of_birth = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    college = models.CharField(max_length=100, null=True, blank=True)
    team = models.ForeignKey(
            'teams.Team',
            on_delete=models.SET_NULL,
            null=True,
            related_name='members_of'  # Change this to avoid conflict
        )

    class Meta:
        verbose_name = 'Custom User'
        verbose_name_plural = 'Custom Users'

    # Override groups field to avoid clash with the default User model
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Unique related name for CustomUser
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions '
                  'granted to each of their groups.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Unique related name for CustomUser
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

