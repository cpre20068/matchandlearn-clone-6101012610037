# Generated by Django 3.0.3 on 2020-02-12 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Savechat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, max_length=200)),
                ('chat', models.TextField(blank=True, max_length=200000000000000)),
            ],
        ),
    ]
