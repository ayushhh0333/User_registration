# Generated by Django 5.0.7 on 2024-08-01 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_customer_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='state',
            field=models.TextField(default=0),
        ),
    ]
