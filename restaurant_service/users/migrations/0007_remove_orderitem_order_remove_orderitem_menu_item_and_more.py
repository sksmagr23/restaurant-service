# Generated by Django 5.0.6 on 2024-07-08 04:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_remove_order_items_remove_order_order_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='menu_item',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
