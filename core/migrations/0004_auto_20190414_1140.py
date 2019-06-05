# Generated by Django 2.0 on 2019-04-14 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190414_1051'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='modeltestansweruser',
            options={},
        ),
        migrations.AddField(
            model_name='modeltestansweruser',
            name='result',
            field=models.IntegerField(blank=True, null=True, verbose_name='полученый бал за тест'),
        ),
        migrations.AddField(
            model_name='modeltestirovanieuser',
            name='result',
            field=models.IntegerField(blank=True, null=True, verbose_name='полученый бал за тест'),
        ),
        migrations.AlterField(
            model_name='modeltestansweruser',
            name='status_answer',
            field=models.BooleanField(default=False, verbose_name='Статус пройденности ответа'),
        ),
    ]