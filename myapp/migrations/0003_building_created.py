# Generated by Django 4.0.3 on 2022-04-03 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_building_flat_delete_property'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
