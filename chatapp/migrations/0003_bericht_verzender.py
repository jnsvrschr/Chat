# Generated by Django 4.0.5 on 2022-07-29 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0002_rename_berichts_bericht_alter_bericht_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='bericht',
            name='verzender',
            field=models.CharField(default='iets', max_length=50),
            preserve_default=False,
        ),
    ]