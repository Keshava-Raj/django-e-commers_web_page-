# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
 
 
# class Usermanager(BaseUserManager):
#      def create_user(self,first_name,last_name,email,username,password=None):
#          if not email:
#              raise ValueError('Enter a Valid e-mail address')
#          if not email:
#              raise ValueError('Enter a Valid e-mail address')
#          user = self.model(
#              email = self.normalize_email(email),
#              first_name = first_name,
#              last_name = last_name,
#              username = username,
#          )
#          user.set_password(password)
#          user.save(using=self._db)
#          return user
#      def create_superuser(self,first_name,last_name,email,username,password=None):
#          user = self.create_user(
#              email = self.normalize_email(email),
#              first_name = first_name,
#              password=password,
#              last_name = last_name,
#              username = username, 
#          )
#          user.is_admin = True
#          user.is_active = True
#          user.is_staff = True
#          user.is_superuser = True
#          user.save(using=self._db)
#          return user

# class Register_form(AbstractBaseUser):
#     name = models.CharField(max_length=30)
#     email = models.EmailField(max_length=30)
#     mobile = models.BigIntegerField()
#     age = models.IntegerField()
#     passewrd = models.CharField( max_length=16)
#     passewrd1 = models.CharField(max_length=16)

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, first_name, phone_no, email,age, username, password=None):
        if not email:
            raise ValueError('Enter a Valid e-mail address')
        
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            mobile=phone_no,
            username=username,
            age = age
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, username, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Register_form(AbstractBaseUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True, max_length=255)
    username = models.CharField(unique=True, max_length=30)
    mobile = models.BigIntegerField()
    age = models.IntegerField()

    # Additional fields for user status
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser


