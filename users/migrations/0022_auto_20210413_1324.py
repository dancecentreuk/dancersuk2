# Generated by Django 3.1.7 on 2021-04-13 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0021_dancersprofile_dress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dancersprofile',
            name='dress',
            field=models.CharField(blank=True, choices=[('N/A', 'Not Applicable'), ('4', 'UK 4'), ('6', 'UK 6'), ('8', 'UK 8'), ('10', 'UK 10'), ('12', 'UK 12'), ('14', 'UK 14'), ('16', 'UK 16'), ('18', 'UK 18'), ('20', 'UK 20'), ('22', 'UK 22'), ('24', 'UK 24'), ('26', 'UK 26'), ('28', 'UK 28'), ('30', 'UK 30')], default=0, max_length=20),
        ),
    ]