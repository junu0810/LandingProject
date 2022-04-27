# Generated by Django 4.0.3 on 2022-04-22 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cus_req',
            fields=[
                ('req_uid', models.AutoField(primary_key=True, serialize=False)),
                ('req_name', models.CharField(max_length=15)),
                ('req_phone', models.CharField(max_length=13)),
                ('req_med_detail', models.TextField()),
                ('req_joindate', models.DateField(auto_now_add=True)),
                ('req_status', models.BooleanField(default=False)),
            ],
        ),
    ]
