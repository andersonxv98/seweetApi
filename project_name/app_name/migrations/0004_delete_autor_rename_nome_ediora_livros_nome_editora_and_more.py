# Generated by Django 4.1.7 on 2023-04-01 19:14

import app_name.models
from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app_name', '0003_autor_livros'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Autor',
        ),
        migrations.RenameField(
            model_name='livros',
            old_name='nome_ediora',
            new_name='nome_editora',
        ),
        migrations.AddField(
            model_name='livros',
            name='author',
            field=djongo.models.fields.EmbeddedField(default=1, model_container=app_name.models.Autor),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='livros',
            name='teste',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
