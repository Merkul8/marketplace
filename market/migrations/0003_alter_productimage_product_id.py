# Generated by Django 4.2.8 on 2023-12-22 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_remove_product_category_id_product_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='market.product'),
        ),
    ]
