# -*- coding:utf-8 -*-

from django.db import models
from django.contrib.auth.models import User



		
class UserProfile(models.Model):
    ROLE_CHOICES = (
        (1, u'Пользователь'),
        (2, u'Администратор'),
    )
    user = models.ForeignKey(User, verbose_name = 'Пользователь', on_delete=models.CASCADE)
    nameuser = models.CharField(max_length=200,verbose_name = 'Имя')
    family = models.CharField(max_length=200,verbose_name = 'Фамилия')
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, verbose_name = 'Роль', default=ROLE_CHOICES[0][0])
    def __str__(self):
        return '%s %s' % (self.nameuser, self.family)
    class Meta:
        ordering = ["nameuser"]
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        

class Text(models.Model):
    bosch = models.TextField(blank=True, default="")
    kis = models.TextField(blank=True, default="")
    kts = models.TextField(blank=True, default="")
    kav = models.TextField(blank=True, default="")
    k_system = models.TextField(blank=True, default="")
    k_inst_unist = models.TextField(blank=True, default="")
    k_license = models.TextField(blank=True, default="")
    k_update = models.TextField(blank=True, default="")
    k_check = models.TextField(blank=True, default="")
    kav_limit = models.TextField(blank=True, default="")
    kis_limit = models.TextField(blank=True, default="")
    kts_limit = models.TextField(blank=True, default="")

    kpm = models.TextField(blank=True, default="")
    kpm_inst_unist = models.TextField(blank=True, default="")
    kpm_job = models.TextField(blank=True, default="")
    kpm_face1 = models.TextField(blank=True, default="")
    kpm_face2 = models.TextField(blank=True, default="")
    kpm_license = models.TextField(blank=True, default="")
    kpm_security = models.TextField(blank=True, default="")
    kpm_task = models.TextField(blank=True, default="")
    kpm_setting = models.TextField(blank=True, default="")

    ksk = models.TextField(blank=True, default="")
    ksk_inst_unist = models.TextField(blank=True, default="")
    ksk_face = models.TextField(blank=True, default="")
    ksk_license = models.TextField(blank=True, default="")
    ksk_license2 = models.TextField(blank=True, default="")
    ksk_setting = models.TextField(blank=True, default="")

    ksec = models.TextField(blank=True, default="")
    ksec_system = models.TextField(blank=True, default="")
    ksec_inst_unist = models.TextField(blank=True, default="")
    ksec_license = models.TextField(blank=True, default="")
    ksec_traffic = models.TextField(blank=True, default="")
    ksec_setting = models.TextField(blank=True, default="")

    myk = models.TextField(blank=True, default="")
    myk_device1 = models.TextField(blank=True, default="")
    myk_device2 = models.TextField(blank=True, default="")
    myk_license = models.TextField(blank=True, default="")
    myk_user = models.TextField(blank=True, default="")
   
        
class ModelTestirovanie(models.Model):
    name = models.CharField(max_length=250,verbose_name='Название')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Тестирования'
        verbose_name_plural = 'Тестирования'
        
        
class ModelTestQuestions(models.Model):
    modeltest = models.ForeignKey(ModelTestirovanie, null = True, on_delete=models.CASCADE)
    name = models.TextField(verbose_name='Название вопроса',blank=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Наз. вопросов'
        verbose_name_plural = 'Наз. вопросов'
        

class ModelTestAnswer(models.Model):
    questions = models.ForeignKey(ModelTestQuestions, null = True, on_delete=models.CASCADE)
    otvet = models.TextField(verbose_name='ответ', blank=True, null = True)
    status = models.BooleanField(verbose_name = 'Статус правильности', default = None, blank=True)
    def __str__(self):
        return self.otvet
    class Meta:
        verbose_name = 'Ответы на вопросы'
        verbose_name_plural = 'Ответы на вопросы'
        

# прохождение тестирования пользователей
class ModelTestirovanieUser(models.Model):
    userid = models.ForeignKey(User, null = True, on_delete=models.CASCADE)
    modeltest = models.ForeignKey(ModelTestirovanie, null = True, on_delete=models.CASCADE)
    status = models.BooleanField(verbose_name = 'Статус пройденности', default = False, blank=True)
    result = models.IntegerField(verbose_name='полученый бал за тест', null = True, blank=True )


class ModelTestAnswerUser(models.Model):
    modeltestirovanieuser = models.ForeignKey(ModelTestirovanieUser, null = True, on_delete=models.CASCADE)
    questions = models.ForeignKey(ModelTestQuestions, null = True, on_delete=models.CASCADE)
    answer = models.TextField(verbose_name='ответ', blank=True)
    result = models.IntegerField(verbose_name='полученый бал за тест', null = True, blank=True )
    status_answer = models.BooleanField(verbose_name = 'Статус пройденности ответа', default = False)
