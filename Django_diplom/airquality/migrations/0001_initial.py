# Generated by Django 2.2.2 on 2019-06-12 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('time', models.DateTimeField(blank=True, null=True)),
                ('aqi', models.IntegerField()),
            ],
        ),
    ]
