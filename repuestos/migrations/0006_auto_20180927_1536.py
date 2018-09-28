# Generated by Django 2.1.1 on 2018-09-27 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repuestos', '0005_kitc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kitb',
            name='kitNumSAP_B',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='repuestos.Articulo'),
        ),
        migrations.AlterField(
            model_name='kitc',
            name='kitNumSAP_C',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='repuestos.Articulo'),
        ),
    ]
