# Generated by Django 5.1.3 on 2024-11-19 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profilephoto_verificationcode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='api_key',
        ),
        migrations.AddField(
            model_name='user',
            name='picture',
            field=models.ImageField(null=True, upload_to='profile_pictures/%y/%m/%d/'),
        ),
    ]