# Generated by Django 2.2 on 2019-08-12 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0003_auto_20190812_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familymember',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='family.FamilyMember'),
        ),
    ]
