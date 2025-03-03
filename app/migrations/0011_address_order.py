# Generated by Django 5.0.1 on 2024-03-07 14:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_carts'),
    ]

    operations = [
        migrations.CreateModel(
            name='address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pin', models.CharField(max_length=240)),
                ('city', models.CharField(max_length=240)),
                ('addres', models.CharField(max_length=240)),
            ],
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField(max_length=100)),
                ('image', models.CharField(max_length=240)),
                ('psize', models.CharField(blank=True, max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('addres', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.address')),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.products')),
            ],
        ),
    ]
