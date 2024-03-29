# Generated by Django 2.0 on 2019-04-14 09:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameuser', models.CharField(max_length=200, verbose_name='Имя')),
                ('family', models.CharField(max_length=200, verbose_name='Фамилия')),
                ('role', models.PositiveSmallIntegerField(choices=[(1, 'Студент'), (2, 'Преподаватель')], default=1, verbose_name='Роль')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'ordering': ['nameuser'],
            },
        ),
    ]
