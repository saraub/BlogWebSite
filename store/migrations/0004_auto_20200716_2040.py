# Generated by Django 3.0.8 on 2020-07-16 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20200716_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='image',
            field=models.ImageField(blank=True, default='profile.jpg', null=True, upload_to=''),
        ),
    ]