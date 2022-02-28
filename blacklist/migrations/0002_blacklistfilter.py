# Generated by Django 3.1.1 on 2021-06-21 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blacklist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlacklistFilter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': 'Smart Filter: User Has Blacklisted Char',
                'verbose_name_plural': 'Smart Filter: User Has Blacklisted Char',
            },
        ),
    ]
