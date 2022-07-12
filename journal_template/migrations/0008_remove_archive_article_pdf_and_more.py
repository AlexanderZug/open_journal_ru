# Generated by Django 4.0.5 on 2022-07-12 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('journal_template', '0007_alter_archive_article'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='archive',
            name='article_pdf',
        ),
        migrations.RemoveField(
            model_name='archive',
            name='article_title',
        ),
        migrations.RemoveField(
            model_name='archive',
            name='author',
        ),
        migrations.RemoveField(
            model_name='archive',
            name='category',
        ),
        migrations.AddField(
            model_name='article',
            name='article_pdf',
            field=models.FileField(default=1, upload_to='issue_pdf/', verbose_name='pdf-файл статьи'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='article_title',
            field=models.CharField(default=1, max_length=300, verbose_name='название статьи'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.CharField(default=1, max_length=200, verbose_name='имя автора'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='categories', to='journal_template.category', verbose_name='категория (опционально)'),
        ),
        migrations.AlterField(
            model_name='archive',
            name='article',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='articles', to='journal_template.article', verbose_name='статья|автор статьи'),
        ),
    ]
