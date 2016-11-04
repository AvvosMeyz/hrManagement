#-*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save, post_init
from datetime import datetime, timedelta


statusNote = (
    (0, 'Devam ediyor'),
    (1, 'Bitti'),
    (2, 'Ertelendi'),
    (3, 'Yarın Yapılacak'),
)


class Tasks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Kullanıcı')
    note = models.CharField(max_length=500, blank=False, verbose_name='Görev')
    status = models.IntegerField(choices=statusNote, default=0, editable=True, verbose_name='Durum')
    create_date = models.DateField(auto_now_add=True, verbose_name='Oluşturma Tarihi')
    done_date = models.DateField(auto_now=True, verbose_name=u'Son Degiştirilen Tarih')
    plan_date = models.DateField(verbose_name='Planlanan Tarih', null=True, blank=True, default=None)

    class Meta:
        verbose_name = u'Görev'
        verbose_name_plural = u'Görevler'


    def __unicode__(self):
        return self.note

    @staticmethod
    def post_save(sender, **kwargs):
        instance = kwargs.get('instance')
        created = kwargs.get('created')
        if instance.status == 3:
            instance.plan_date = instance.create_date + timedelta(days=1)


post_save.connect(Tasks.post_save, sender=Tasks)
post_init.connect(Tasks.post_save, sender=Tasks)


class Comments(models.Model):
    user = models.ManyToManyField(User, )
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500, blank=False, verbose_name="Yorum")

    class Meta:
        verbose_name = u'Yorum'
        verbose_name_plural = u'Yorumlar'


    def get_user(self):
        return "\n".join([p.username for p in self.user.all()])

    def __unicode__(self):
        return self.comment
