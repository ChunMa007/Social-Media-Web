# Generated by Django 5.2 on 2025-04-11 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_userprofile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, default='images/Default_Profile.webp', null=True, upload_to='images/'),
        ),
    ]
