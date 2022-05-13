# Generated by Django 4.0.4 on 2022-05-13 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=150)),
                ('mobile_number', models.CharField(max_length=150)),
                ('birth', models.DateField()),
                ('gpa', models.IntegerField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('m', 'Male'), ('f', 'Female')], max_length=1)),
                ('level', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')], default=1)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'inactive')], default='active', max_length=10)),
                ('department', models.CharField(blank=True, choices=[('AI', 'AI'), ('CS', 'CS'), ('IS', 'IS'), ('IT', 'IT'), ('DS', 'DS')], max_length=2, null=True)),
            ],
        ),
    ]
