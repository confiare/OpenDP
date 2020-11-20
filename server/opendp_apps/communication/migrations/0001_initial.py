# Generated by Django 3.1.2 on 2020-11-11 00:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_type', models.CharField(choices=[('text/plain', 'Plain Text'), ('application/html', 'Html')], max_length=128)),
                ('message_template', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_email', models.CharField(max_length=128)),
                ('to_email', models.CharField(max_length=128)),
                ('subject', models.CharField(max_length=128)),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='communication.emailmessage')),
            ],
        ),
    ]