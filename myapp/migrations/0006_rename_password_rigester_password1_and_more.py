# Generated by Django 4.0.2 on 2022-03-27 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_rigester'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rigester',
            old_name='password',
            new_name='password1',
        ),
        migrations.AddField(
            model_name='rigester',
            name='password2',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
