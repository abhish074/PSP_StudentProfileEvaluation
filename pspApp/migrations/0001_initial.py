# Generated by Django 3.0.1 on 2020-04-08 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentProfileModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('gre', models.IntegerField(default=0)),
                ('paper', models.CharField(max_length=30)),
                ('workex', models.IntegerField(default=0)),
                ('undergrad', models.FloatField(default=0)),
                ('quants', models.IntegerField(default=0)),
                ('verbal', models.IntegerField(default=0)),
                ('ielts', models.FloatField(default=0)),
                ('toefl', models.IntegerField(default=0)),
            ],
        ),
    ]
