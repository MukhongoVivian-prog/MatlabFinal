# Generated by Django 5.1.3 on 2024-11-13 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0004_alter_patient_phonenumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('Email', models.EmailField(max_length=254)),
                ('Phone', models.CharField(max_length=20)),
                ('Date', models.DateTimeField()),
                ('Department', models.CharField(max_length=200)),
                ('Doctor', models.CharField(max_length=200)),
                ('message', models.TextField()),
            ],
        ),
    ]
