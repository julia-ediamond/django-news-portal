# Generated by Django 3.2.6 on 2021-08-20 01:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20210818_0921'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsstory',
            options={'ordering': ['-pub_date']},
        ),
    ]
