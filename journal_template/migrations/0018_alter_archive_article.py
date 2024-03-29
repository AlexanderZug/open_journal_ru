# Generated by Django 4.0.5 on 2022-07-24 13:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            'journal_template',
            '0017_alter_archive_article_alter_article_category',
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name='archive',
            name='article',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='articles',
                to='journal_template.article',
                verbose_name='статья|автор статьи',
            ),
        ),
    ]
