# Generated by Django 2.0 on 2019-04-14 10:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_auto_20190414_0931'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelTestAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otvet', models.TextField(blank=True, null=True, verbose_name='ответ')),
                ('status', models.BooleanField(default=None, verbose_name='Статус правильности')),
            ],
            options={
                'verbose_name': 'Ответы на вопросы',
                'verbose_name_plural': 'Ответы на вопросы',
            },
        ),
        migrations.CreateModel(
            name='ModelTestAnswerUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(blank=True, verbose_name='ответ')),
                ('status_answer', models.BooleanField(default=False, verbose_name='Статус ответа')),
            ],
            options={
                'verbose_name': 'Ответы на вопросы юзеров',
                'verbose_name_plural': 'Ответы на вопросы юзеров',
            },
        ),
        migrations.CreateModel(
            name='ModelTestirovanie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Тестирования',
                'verbose_name_plural': 'Тестирования',
            },
        ),
        migrations.CreateModel(
            name='ModelTestirovanieUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False, verbose_name='Статус пройденности')),
                ('modeltest', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.ModelTestirovanie')),
                ('userid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ModelTestQuestions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, verbose_name='Название вопроса')),
                ('modeltest', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.ModelTestirovanie')),
            ],
            options={
                'verbose_name': 'Наз. вопросов',
                'verbose_name_plural': 'Наз. вопросов',
            },
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='role',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Пользователь'), (2, 'Администратор')], default=1, verbose_name='Роль'),
        ),
        migrations.AddField(
            model_name='modeltestansweruser',
            name='modeltestirovanieuser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.ModelTestirovanieUser'),
        ),
        migrations.AddField(
            model_name='modeltestansweruser',
            name='questions',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.ModelTestQuestions'),
        ),
        migrations.AddField(
            model_name='modeltestanswer',
            name='questions',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.ModelTestQuestions'),
        ),
    ]