# Generated by Django 2.2.7 on 2019-12-06 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='volunteerRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('contact_no', models.IntegerField()),
                ('email', models.EmailField(max_length=25)),
                ('address', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'volunteer registration',
                'db_table': 'tbl_volunteerRegistration',
            },
        ),
    ]
