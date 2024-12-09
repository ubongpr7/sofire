# Generated by Django 5.1.3 on 2024-11-21 15:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='GroupSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_public', models.BooleanField(default=True)),
                ('post_approval', models.BooleanField(default=True)),
                ('allow_invitations', models.BooleanField(default=True)),
                ('member_approval', models.BooleanField(default=True)),
                ('cover_photo', models.ImageField(blank=True, null=True, upload_to='group_covers/')),
            ],
            options={
                'verbose_name_plural': 'Group Settings',
            },
        ),
        migrations.CreateModel(
            name='SofireGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('categories', models.ManyToManyField(blank=True, related_name='groups', to='bell_group.groupcategory')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_groups', to=settings.AUTH_USER_MODEL)),
                ('settings', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bell_group.groupsettings')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='GroupRule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField(blank=True, null=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bell_group.sofiregroup')),
            ],
            options={
                'verbose_name_plural': 'Group Rules',
            },
        ),
        migrations.CreateModel(
            name='GroupAnnouncements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bell_group.sofiregroup')),
            ],
            options={
                'verbose_name_plural': 'Group Announcements',
            },
        ),
        migrations.CreateModel(
            name='SofireGroupPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('role', models.CharField(choices=[('member', 'Member'), ('admin', 'Admin'), ('moderator', 'Moderator')], default='member', max_length=30)),
                ('can_post', models.BooleanField(default=True)),
                ('can_comment', models.BooleanField(default=True)),
                ('can_invite_members', models.BooleanField(default=False)),
                ('can_manage_members', models.BooleanField(default=False)),
                ('can_edit_group_info', models.BooleanField(default=False)),
                ('can_delete_group', models.BooleanField(default=False)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bell_group.sofiregroup')),
            ],
            options={
                'verbose_name_plural': 'Group Permissions',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='GroupMembership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('membership_status', models.CharField(choices=[('member', 'Member'), ('removed', 'Removed'), ('request', 'Request')], default='request', max_length=20)),
                ('role', models.CharField(choices=[('member', 'Member'), ('admin', 'Admin'), ('moderator', 'Moderator')], default='member', max_length=30)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bell_group.sofiregroup')),
            ],
            options={
                'constraints': [models.UniqueConstraint(fields=('member', 'group'), name='unique_member_group')],
            },
        ),
    ]
