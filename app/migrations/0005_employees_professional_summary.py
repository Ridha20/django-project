# Generated by Django 4.2.6 on 2023-11-20 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_project_roles_responsibilities'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='professional_summary',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
