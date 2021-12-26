# Generated by Django 4.0 on 2021-12-23 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0008_alter_modelformregistration_phone'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='modelformregistration',
            options={'ordering': ('-date',)},
        ),
        migrations.RemoveField(
            model_name='modelformregistration',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='modelformregistration',
            name='time',
        ),
        migrations.AlterField(
            model_name='modelformregistration',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]