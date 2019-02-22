# Generated by Django 2.1.7 on 2019-02-22 05:54

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('code', models.CharField(max_length=128)),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField(blank=True)),
                ('current_status', models.CharField(choices=[('created', 'created'), ('open', 'open'), ('finished', 'finished'), ('archived', 'archived')], max_length=128)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
