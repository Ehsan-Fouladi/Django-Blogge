# Generated by Django 4.0.5 on 2022-08-26 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0003_alter_profile_options_ticket'),
    ]

    operations = [
        migrations.CreateModel(
            name='nameusergo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
        ),
    ]
