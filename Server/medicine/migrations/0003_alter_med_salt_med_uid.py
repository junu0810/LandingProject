# Generated by Django 4.0.3 on 2022-04-22 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0002_med_salt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='med_salt',
            name='med_uid',
            field=models.ForeignKey(db_column='med_uid', on_delete=django.db.models.deletion.CASCADE, related_name='med_salt_set', to='medicine.medicine'),
        ),
    ]