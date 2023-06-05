# Generated by Django 4.2.1 on 2023-05-29 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_alter_populationdata_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='cityData',
            fields=[
                ('city_id', models.IntegerField(primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('city_id',),
            },
        ),
        migrations.RenameField(
            model_name='populationdata',
            old_name='Dist',
            new_name='dist',
        ),
    ]
