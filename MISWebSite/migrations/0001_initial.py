# Generated by Django 4.2.3 on 2023-07-20 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='non', max_length=50)),
                ('email', models.EmailField(default='non', max_length=100)),
                ('Phone', models.IntegerField(default='0', max_length=12)),
                ('textarea', models.TextField(default='non', max_length=500)),
            ],
        ),
    ]
