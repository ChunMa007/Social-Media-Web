# Generated by Django 5.2 on 2025-04-09 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, default='media/images/Default_Profile.webp', null=True, upload_to='images/'),
        ),
    ]
