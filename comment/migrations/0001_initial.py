# Generated by Django 5.0 on 2024-02-29 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('content', models.TextField()),
                ('created_time', models.DateTimeField(auto_now=True)),
                ('modified_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]