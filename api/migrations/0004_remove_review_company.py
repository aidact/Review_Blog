# Generated by Django 2.2.3 on 2019-07-05 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_review_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='company',
        ),
    ]
