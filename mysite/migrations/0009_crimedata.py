# Generated by Django 4.2.1 on 2023-05-29 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0008_rename_crimedata_categorydata_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='crimeData',
            fields=[
                ('crime_id', models.IntegerField(primary_key=True, serialize=False)),
                ('year', models.IntegerField(default=0)),
                ('month', models.IntegerField(default=0)),
                ('quantity', models.IntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.categorydata')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.citydata')),
            ],
            options={
                'ordering': ('year',),
            },
        ),
    ]
