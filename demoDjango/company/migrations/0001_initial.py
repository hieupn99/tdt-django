# Generated by Django 3.0.2 on 2021-05-04 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=50)),
                ('price', models.FloatField(null=True)),
                ('date', models.DateField(null=True)),
            ],
        ),
    ]
