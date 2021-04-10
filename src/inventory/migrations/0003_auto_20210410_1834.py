# Generated by Django 3.1.7 on 2021-04-10 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_rawmaterial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-created_at'], 'permissions': [('pharma_can_create', 'Pharma can create product'), ('pharma_can_update', 'Pharma can update product'), ('pharma_can_delete', 'Pharma_can_delete_product'), ('pharma_can_view', 'Pharma can view product'), ('pharma_can_view_list', 'Pharma can view product list')]},
        ),
    ]
