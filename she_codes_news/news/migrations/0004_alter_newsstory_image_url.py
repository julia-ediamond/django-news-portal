# Generated by Django 3.2.6 on 2021-08-20 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_newsstory_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsstory',
            name='image_url',
            field=models.TextField(),
        ),
    ]