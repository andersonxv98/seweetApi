# Generated by Django 4.1.7 on 2023-04-01 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClienteCobranca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('cpf', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=13)),
                ('street', models.CharField(max_length=200)),
                ('neighborhood', models.CharField(max_length=200)),
                ('zipcode', models.CharField(max_length=8)),
                ('city', models.CharField(max_length=50)),
                ('complement', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('value', models.IntegerField()),
                ('expire_at', models.CharField(max_length=50)),
                ('sigla', models.CharField(max_length=50)),
            ],
        ),
    ]
