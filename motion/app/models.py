from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyUserManager(BaseUserManager):
    def create_user(self, email, username, firstname, lastname, password=None):
        if not email:
            raise ValueError("Email is required")
        if not username:
            raise ValueError("Username is required")
        if not firstname:
            raise ValueError("First Name is required")
        if not lastname:
            raise ValueError("Last Name is require")
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            firstname = firstname,
            lastname = lastname
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, firstname, lastname, password=None):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            firstname = firstname,
            lastname = lastname,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    email = models.EmailField(verbose_name="Email address", max_length=60, unique=True)
    username = models.CharField(verbose_name="Username", max_length=60, unique=True)
    firstname = models.CharField(verbose_name="First Name", max_length=200)
    lastname = models.CharField(verbose_name="Last Name", max_length=200)
    date_joined = models.DateTimeField(verbose_name="Date Joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="Last Login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username', 'firstname', 'lastname']
    objects = MyUserManager()

    def __str__(self):
        return self.firstname

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

class Package(models.Model):
    name = models.CharField(max_length=255)
    percent_per_day = models.CharField(max_length=255)
    days = models.CharField(max_length=255)
    returns = models.CharField(max_length=255)
    min_amount = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} Package'

class List(models.Model):
    option_one = models.CharField(max_length=255, default="text")
    option_two = models.CharField(max_length=255, default="text")
    option_three = models.CharField(max_length=255, default="text")
    option_four = models.CharField(max_length=255, default="text")
    package = models.OneToOneField(Package, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.package} Data'
        
class Interest(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, null=True)
    amount = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.user}'

class Referral_reward(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, null=True)
    amount = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.user}'

class Dividens(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, null=True)
    amount = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.user}'


class Deposit(models.Model):
    name = models.CharField(max_length=255, default='John doe')
    amount = models.CharField(max_length=50)


    def __str__(self):
        return f'{self.name} Deposited ${self.amount}'

class Withdraw(models.Model):
    name = models.CharField(max_length=255, default='John Doe')
    amount = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} Withdraw ${self.amount}'


class Error(models.Model):
    message = models.CharField(max_length=255, default='Error processing result')

    def __str__(self):
        return f'{self.message}'

class Setting(models.Model):
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
    youtube_link = models.URLField(max_length=255, default='https://www.youtube.com/watch?v=41JCpzvnn_0&feature=youtu.be')
    btc_address = models.CharField(max_length=255, default="btcaddress")

    def __str__(self):
        return f'{self.address}'

class Proof(models.Model):
    username = models.CharField(max_length=200)
    image = models.ImageField(upload_to='proof')
    
    def __str__(self):
        return f'{self.username} deposited'
        
class Approved(models.Model):
    user_name = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True)
    amount = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.user_name} deposit approved'
