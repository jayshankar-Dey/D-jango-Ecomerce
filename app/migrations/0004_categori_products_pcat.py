# Generated by Django 5.0.1 on 2024-02-10 05:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_products_pprice_alter_products_ptotal'),
    ]

    operations = [
        migrations.CreateModel(
            name='categori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='products',
            name='pcat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.categori'),
        ),
    ]
