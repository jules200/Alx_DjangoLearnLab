from django.db import models

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, date_of_birth, profile_photo=None, password=None, **extra_fields):
        """
        Create and return a regular user with the given username, email, date of birth, and profile photo.
        """
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, date_of_birth=date_of_birth, profile_photo=profile_photo, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, date_of_birth, profile_photo=None, password=None, **extra_fields):
        """
        Create and return a superuser with the given username, email, date of birth, and profile photo.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, date_of_birth, profile_photo, password, **extra_fields)
class CustomUser(AbstractUser):
    date_of_birth = models.DateField()
    profile_photo = models.ImageField()
    
    objects = CustomUserManager()
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    
    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        
        permissions=[
            ("can_create", "can_delete"),
            ("can_edit", "user can edit"),
            ("can_view", "user can add"),
        ]