# Generated by Django 5.1.4 on 2024-12-15 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileanalyzer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='finderobject',
            name='height',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='finderobject',
            name='pages_count',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='finderobject',
            name='width',
            field=models.IntegerField(default=None, null=True),
        ),
    ]