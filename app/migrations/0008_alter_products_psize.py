# Generated by Django 5.0.1 on 2024-02-12 13:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_products_psize'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='psize',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='missions_assigned', to='app.size'),
        ),
    ]
