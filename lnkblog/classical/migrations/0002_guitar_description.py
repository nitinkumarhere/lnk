# Generated by Django 2.0.4 on 2018-05-03 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classical', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='guitar',
            name='description',
            field=models.TextField(default='First built.'),
            preserve_default=False,
        ),
    ]
