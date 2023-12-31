# Generated by Django 4.2.1 on 2023-06-11 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notebooks', '0009_alter_notebook_options_alter_notes_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tasks',
            options={'ordering': ['rank']},
        ),
        migrations.AddField(
            model_name='tasks',
            name='rank',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='notebook',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notebook_tasks', to='notebooks.notebook'),
        ),
    ]
