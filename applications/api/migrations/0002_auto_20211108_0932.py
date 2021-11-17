# Generated by Django 3.2 on 2021-11-08 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='medico',
            name='domicilio',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='domicilio',
        ),
        migrations.RemoveField(
            model_name='radiologo',
            name='domicilio',
        ),
        migrations.RemoveField(
            model_name='secretario',
            name='domicilio',
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.pais')),
            ],
        ),
        migrations.CreateModel(
            name='Localidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('codigo_postal', models.CharField(max_length=5)),
                ('provincia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.provincia')),
            ],
        ),
        migrations.CreateModel(
            name='Domicilio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=30)),
                ('entre_calle_sup', models.CharField(max_length=30)),
                ('entre_calle_inf', models.CharField(max_length=30)),
                ('fecha_desde', models.DateField()),
                ('fecha_hasta', models.DateField()),
                ('localidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.localidad')),
            ],
        ),
        migrations.AddField(
            model_name='medico',
            name='domicilio',
            field=models.ManyToManyField(blank=True, null=True, to='api.Domicilio'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='domicilio',
            field=models.ManyToManyField(blank=True, null=True, to='api.Domicilio'),
        ),
        migrations.AddField(
            model_name='radiologo',
            name='domicilio',
            field=models.ManyToManyField(blank=True, null=True, to='api.Domicilio'),
        ),
        migrations.AddField(
            model_name='secretario',
            name='domicilio',
            field=models.ManyToManyField(blank=True, null=True, to='api.Domicilio'),
        ),
    ]