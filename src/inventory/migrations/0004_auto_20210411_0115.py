# Generated by Django 3.1.7 on 2021-04-11 01:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20210410_1834'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rawmaterial',
            options={'ordering': ['-created_at'], 'permissions': [('supplier_can_create', 'Supplier can create raw material'), ('supplier_can_update', 'Supplier can update raw material'), ('supplier_can_delete', 'Supplier can delete raw material'), ('supplier_can_view', 'Supplier can view raw material'), ('supplier_can_view_list', 'Supplier can view raw material list'), ('pharma_can_view', 'Pharmaceutical can view raw material'), ('pharma_can_view_list', 'Pharmaceutical can view raw material list')]},
        ),
    ]
