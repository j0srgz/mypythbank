# Generated by Django 4.1.3 on 2022-11-05 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cuentas',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='transfers',
            old_name='id_emisora',
            new_name='emisora',
        ),
        migrations.AlterField(
            model_name='cuentas',
            name='cedula_prop',
            field=models.IntegerField(max_length=20),
        ),
        migrations.AlterField(
            model_name='cuentas',
            name='nrocuenta',
            field=models.IntegerField(max_length=20),
        ),
        migrations.AlterField(
            model_name='transfers',
            name='cta_receptora',
            field=models.IntegerField(max_length=20),
        ),
    ]
