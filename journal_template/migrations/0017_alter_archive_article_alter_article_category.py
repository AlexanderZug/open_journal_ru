# Generated by Django 4.0.5 on 2022-07-24 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('journal_template', '0016_alter_archive_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archive',
            name='article',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='articles', to='journal_template.article', verbose_name='статья|автор статьи (необходимо заполнить)'),
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='categories', to='journal_template.category', verbose_name='категория (опционально)'),
        ),
    ]
