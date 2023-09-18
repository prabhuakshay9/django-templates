from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from simple_history.models import HistoricalRecords


class CustomUserManager(BaseUserManager):
    """ Custom User Manager for CustomUser Model. """

    def create_user(self, email, password=None, **extra_fields):
        """ Method to create a Base CustomUser """

        if not email:
            raise ValueError("The Email field must be set")

        # Normalize the email address (convert to lowercase) and create a user instance.
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)  # Set the user's password securely.
        user.save()  # Save the user to the database.
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """ Method to create a superuser with staff and superuser privileges. """

        # Set default values for is_staff and is_superuser if not provided.
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        # Ensure that is_staff and is_superuser are True for a superuser.
        if (extra_fields.get("is_staff") is not True
                or extra_fields.get("is_superuser") is not True):
            raise ValueError("Superuser must have is_staff=True and is_superuser=True.")

        # Call the create_user method to create the superuser.
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    """ A Custom user model that extends AbstractUser. """

    # Replace the username field with an email field that must be unique.
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)

    # Remove the username, first_name and last_name field as it's not needed.
    first_name = None
    last_name = None
    username = None

    # Add historical records tracking to the model.
    history = HistoricalRecords()

    objects = CustomUserManager()  # Use the custom user manager for user creation.

    # Set the email field as the username field for authentication.
    USERNAME_FIELD = "email"

    # No additional required fields for user creation.
    REQUIRED_FIELDS = []

    # Define a human-readable string representation of the user (email).
    def __str__(self):
        return self.email

    # Overwrite get_full_name method
    def get_full_name(self):
        return self.name

    # Overwrite get_short_name method
    def get_short_name(self):
        return self.name.split(" ")[0]

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
