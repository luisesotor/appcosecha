# Generated by Django 4.1 on 2022-09-01 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcosecha', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listadeprecios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Nosotros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nosotros', models.CharField(max_length=300)),
            ],
        ),
    ]
