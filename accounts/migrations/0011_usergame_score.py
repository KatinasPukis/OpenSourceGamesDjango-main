# Generated by Django 3.2.7 on 2021-11-20 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_gamecomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='usergame',
            name='score',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
