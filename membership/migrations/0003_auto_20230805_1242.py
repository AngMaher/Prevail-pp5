# Generated by Django 3.2.20 on 2023-08-05 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0002_alter_membership_class_choice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='class_choice',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='membership',
            name='member_first_name',
            field=models.CharField(max_length=50),
        ),
    ]
