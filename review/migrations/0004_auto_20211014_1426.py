# Generated by Django 3.2.6 on 2021-10-14 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_customer_image'),
        ('product', '0005_auto_20210930_0108'),
        ('review', '0003_remove_review_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='order_product',
        ),
        migrations.AddField(
            model_name='review',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.product'),
        ),
        migrations.AlterField(
            model_name='review',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='customers.customer'),
        ),
    ]
