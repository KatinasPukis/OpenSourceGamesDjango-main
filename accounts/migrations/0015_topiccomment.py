# Generated by Django 3.2.7 on 2021-11-21 10:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0014_topic'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopicComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_body', models.TextField(null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('topic_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='topiccc', to='accounts.topic')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userrr', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
