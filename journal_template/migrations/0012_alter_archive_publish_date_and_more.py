# Generated by Django 4.0.5 on 2022-07-19 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal_template', '0011_alter_clientcontact_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archive',
            name='publish_date',
            field=models.DateTimeField(
                auto_now_add=True,
                db_index=True,
                verbose_name='дата (автоматически)',
            ),
        ),
        migrations.AlterField(
            model_name='clientcontact',
            name='publish_date',
            field=models.DateTimeField(
                auto_now_add=True,
                db_index=True,
                verbose_name='дата (автоматически)',
            ),
        ),
    ]
