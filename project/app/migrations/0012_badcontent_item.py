# Generated by Django 3.1.2 on 2020-10-06 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20201006_1313'),
    ]

    operations = [
        migrations.AddField(
            model_name='badcontent',
            name='item',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='app.item'),
            preserve_default=False,
        ),
    ]
