# Generated by Django 3.2.7 on 2024-05-03 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('steve', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
