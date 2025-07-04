# Generated by Django 5.2.1 on 2025-06-18 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PTStaff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('staff_id', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('phone_number', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=200)),
                ('student_id', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=200)),
                ('teacher_id', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
