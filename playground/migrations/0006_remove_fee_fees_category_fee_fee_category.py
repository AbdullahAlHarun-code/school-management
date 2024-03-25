# Generated by Django 5.0.3 on 2024-03-24 14:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0005_feeset'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fee',
            name='fees_category',
        ),
        migrations.AddField(
            model_name='fee',
            name='fee_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='playground.feeset', verbose_name='Fee Category'),
            preserve_default=False,
        ),
    ]