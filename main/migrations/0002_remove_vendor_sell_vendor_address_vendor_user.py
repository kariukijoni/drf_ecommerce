# Generated by Django 4.2.5 on 2023-09-22 11:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='sell',
        ),
        migrations.AddField(
            model_name='vendor',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='vendor',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
