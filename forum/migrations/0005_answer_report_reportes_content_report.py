# Generated by Django 4.1.4 on 2023-12-19 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_remove_reportes_user_report'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='report',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='reportes',
            name='content_report',
            field=models.TextField(blank=True, null=True),
        ),
    ]
