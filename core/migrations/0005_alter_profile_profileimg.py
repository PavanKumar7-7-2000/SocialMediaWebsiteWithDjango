# Generated by Django 3.2.5 on 2022-10-19 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_profile_profileimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profileimg',
            field=models.ImageField(upload_to='blank_profile_picture.png'),
        ),
    ]
