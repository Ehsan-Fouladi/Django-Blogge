# Generated by Django 4.0.5 on 2022-07-24 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_app', '0022_remove_post_bode'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='bode',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]