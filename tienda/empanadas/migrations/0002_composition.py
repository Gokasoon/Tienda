# Generated by Django 5.1 on 2024-09-03 12:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empanadas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Composition',
            fields=[
                ('idComposition', models.AutoField(primary_key=True, serialize=False)),
                ('quantite', models.CharField(max_length=100)),
                ('empanada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empanadas.empanada')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empanadas.ingredient')),
            ],
            options={
                'unique_together': {('ingredient', 'empanada')},
            },
        ),
    ]
