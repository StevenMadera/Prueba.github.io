# Generated by Django 4.2.6 on 2023-10-22 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cocina', '0003_alter_receta_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receta',
            name='codigo',
            field=models.CharField(default='313464', editable=False, max_length=6, primary_key=True, serialize=False),
        ),
    ]
