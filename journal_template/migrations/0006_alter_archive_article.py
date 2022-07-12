# Generated by Django 4.0.5 on 2022-07-12 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('journal_template', '0005_remove_article_article_url_archive_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archive',
            name='article',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='articles', to='journal_template.article', verbose_name='статья'),
        ),
    ]