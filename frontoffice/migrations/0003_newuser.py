# Generated by Django 3.2.2 on 2021-05-17 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontoffice', '0002_rename_cnl_proprietaire_cne'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=150)),
                ('Email', models.CharField(max_length=150)),
                ('Pwd', models.CharField(max_length=150)),
                ('Age', models.IntegerField()),
            ],
        ),
    ]
