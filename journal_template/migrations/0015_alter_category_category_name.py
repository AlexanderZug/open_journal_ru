# Generated by Django 4.0.5 on 2022-07-24 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal_template', '0014_alter_clientcontact_massage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='категории'),
        ),
    ]