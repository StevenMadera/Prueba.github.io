# Generated by Django 4.2.6 on 2023-10-22 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cocina', '0004_alter_receta_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receta',
            name='codigo',
            field=models.CharField(max_length=6, primary_key=True, serialize=False),
        ),
    ]
