import time
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from mptt.models import MPTTModel, TreeForeignKey
from django.utils import timezone


User=settings.AUTH_USER_MODEL
class UpdatableModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    class Meta:
        abstract=True

class GenericModel(UpdatableModel):
    """
    Abstract base class for models with GenericForeignKey.

    This abstract base class provides fields to link to any other model using a GenericForeignKey.
    It includes fields for content type, object ID, and a field to specify the target model.

    Fields:
    - content_type: ForeignKey to ContentType model representing the type of the linked object.
    - object_id: PositiveIntegerField representing the ID of the linked object.
    - content_object: GenericForeignKey to represent the linked object.
    - created_at: DateTime field representing the timestamp when the like was created.
    - updated_at: DateTime field representing the timestamp when the comment was last updated.

    Methods:
    - __str__: Returns a string representation of the model instance.
    """

    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        verbose_name='Content Type',
        help_text='The content type of the linked object.'
    )
    object_id = models.PositiveIntegerField(
        verbose_name='Object ID',
        help_text='The ID of the linked object.'
    )
    content_object = GenericForeignKey('content_type', 'object_id')
    
    class Meta:
        abstract = True

    def __str__(self):
        """
        String representation of the model instance.
        
        Returns:
            str: A string representing the linked object using content type and object ID.
        """
        return f"Instance for {self.content_type.model} ({self.object_id})"



class NotificationCategory(GenericModel):
    """
    Model representing notification types.

    Fields:
    - type_name: Name of the notification type.
    """
    type_name = models.CharField(max_length=50)

class UserInterest(GenericModel):
    """
    Model representing user interests.

    Fields:
    - name: Name of the interest.
    """
    name = models.CharField(max_length=50)
   
class SocialMediaHandles(GenericModel):
    """
    Model representing user social media links.

    Fields:
    - platform_name: Name of the social media platform.
    - link: Link to the user's profile on the platform.
    """
    platform_name = models.CharField(max_length=50)
    link = models.URLField()


class CustomCategory(GenericModel,MPTTModel):
    """
    Model representing categories of interest for events.

    Fields:
    - category_name: Name of the event category.
    - parent: TreeForeignKey to represent the parent category in a hierarchical structure.
    """
    category_name = models.CharField(max_length=50)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    

    def __str__(self):
        return f"{self.category_name} created -> {self.content_type}  ({self.object_id})"

    class Meta:
        ordering = ['category_name']
        verbose_name_plural='Categories'


class Subscription(GenericModel):
    """
    Model representing subscription plans.

    Fields:
    - plan_name: Name of the subscription plan.
    - price: Price of the subscription plan.
    """
    plan_name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2,)
    
class PlatformSettings(models.Model):
    terms_of_service = models.TextField()
    privacy_policy = models.TextField()

    def __str__(self):
        return "Platform Settings"

class Share(GenericModel):
    """
    Model representing a share of a content object.

    Fields:
    - user: ForeignKey to User model representing the user who shared.
    
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return f"{self.user.username} shared {self.content_type} ({self.object_id})"


class Tag(models.Model):
    """
    Model representing tags for various objects.

    Fields:
    - tag: CharField representing the name of the tag.
    """
    tag = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Attachment(GenericModel):
    """
    Model representing attachments for posts and events.

    Fields:
    """
    def __str__(self):
        return f"Attachment for {self.content_type.model} ({self.object_id})"



def attachment_upload_path(instance, filename):
    timestamp = int(time.time())
    ext=filename.split('.')[-1]
    return f'attachments/{instance.attachment.content_type.model}/{instance.attachment.object_id}/{instance.attachment.id}/{instance.id}/{filename}_{timestamp}.{ext}'


class File(models.Model):
    """
    Model representing individual files associated with an attachment.

    Fields:
    - attachment: ForeignKey to Attachment model representing the parent attachment.
    - file: FileField representing the attached file.
    """
    attachment = models.ForeignKey(Attachment, on_delete=models.CASCADE, related_name='attached_files')
    file = models.FileField(upload_to=attachment_upload_path, blank=True,null=True)

    def __str__(self):
        return f"File for {self.attachment}"


        

