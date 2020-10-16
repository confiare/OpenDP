# Generated by Django 3.1.2 on 2020-10-16 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataverse', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisteredDataverse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('dataverse_url', models.URLField(help_text='No trailing slash.', unique=True)),
                ('active', models.BooleanField(default=True)),
                ('notes', models.TextField(blank=True, help_text='optional')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
