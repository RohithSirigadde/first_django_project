# Generated by Django 4.2.3 on 2023-07-24 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdetails',
            name='summary',
            field=models.TextField(default='this is summary, which is cool!'),
        ),
    ]