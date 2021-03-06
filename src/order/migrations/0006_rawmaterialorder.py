# Generated by Django 3.1.7 on 2021-04-11 21:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0004_auto_20210409_2309'),
        ('inventory', '0005_auto_20210411_0306'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0005_auto_20210411_1805'),
    ]

    operations = [
        migrations.CreateModel(
            name='RawMaterialOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('active', 'active'), ('rejected', 'rejected'), ('fulfilled', 'fulfilled'), ('canceled', 'canceled')], default='active', max_length=20)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('raw_material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.rawmaterial')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='raw_material_orders', to='organization.organization')),
            ],
            options={
                'db_table': 'raw_material_orders',
                'ordering': ['-created_at'],
                'permissions': [('pharma_can_create_order_raw_material', 'Pharma can create order for raw material'), ('pharma_can_cancel_order_raw_material', 'Pharma can cancel order for raw material'), ('supplier_can_fulfill_order_raw_material', 'Supplier can fulfill order for raw material'), ('supplier_can_reject_order_raw_material', 'Supplier can reject order for raw material'), ('supplier_can_view_order_raw_material_list', 'Supplier can view order list for raw material')],
            },
        ),
    ]
