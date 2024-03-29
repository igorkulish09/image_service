# Generated by Django 5.0.1 on 2024-01-19 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeneratedImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('color', models.CharField(max_length=7)),
                ('title', models.CharField(max_length=255)),
                ('subTitle', models.CharField(max_length=255)),
                ('site', models.CharField(max_length=255)),
                ('image_url', models.URLField()),
            ],
        ),
    ]
