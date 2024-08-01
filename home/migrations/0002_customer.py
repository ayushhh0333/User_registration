# Generated by Django 5.0.7 on 2024-07-24 13:09

from django.db import migrations, models





class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('contact', models.CharField(max_length=14)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.TextField(max_length=250)),
                
            ],
        ),
    ]
