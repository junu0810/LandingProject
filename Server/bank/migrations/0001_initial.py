# Generated by Django 4.0.3 on 2022-04-22 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('bank_uid', models.AutoField(primary_key=True, serialize=False)),
                ('bank_name', models.CharField(max_length=15)),
            ],
        ),
    ]
