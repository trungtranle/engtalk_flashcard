# Generated by Django 2.1.2 on 2018-10-16 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flashcard', '0005_auto_20181016_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='writing',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='flashcard.Writing_question'),
        ),
    ]
