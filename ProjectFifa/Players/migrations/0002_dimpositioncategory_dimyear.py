# Generated by Django 3.2.8 on 2021-11-14 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Players', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DimPositioncategory',
            fields=[
                ('position_categoryid', models.IntegerField(primary_key=True, serialize=False)),
                ('position_category', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Dim.Positioncategory',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DimYear',
            fields=[
                ('year', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'Dim.Year',
            },
        ),
    ]