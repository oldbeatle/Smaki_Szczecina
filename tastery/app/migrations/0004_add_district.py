# Generated by Django 3.2.9 on 2022-01-04 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_more_rest_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='district',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
