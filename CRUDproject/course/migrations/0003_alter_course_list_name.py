# Generated by Django 4.2.7 on 2023-11-21 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_alter_course_list_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course_list',
            name='Name',
            field=models.CharField(max_length=70),
        ),
    ]
