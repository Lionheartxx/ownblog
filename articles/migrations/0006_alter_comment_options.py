# Generated by Django 4.0.3 on 2022-04-23 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_rename_comment_comment_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-date_added']},
        ),
    ]