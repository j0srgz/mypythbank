# Generated by Django 4.1.3 on 2022-11-05 05:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0005_remove_cuentas_cedula_prop_remove_cuentas_nrocuenta_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transfers',
            name='id_emisora',
        ),
        migrations.DeleteModel(
            name='Cuentas',
        ),
        migrations.DeleteModel(
            name='Transfers',
        ),
    ]