# Generated by Django 5.0.6 on 2024-05-17 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_video_upload_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video_upload',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='thumbnail/'),
        ),
    ]
