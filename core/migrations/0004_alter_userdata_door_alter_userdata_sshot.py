# Generated by Django 4.2 on 2023-05-01 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_userdata_door_alter_userdata_sshot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='door',
            field=models.ImageField(blank=True, null=True, upload_to='doorstep/'),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='sshot',
            field=models.ImageField(blank=True, null=True, upload_to='screenshot/'),
        ),
    ]