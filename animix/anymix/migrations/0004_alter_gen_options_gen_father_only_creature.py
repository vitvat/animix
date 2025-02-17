# Generated by Django 5.1.6 on 2025-02-17 17:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anymix', '0003_alter_gen_rank'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gen',
            options={'ordering': ['id']},
        ),
        migrations.AddField(
            model_name='gen',
            name='father_only',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Creature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('rank', models.IntegerField(choices=[(2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)])),
                ('type', models.CharField(choices=[('gold', 'Gold'), ('water', 'Water'), ('air', 'Air'), ('universal', 'Universal')], max_length=10)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('father', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creature_father', to='anymix.gen')),
                ('mother', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creature_mother', to='anymix.gen')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
