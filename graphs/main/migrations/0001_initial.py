# Generated by Django 5.0 on 2023-12-06 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Count',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(verbose_name='Количество')),
            ],
        ),
        migrations.CreateModel(
            name='Edges',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('out', models.IntegerField(verbose_name='1')),
                ('to', models.IntegerField(verbose_name='2')),
                ('weight', models.IntegerField(verbose_name='3')),
            ],
        ),
        migrations.CreateModel(
            name='Names',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(verbose_name='Номер')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('dangerous', models.BooleanField(verbose_name='Опасное сост.')),
            ],
        ),
    ]
