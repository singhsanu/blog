# Generated by Django 5.0.1 on 2024-01-29 05:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0006_alter_blog_post_blog_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_post',
            name='blog_cat',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myblog.blog_category'),
            preserve_default=False,
        ),
    ]