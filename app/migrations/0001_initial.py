# Generated by Django 5.0.1 on 2024-02-10 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_size1', models.CharField(max_length=200)),
                ('product_size2', models.CharField(max_length=200)),
                ('product_size3', models.CharField(max_length=200)),
                ('product_size4', models.CharField(max_length=200)),
            ],
        ),
    ]
