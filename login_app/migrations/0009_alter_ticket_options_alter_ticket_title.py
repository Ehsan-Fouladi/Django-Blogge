# Generated by Django 4.0.5 on 2022-08-26 19:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('login_app', '0008_ticket_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ticket',
            options={'verbose_name': 'تیکت های کاربر', 'verbose_name_plural': 'تیکت ها'},
        ),
        migrations.AlterField(
            model_name='ticket',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
