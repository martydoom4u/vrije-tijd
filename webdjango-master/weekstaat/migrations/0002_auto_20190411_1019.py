# Generated by Django 2.0.2 on 2019-04-11 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('weekstaat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weekstaat',
            name='week',
            field=models.ForeignKey(default=15, on_delete=django.db.models.deletion.CASCADE, to='weekstaat.Week'),
        ),
    ]
