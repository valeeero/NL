# Generated by Django 4.0.6 on 2022-07-15 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note_lists', '0002_alter_notelist_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='notelist',
            name='header',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
