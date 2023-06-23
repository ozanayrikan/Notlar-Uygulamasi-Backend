# Generated by Django 4.2.1 on 2023-06-14 20:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notebooks', '0012_remove_notebook_deleted_at_remove_notes_deleted_at_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notebook',
            options={'ordering': ['id'], 'verbose_name': 'Not defteri', 'verbose_name_plural': 'Not defterleri'},
        ),
        migrations.AlterModelOptions(
            name='notes',
            options={'ordering': ['id'], 'verbose_name': 'Not', 'verbose_name_plural': 'Notlar'},
        ),
        migrations.AlterModelOptions(
            name='taskgroup',
            options={'ordering': ['id'], 'verbose_name': 'Görev grubu', 'verbose_name_plural': 'Görev grupları'},
        ),
        migrations.AlterModelOptions(
            name='tasks',
            options={'ordering': ['rank'], 'verbose_name': 'Görev', 'verbose_name_plural': 'Görevler'},
        ),
        migrations.RemoveField(
            model_name='tasks',
            name='responsible',
        ),
        migrations.AddField(
            model_name='tasks',
            name='assigned_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_to_tasks', to=settings.AUTH_USER_MODEL, verbose_name='Atanacak kullanıcı'),
        ),
    ]