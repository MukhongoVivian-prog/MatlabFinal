# Generated by Django 5.1.3 on 2024-11-13 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0003_patient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='phonenumber',
            field=models.CharField(max_length=50),
        ),
    ]