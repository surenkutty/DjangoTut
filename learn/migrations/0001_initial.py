# Generated by Django 5.1.3 on 2024-11-24 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('offer_price', models.IntegerField()),
                ('description', models.CharField(max_length=500)),
                ('mrp_price', models.IntegerField()),
                ('category', models.CharField(max_length=50)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
