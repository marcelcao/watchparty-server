# Generated by Django 4.1.3 on 2024-03-02 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchpartyapi', '0003_partycomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partycomment',
            name='posted_on',
            field=models.DateField(auto_now=True),
        ),
    ]