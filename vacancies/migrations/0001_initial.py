# Generated by Django 4.2.20 on 2025-03-11 18:04

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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('salary', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('description', models.TextField()),
                ('experience', models.CharField(choices=[('entry', 'Entry Level'), ('mid', 'Mid Level'), ('senior', 'Senior Level')], default='entry', max_length=50)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacancies.category')),
            ],
        ),
    ]
