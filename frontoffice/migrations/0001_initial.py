# Generated by Django 3.2 on 2021-04-30 23:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adresse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ville', models.CharField(max_length=200)),
                ('rue', models.CharField(max_length=200)),
                ('no', models.IntegerField()),
                ('cp', models.IntegerField()),
                ('departement', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Logement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nbPieces', models.IntegerField()),
                ('surface', models.FloatField()),
                ('photo', models.CharField(max_length=200)),
                ('loyer', models.FloatField()),
                ('charges', models.FloatField()),
                ('partAgence', models.FloatField()),
                ('adresse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontoffice.adresse')),
            ],
        ),
        migrations.CreateModel(
            name='Personne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('prenom', models.CharField(max_length=200)),
                ('adresse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontoffice.adresse')),
            ],
        ),
        migrations.CreateModel(
            name='Appartement',
            fields=[
                ('logement_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='frontoffice.logement')),
                ('etage', models.IntegerField()),
                ('ascenseur', models.BooleanField()),
                ('garage', models.BooleanField()),
            ],
            bases=('frontoffice.logement',),
        ),
        migrations.CreateModel(
            name='Collaborateur',
            fields=[
                ('personne_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='frontoffice.personne')),
                ('courriel', models.CharField(max_length=200)),
                ('telephone', models.CharField(max_length=200)),
            ],
            bases=('frontoffice.personne',),
        ),
        migrations.CreateModel(
            name='Locataire',
            fields=[
                ('personne_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='frontoffice.personne')),
                ('adresse_origine', models.CharField(max_length=300)),
            ],
            bases=('frontoffice.personne',),
        ),
        migrations.CreateModel(
            name='Maison',
            fields=[
                ('logement_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='frontoffice.logement')),
                ('surface_terrain', models.FloatField()),
                ('grenier', models.BooleanField()),
            ],
            bases=('frontoffice.logement',),
        ),
        migrations.CreateModel(
            name='Proprietaire',
            fields=[
                ('personne_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='frontoffice.personne')),
                ('cne', models.CharField(max_length=200)),
            ],
            bases=('frontoffice.personne',),
        ),
        migrations.AddField(
            model_name='logement',
            name='collaborateur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontoffice.collaborateur'),
        ),
        migrations.AddField(
            model_name='logement',
            name='proprietaire',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontoffice.proprietaire'),
        ),
        migrations.CreateModel(
            name='Bail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.IntegerField()),
                ('loyerTTC', models.FloatField()),
                ('date_debut', models.DateField(auto_now_add=True)),
                ('duree', models.DurationField()),
                ('logement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontoffice.logement')),
                ('locataire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontoffice.locataire')),
            ],
        ),
    ]
