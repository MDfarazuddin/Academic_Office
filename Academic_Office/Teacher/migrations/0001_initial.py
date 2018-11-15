# Generated by Django 2.1.3 on 2018-11-15 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('T_id', models.CharField(max_length=15)),
                ('T_name', models.CharField(max_length=20)),
                ('T_course', models.CharField(default='not assigned', max_length=20)),
                ('slug', models.SlugField()),
                ('T_email', models.EmailField(default='farazuddin.m17@iiits.in', max_length=254)),
            ],
        ),
    ]
