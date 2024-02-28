# Generated by Django 4.1.3 on 2024-02-27 05:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('watchpartyapi', '0002_alter_show_show_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartyComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=600)),
                ('posted_on', models.DateField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='watchpartyapi.user')),
                ('party', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='watchpartyapi.party')),
            ],
        ),
    ]