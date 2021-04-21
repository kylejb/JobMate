# Generated by Django 3.1.7 on 2021-03-31 23:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20210330_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='required_experience',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AlterField(
            model_name='listing',
            name='salary',
            field=models.CharField(default='', max_length=7),
        ),
        migrations.AlterField(
            model_name='listing',
            name='tech_stack',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='listings.techstack'),
        ),
    ]
