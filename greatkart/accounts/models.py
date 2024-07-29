from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager


class MyAccountManager(BaseUserManager):
    def create_user(self, nom, prenom, username, email, password=None):
        if not email:
            raise ValueError("l'utilisateur doit avoir une adresse email")
        
        if not username :
            raise ValueError("l'utilisateur doit avoir un nom ")
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            nom = nom,
            prenom = prenom,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, nom='gtgt', prenom='gtgt', email='dani@gmail.com', username='gtgt', password=None):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password=password,
            nom = nom,
            prenom = prenom,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user



class Account(AbstractBaseUser):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    username = models.CharField(max_length=50,unique=True)
    email = models.EmailField(max_length=100,unique=True)
    phone_number = models.CharField(max_length=50)

    #requise
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_activate = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIERED_FIELDS = 'username'

    objects = MyAccountManager()

    def __str__(self):
        return self.email
    
    def has_perm(self,perm,obj=None):
        return self.is_admin
    
    def has_module_perms(self, add_label):
        return True
        

