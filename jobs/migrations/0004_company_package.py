# Generated by Django 3.2.4 on 2022-12-17 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_company_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='package',
            field=models.TextField(default=1, max_length=29),
            preserve_default=False,
        ),
    ]