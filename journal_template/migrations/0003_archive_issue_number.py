# Generated by Django 4.0.5 on 2022-07-11 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            'journal_template',
            '0002_alter_about_options_alter_archive_options_and_more',
        ),
    ]

    operations = [
        migrations.AddField(
            model_name='archive',
            name='issue_number',
            field=models.CharField(
                default=1, max_length=250, verbose_name='номер журнала'
            ),
            preserve_default=False,
        ),
    ]
