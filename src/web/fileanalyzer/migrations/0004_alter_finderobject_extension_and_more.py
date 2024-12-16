# Generated by Django 5.1.4 on 2024-12-16 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileanalyzer', '0003_finderobject_file_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finderobject',
            name='extension',
            field=models.CharField(blank=True, default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='finderobject',
            name='file_type',
            field=models.CharField(blank=True, choices=[('I', 'Image'), ('T', 'Text'), ('V', 'Video'), ('A', 'Audio'), ('Z', 'Archive'), ('E', 'Executable'), ('S', 'Script'), ('W', 'Web'), ('D', 'Data'), ('U', 'Unknown')], default=None, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='finderobject',
            name='height',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='finderobject',
            name='pages_count',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='finderobject',
            name='path',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='finderobject',
            name='type',
            field=models.CharField(choices=[('F', 'File'), ('FD', 'Folder'), ('U', 'Unknown')], default='U', max_length=2),
        ),
        migrations.AlterField(
            model_name='finderobject',
            name='width',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
