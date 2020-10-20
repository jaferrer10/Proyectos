# Generated by Django 3.1.2 on 2020-10-16 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inmueble', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Casa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('medidas', models.CharField(blank=True, max_length=30)),
                ('moneda', models.CharField(choices=[('peso', 'Peso'), ('dolar', 'Dólar'), ('euro', 'Euro'), ('real', 'Real')], default='peso', max_length=5)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=11)),
                ('descripcion', models.TextField(blank=True)),
                ('en_venta', models.BooleanField(default=False)),
                ('en_alquiler', models.BooleanField(default=False)),
                ('cantidad_habitaciones', models.PositiveSmallIntegerField(default=0)),
                ('cantidad_banios', models.PositiveSmallIntegerField(default=0)),
                ('cantidad_suite', models.PositiveSmallIntegerField(default=0)),
                ('servicios', models.ManyToManyField(blank=True, to='inmueble.Servicio')),
            ],
            options={
                'verbose_name': 'Lista de casa',
                'verbose_name_plural': 'Listado de casas',
            },
        ),
    ]