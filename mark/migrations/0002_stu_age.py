# Generated by Django 2.2 on 2019-05-13 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mark', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stu',
            name='age',
            field=models.IntegerField(choices=[(1, '中1'), (2, '中2'), (3, '中3'), (4, '高1'), (5, '高2'), (6, '高3'), (7, '講師')], default=1, verbose_name='学年'),
        ),
    ]
