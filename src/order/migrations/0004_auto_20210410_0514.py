# Generated by Django 3.1.7 on 2021-04-10 05:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20210410_0513'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-created_at'], 'permissions': [('supplier_order_list', 'Can view order request list for the supplier'), ('pharma_order_list', 'Can view order list made by pharma')]},
        ),
    ]