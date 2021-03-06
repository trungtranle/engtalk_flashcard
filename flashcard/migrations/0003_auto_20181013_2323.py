# Generated by Django 2.1 on 2018-10-13 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flashcard', '0002_auto_20181009_1824'),
    ]

    operations = [
        migrations.CreateModel(
            name='Writing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=40)),
                ('essay', models.TextField()),
                ('added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Writing_question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.PositiveIntegerField()),
                ('question', models.TextField()),
                ('picture', models.ImageField(upload_to='img/')),
            ],
        ),
        migrations.AddField(
            model_name='writing',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='flashcard.Writing_question'),
        ),
    ]
