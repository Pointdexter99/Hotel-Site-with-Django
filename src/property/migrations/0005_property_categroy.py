# Generated by Django 3.0.5 on 2020-04-12 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='categroy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='property.Category'),
        ),
    ]
