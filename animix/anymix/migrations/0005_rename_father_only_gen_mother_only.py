# Generated by Django 4.2.19 on 2025-02-17 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anymix', '0004_alter_gen_options_gen_father_only_creature'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gen',
            old_name='father_only',
            new_name='mother_only',
        ),
    ]
