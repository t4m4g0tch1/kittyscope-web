# Generated by Django 5.1.4 on 2024-12-11 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FinderObject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('F', 'File'), ('FD', 'Fold'), ('U', 'Unknown')], default='U', max_length=2)),
                ('name', models.CharField(max_length=255)),
                ('path', models.CharField(max_length=255)),
                ('size', models.BigIntegerField(default=0)),
                ('extension', models.CharField(max_length=255)),
                ('last_access', models.DateTimeField()),
                ('last_modified', models.DateTimeField()),
            ],
        ),
    ]