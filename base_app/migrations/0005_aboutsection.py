# Generated by Django 4.0 on 2021-12-22 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0004_herosection'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_1', models.CharField(max_length=30)),
                ('title_2', models.CharField(max_length=30)),
                ('desc_1', models.TextField(max_length=150)),
                ('desc_2', models.TextField(max_length=150)),
                ('desc_3', models.TextField(max_length=150)),
                ('feature_1', models.TextField(max_length=100)),
                ('feature_2', models.TextField(max_length=100)),
                ('feature_3', models.TextField(max_length=100)),
            ],
        ),
    ]
