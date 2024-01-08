# Generated by Django 4.2.8 on 2024-01-08 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0007_product_updated'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='views',
        ),
        migrations.AddField(
            model_name='product',
            name='views',
            field=models.ManyToManyField(blank=True, related_name='product_views', to='market.ip'),
        ),
    ]