# Generated by Django 4.2.9 on 2024-01-19 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0002_entry'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='text',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
