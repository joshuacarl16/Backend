# Generated by Django 4.2 on 2023-05-16 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_topic_categoryname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='categoryName',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='created_at',
            new_name='dateCreated',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='topic',
            new_name='topicName',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='user',
            new_name='userId',
        ),
        migrations.AlterField(
            model_name='topic',
            name='categoryName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.category'),
        ),
    ]
