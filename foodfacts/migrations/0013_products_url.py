# Generated by Django 3.0.5 on 2020-05-07 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodfacts', '0012_auto_20200507_0047'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='url',
            field=models.CharField(db_column='url', default='', max_length=600),
        ),
    ]
