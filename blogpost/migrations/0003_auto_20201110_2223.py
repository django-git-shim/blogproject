# Generated by Django 3.1.3 on 2020-11-10 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogpost', '0002_blogmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='samplemodel',
            old_name='title',
            new_name='title1',
        ),
    ]
