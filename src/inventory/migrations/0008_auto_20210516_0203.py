# Generated by Django 3.1.7 on 2021-05-16 02:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_auto_20210505_0350'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='batch',
            options={'ordering': ['-created_at'], 'permissions': [('pharma_can_create_batch', 'Pharma can create batch'), ('pharma_can_update_batch', 'Pharma can update batch'), ('pharma_can_view_batch', 'Pharma can view batch'), ('retailer_can_order_batch', 'Retailer can order batch'), ('retailer_can_view_batch', 'Retailer can view batch')]},
        ),
    ]
