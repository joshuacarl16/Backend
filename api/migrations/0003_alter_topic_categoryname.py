# Generated by Django 4.2 on 2023-05-16 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_category_topic_categoryname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='categoryName',
            field=models.CharField(max_length=100),
        ),
    ]