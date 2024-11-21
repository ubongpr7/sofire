from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from mptt.models import MPTTModel, TreeForeignKey

from mainapps.common.models import Tag,GenericModel, UpdatableModel
User=settings.AUTH_USER_MODEL


class Post(GenericModel):
    """
    Model representing a user's post on their timeline.

    Fields:
    - title: CharField representing the title of the post.
    - content: Text field representing the content of the post.
    - visibility: CharField representing the visibility of the post (public, private, friends-only).
    - tags: Many-to-Many relationship with Tag representing tags associated with the post.
    
    """
    VISIBILITY_CHOICES = [
        ('public', 'Public'),
        ('private', 'Private'),
        ('friends_only', 'Friends Only'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    visibility = models.CharField(max_length=20, choices=VISIBILITY_CHOICES, default='public')
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return f"{self.user.username} Created {self.content_type} post, title: {self.title} ({self.object_id})"

    class Meta:
        ordering = ['-created_at']


class Reaction(models.Model):
    """
    Model representing reactions on various objects.

    Fields:
    - emoji: CharField representing the emoji or symbol used for the reaction.
    """
    emoji = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.emoji}"


class PostLike(UpdatableModel):
    """
    Model representing a like on a post or comment.

    Fields:
    - user: ForeignKey to User model representing the user who liked.
    """
    post=models.ForeignKey(Post, on_delete=models.CASCADE,related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reaction=models.ForeignKey(Reaction, on_delete=models.SET_NULL,null=True,blank=True, default='1', related_name='likes')    





class PostComment(GenericModel, MPTTModel):
    """
    Model representing a comment on a content object.

    Fields:
    - user: ForeignKey to User model representing the user who posted the comment.
    - comment: what user has to say
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')

    def __str__(self):
        return f"{self.user.username}'s Comment on {self.content_type} ({self.object_id})"

