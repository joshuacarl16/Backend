# Generated by Django 4.2 on 2023-05-16 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='category',
            new_name='categoryName',
        ),
        migrations.RenameField(
            model_name='topic',
            old_name='created_at',
            new_name='dateCreated',
        ),
        migrations.RenameField(
            model_name='topic',
            old_name='title',
            new_name='topicName',
        ),
        migrations.RenameField(
            model_name='topic',
            old_name='user',
            new_name='userId',
        ),
    ]
