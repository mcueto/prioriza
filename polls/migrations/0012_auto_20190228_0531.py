# Generated by Django 2.1.7 on 2019-02-28 05:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_pollvote_poll_option_selections'),
    ]

    operations = [
        migrations.RenameField(
            model_name='polloptionselection',
            old_name='selection_priority',
            new_name='priority',
        ),
    ]
