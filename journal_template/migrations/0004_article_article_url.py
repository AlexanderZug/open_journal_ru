# Generated by Django 4.0.5 on 2022-07-11 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal_template', '0003_archive_issue_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_url',
            field=models.SlugField(default=1, max_length=100, unique=True),
            preserve_default=False,
        ),
    ]
