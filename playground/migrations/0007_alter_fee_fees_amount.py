# Generated by Django 5.0.3 on 2024-03-24 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0006_remove_fee_fees_category_fee_fee_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fee',
            name='fees_amount',
            field=models.DecimalField(decimal_places=2, editable=False, max_digits=10, verbose_name='Fees Amount'),
        ),
    ]
