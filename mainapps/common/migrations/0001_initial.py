# Generated by Django 5.1.3 on 2024-11-21 15:48

import django.db.models.deletion
import mainapps.common.models
import mptt.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PlatformSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('terms_of_service', models.TextField()),
                ('privacy_policy', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('object_id', models.PositiveIntegerField(help_text='The ID of the linked object.', verbose_name='Object ID')),
                ('content_type', models.ForeignKey(help_text='The content type of the linked object.', on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype', verbose_name='Content Type')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CustomCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('object_id', models.PositiveIntegerField(help_text='The ID of the linked object.', verbose_name='Object ID')),
                ('category_name', models.CharField(max_length=50)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('content_type', models.ForeignKey(help_text='The content type of the linked object.', on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype', verbose_name='Content Type')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='common.customcategory')),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ['category_name'],
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to=mainapps.common.models.attachment_upload_path)),
                ('attachment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attached_files', to='common.attachment')),
            ],
        ),
        migrations.CreateModel(
            name='NotificationCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('object_id', models.PositiveIntegerField(help_text='The ID of the linked object.', verbose_name='Object ID')),
                ('type_name', models.CharField(max_length=50)),
                ('content_type', models.ForeignKey(help_text='The content type of the linked object.', on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype', verbose_name='Content Type')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Share',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('object_id', models.PositiveIntegerField(help_text='The ID of the linked object.', verbose_name='Object ID')),
                ('content_type', models.ForeignKey(help_text='The content type of the linked object.', on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype', verbose_name='Content Type')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SocialMediaHandles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('object_id', models.PositiveIntegerField(help_text='The ID of the linked object.', verbose_name='Object ID')),
                ('platform_name', models.CharField(max_length=50)),
                ('link', models.URLField()),
                ('content_type', models.ForeignKey(help_text='The content type of the linked object.', on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype', verbose_name='Content Type')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('object_id', models.PositiveIntegerField(help_text='The ID of the linked object.', verbose_name='Object ID')),
                ('plan_name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('content_type', models.ForeignKey(help_text='The content type of the linked object.', on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype', verbose_name='Content Type')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserInterest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('object_id', models.PositiveIntegerField(help_text='The ID of the linked object.', verbose_name='Object ID')),
                ('name', models.CharField(max_length=50)),
                ('content_type', models.ForeignKey(help_text='The content type of the linked object.', on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype', verbose_name='Content Type')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
