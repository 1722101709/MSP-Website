# Generated by Django 3.2.4 on 2022-12-17 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_company_package'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='info',
            field=models.TextField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
