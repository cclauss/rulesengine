# Generated by Django 2.1 on 2018-08-10 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rules', '0003_auto_20180809_2243'),
    ]

    operations = [
        migrations.AddField(
            model_name='rule',
            name='negated_surt',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='rulechange',
            name='negated_surt',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='rule',
            name='surt',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='rulechange',
            name='surt',
            field=models.TextField(),
        ),
    ]
