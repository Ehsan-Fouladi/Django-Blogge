# Generated by Django 4.0.5 on 2022-08-26 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0006_alter_profile_options_ticket'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ticket',
            options={'verbose_name': 'تیکت های کاربر', 'verbose_name_plural': 'تیکت'},
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='title',
        ),
    ]
