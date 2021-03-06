# Generated by Django 4.0.3 on 2022-04-03 04:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.FloatField()),
                ('number_rooms', models.FloatField()),
                ('price', models.FloatField()),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Flat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.building')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.owner')),
            ],
        ),
        migrations.DeleteModel(
            name='Property',
        ),
    ]
