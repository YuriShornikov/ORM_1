# Generated by Django 4.1.7 on 2023-04-03 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=50)),
                ('release_date', models.CharField(max_length=50)),
                ('lte_exists', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
            ],
        ),
    ]
