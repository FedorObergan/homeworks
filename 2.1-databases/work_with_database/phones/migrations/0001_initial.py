# Generated by Django 5.0.6 on 2024-06-11 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('image', models.CharField(max_length=100)),
                ('release_date', models.DateField(max_length=50)),
                ('lte_exists', models.BooleanField()),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
        ),
    ]
