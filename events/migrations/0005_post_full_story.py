# Generated by Django 3.1.2 on 2021-01-07 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='full_story',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
    ]
