# Generated by Django 3.1.6 on 2021-07-07 03:17

import backend.apps.products.utils
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('price', models.FloatField()),
                ('description', models.TextField(blank=True, null=True)),
                ('code', models.CharField(default=backend.apps.products.utils.create_new_code_number, editable=False, max_length=4, unique=True)),
                ('image', models.CharField(max_length=256)),
                ('sub_image', models.JSONField(blank=True, null=True)),
                ('sub_category', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='products.subcategory')),
            ],
        ),
    ]
