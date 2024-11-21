from django.db import models

from tinymce.models import HTMLField  

from mainapps.common.models import UpdatableModel, User

class GroupSettings(models.Model):
    """
    Model representing extended settings for a group.

    Fields:
    - is_public: BooleanField indicating whether the group is public or private.
    - max_members: IntegerField representing the maximum number of members allowed in the group.
    - allow_posts: BooleanField indicating whether members can make posts within the group.
    - allow_comments: BooleanField indicating whether members can comment on posts.
    - allow_invitations: BooleanField indicating whether members can invite others to join.
    - join_requests: BooleanField indicating whether members need approval to join.
    - moderation_level: ChoiceField representing the moderation level for group content.
    - group_color: CharField representing the color theme of the group.
    - cover_photo: ImageField for the group's cover photo.
    - custom_fields: JSONField for storing custom fields or settings.
    """
    MODERATION_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    is_public = models.BooleanField(default=True)
    post_approval = models.BooleanField(default=True)
    allow_invitations = models.BooleanField(default=True)
    member_approval = models.BooleanField(default=True)
    cover_photo = models.ImageField(upload_to='group_covers/', blank=True, null=True)
    class Meta:
        verbose_name_plural = 'Group Settings'

class GroupCategory(models.Model):
    """
    Model representing roles within a group.

    Fields:
    - name: CharField representing the name of the group role.
    - description: TextField for a detailed description of the group role.
    """
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class SofireGroup(UpdatableModel):
    """
    Model representing a group.

    Fields:
    - name: CharField representing the name of the group.
    - description: TextField for a detailed description of the group.
    - categories: Many-to-Many relationship with GroupRole representing the roles within the group.
    - settings: One-to-One relationship with GroupSettings representing the settings for the group.
    - created_by: ForeignKey to User model representing the user who created the group.
    """
    name = models.CharField(max_length=100)
    description = models.TextField()
    categories = models.ManyToManyField(GroupCategory, related_name='groups', blank=True)
    settings = models.OneToOneField(GroupSettings, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_groups')

    def __str__(self):
        return f"{self.name} (Created by: {self.created_by.username})"


    class Meta:
        ordering = ['-created_at']

class GroupMembership(models.Model):
    member=models.ForeignKey(User,on_delete=models.CASCADE)
    group=models.ForeignKey(SofireGroup,on_delete=models.CASCADE)
    class MembershipStatus(models.TextChoices):
        member='member','Member'
        removed='removed','Removed'
        requested='request','Request'

    membership_status=models.CharField(max_length=20,choices=MembershipStatus,default=MembershipStatus.requested)
    class Roles(models.TextChoices):
        member='member',"Member"
        admin='admin',"Admin"
        moderator='moderator',"Moderator"
    role=models.CharField(max_length=30, choices=Roles,default=Roles.member)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['member', 'group'], name='unique_member_group')
        ]
class GroupRule(UpdatableModel):
    """
    Model representing rules for a group.

    Fields:
    - group: ForeignKey to Group model representing the group to which the rules belong.
    - title: CharField representing the title of the rules.
    - content: HTMLField representing the content of the rules.
    - created_at: DateTimeField representing the timestamp when the rules were created.
    - updated_at: DateTimeField representing the timestamp when the rules were last updated.
    """
    group = models.ForeignKey(SofireGroup, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content=models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Group Rules - {self.title} ({self.group})"

    class Meta:
        verbose_name_plural = 'Group Rules'


class SofireGroupPermission(UpdatableModel):
    """
    Model representing group permissions based on roles.

    Fields:
    - group: ForeignKey to the Group model representing the group associated with these permissions.
    - can_post: BooleanField indicating whether group members can create posts.
    - can_comment: BooleanField indicating whether group members can comment on posts.
    - can_invite_members: BooleanField indicating whether group members can invite others to join the group.
    - can_manage_members: BooleanField indicating whether group members can manage (add/remove) other members.
    - can_edit_group_info: BooleanField indicating whether group members can edit group information.
    - can_delete_group: BooleanField indicating whether group members can delete the group.
    - created_at: DateTimeField representing the timestamp when the permissions were created.
    - updated_at: DateTimeField representing the timestamp when the permissions were last updated.
    """

    group = models.ForeignKey(SofireGroup, on_delete=models.CASCADE)
    class Roles(models.TextChoices):
        member='member',"Member"
        admin='admin',"Admin"
        moderator='moderator',"Moderator"
    role=models.CharField(max_length=30, choices=Roles,default=Roles.member)
    can_post = models.BooleanField(default=True)
    can_comment = models.BooleanField(default=True)
    can_invite_members = models.BooleanField(default=False)
    can_manage_members = models.BooleanField(default=False)
    can_edit_group_info = models.BooleanField(default=False)
    can_delete_group = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Group Permissions for {self.group.name}"

    class Meta:
        verbose_name_plural = "Group Permissions"
        ordering = ['-created_at']

class GroupAnnouncements(UpdatableModel):
    """
    Model representing announcements within a group.

    Fields:
    - group: ForeignKey to SofireGroup model representing the group to which the announcement belongs.
    - title: CharField representing the title of the announcement.
    - content: TextField for the content of the announcement.
    - created_at: DateTimeField representing the timestamp when the announcement was created.
    - updated_at: DateTimeField representing the timestamp when the announcement was last updated.
    """
    group = models.ForeignKey(SofireGroup, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return f"Group Announcement - {self.title} ({self.group})"

    class Meta:
        verbose_name_plural = 'Group Announcements'

