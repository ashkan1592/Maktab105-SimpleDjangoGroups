# Generated by Django 5.0.2 on 2024-02-14 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='urls',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='urls',
            name='url',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
