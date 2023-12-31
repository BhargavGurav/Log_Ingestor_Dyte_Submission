# Generated by Django 3.2.2 on 2023-11-18 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=100)),
                ('resourceId', models.CharField(max_length=50)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('spanId', models.CharField(max_length=50)),
                ('commit', models.CharField(max_length=50)),
            ],
        ),
    ]
