# Generated by Django 3.0.3 on 2020-03-08 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jovem', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('cpf', models.CharField(max_length=200)),
                ('email1', models.CharField(max_length=200)),
                ('email2', models.CharField(blank=True, max_length=200, null=True)),
                ('celular1', models.CharField(max_length=50)),
                ('celular2', models.CharField(blank=True, max_length=50, null=True)),
                ('instituicao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='jovem.Instituicao')),
            ],
        ),
    ]
