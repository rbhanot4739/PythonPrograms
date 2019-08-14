# Generated by Django 2.2 on 2019-08-12 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0002_familymember_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='familymember',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='familymember',
            name='job',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
