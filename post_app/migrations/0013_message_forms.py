# Generated by Django 4.0.5 on 2022-07-18 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_app', '0012_alter_comment_parent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message_forms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=150)),
                ('Password', models.CharField(max_length=150)),
                ('Year_time', models.DateTimeField(blank=True)),
            ],
        ),
    ]
