# Generated by Django 4.2.1 on 2023-05-29 04:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_crimedata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='populationdata',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.citydata'),
        ),
    ]