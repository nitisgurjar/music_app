# Generated by Django 4.2.1 on 2023-06-02 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_name', models.CharField(max_length=50)),
                ('singer_name', models.CharField(max_length=50)),
                ('song_image', models.ImageField(upload_to='image')),
                ('song_audio', models.FileField(upload_to='song')),
                ('upload_time', models.DateTimeField(auto_now_add=True)),
                ('duration', models.IntegerField()),
            ],
        ),
    ]
