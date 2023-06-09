# Generated by Django 4.1.7 on 2023-04-01 19:47

import app_name.models
from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app_name', '0004_delete_autor_rename_nome_ediora_livros_nome_editora_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('idade', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='livros',
            name='author',
        ),
        migrations.AddField(
            model_name='livros',
            name='autor',
            field=djongo.models.fields.ArrayField(model_container=app_name.models.Autor, null=True),
        ),
    ]
