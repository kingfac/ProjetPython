# Generated by Django 4.2 on 2023-04-17 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceAchat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produit',
            name='image',
        ),
        migrations.AddField(
            model_name='produit',
            name='posologie',
            field=models.TextField(default='joel'),
        ),
    ]