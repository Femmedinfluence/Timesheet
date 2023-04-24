# Generated by Django 4.1.7 on 2023-04-04 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employe',
            fields=[
                ('id_empl', models.AutoField(primary_key=True, serialize=False)),
                ('nom_empl', models.CharField(max_length=255)),
                ('prenom_empl', models.CharField(max_length=255)),
                ('fonct_empl', models.CharField(max_length=255)),
                ('mail_empl', models.CharField(max_length=255)),
                ('password_empl', models.CharField(max_length=255)),
                ('adresse_empl', models.CharField(max_length=255)),
                ('contact_empl', models.IntegerField()),
                ('localisation_empl', models.CharField(max_length=255)),
                ('genre_empl', models.CharField(max_length=255)),
                ('signature_empl', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'employe',
            },
        ),
        migrations.CreateModel(
            name='Feuilletemps',
            fields=[
                ('id_ftemps', models.AutoField(primary_key=True, serialize=False)),
                ('date_debut', models.TextField()),
                ('date_fin', models.TextField(blank=True, null=True)),
                ('date_jour', models.TextField()),
                ('nombre_heure', models.IntegerField()),
                ('type_conge', models.CharField(max_length=255)),
                ('observations', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'feuilletemps',
            },
        ),
        migrations.CreateModel(
            name='Projet',
            fields=[
                ('code_projet', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'projet',
            },
        ),
        migrations.CreateModel(
            name='Travail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_projet', models.ForeignKey(blank=True, db_column='code_projet', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='timeapp.projet')),
                ('id_empl', models.ForeignKey(blank=True, db_column='id_empl', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='timeapp.employe')),
            ],
            options={
                'db_table': 'travail',
            },
        ),
        migrations.CreateModel(
            name='Superviseur',
            fields=[
                ('id_superv', models.AutoField(primary_key=True, serialize=False)),
                ('libelle', models.CharField(max_length=42)),
                ('id_empl', models.ForeignKey(db_column='id_empl', on_delete=django.db.models.deletion.DO_NOTHING, to='timeapp.employe')),
                ('id_ftemps', models.ForeignKey(db_column='id_ftemps', on_delete=django.db.models.deletion.DO_NOTHING, to='timeapp.feuilletemps')),
            ],
            options={
                'db_table': 'superviseur',
            },
        ),
        migrations.CreateModel(
            name='Renseigner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_empl', models.ForeignKey(blank=True, db_column='id_empl', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='timeapp.employe')),
                ('id_ftemps', models.ForeignKey(blank=True, db_column='id_ftemps', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='timeapp.feuilletemps')),
            ],
            options={
                'db_table': 'renseigner',
            },
        ),
        migrations.CreateModel(
            name='Departement',
            fields=[
                ('id_dptmt', models.AutoField(primary_key=True, serialize=False)),
                ('nom_dptmt', models.CharField(max_length=255)),
                ('libelle', models.CharField(max_length=255)),
                ('id_empl', models.ForeignKey(db_column='id_empl', on_delete=django.db.models.deletion.DO_NOTHING, to='timeapp.employe')),
            ],
            options={
                'db_table': 'departement',
            },
        ),
    ]
