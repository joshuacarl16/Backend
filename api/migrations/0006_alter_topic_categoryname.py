# Generated by Django 4.2.1 on 2023-05-17 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_topic_categoryname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='categoryName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.category'),
        ),
    ]
