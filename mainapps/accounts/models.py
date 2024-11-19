from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.conf import settings

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    email = models.EmailField(unique=True, null=False, blank=False)
    api_key = models.CharField(max_length=255, blank=True, null=True)
    class AccountTypeChoice(models.TextChoices):
        personal='personal','Personal'
        church='church','Church'
        celeb='celeb','Celebrity'
    account_type=models.CharField(choices=AccountTypeChoice.choices,default=AccountTypeChoice.personal,max_length=50)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        self.username = self.email
        super().save(*args, **kwargs)


class Follower(models.Model):
    user=models.OneToOneField(User,related_name='follower', on_delete=models.CASCADE,)


class ProfilePhoto(models.Model):
    picture=models.ImageField(upload_to='profile_photos')
    user=models.ForeignKey(User,on_delete=models.CASCADE)

class VerificationCode(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    code=models.CharField(max_length=6,blank=True)
    slug=models.SlugField(editable=False,blank=True)
    time_requested=models.DateTimeField(auto_now=True)
    successful_attempts=models.IntegerField(default=0)
    total_attempts=models.IntegerField(default=0)
    def __str__(self):
        return self.code
    def save(self, *args,**kwargs):
        nums=[i for i in range(1,9)]
        code_list=[]
        for i in range(6):
            n=random.choice(nums)
            code_list.append(n)
        code_string="".join(str(i)  for i in code_list)
        self.code=code_string
        self.slug=self.user.username
        super().save( *args,**kwargs)
    
