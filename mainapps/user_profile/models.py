from django.db import models

from mainapps.common.models import  PlatformSettings,  User



class UserProfile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    two_factor_authentication = models.BooleanField(default=False)
    account_visibility = models.CharField(max_length=20, choices=[('public', 'Public'), ('private', 'Private'), ('friends_only', 'Friends Only')])
    bio = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    # blocked_users= models.ForeignKey(User, on_delete=models.SET_NULL,null=True, blank=True)

    def __str__(self):
        return self.user.username
