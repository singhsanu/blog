# Generated by Django 5.0.1 on 2024-02-05 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0010_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]