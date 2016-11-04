#-*- coding: utf-8 -*-
from django.contrib import admin
from django.db import models
from .models import Tasks, Comments
from django.contrib.auth.models import User
from django_cron import CronJobBase, Schedule
from django.conf.urls import url
from django.template.response import TemplateResponse
from datetime import datetime


# Gece 00:01'de 1 kere kontrol ediyor
class MyCronJob(CronJobBase):
    #RUN_EVERY_MINS = 1
    RUN_AT_TIMES = ['00:01']
    #schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    schedule = Schedule(run_at_times=RUN_AT_TIMES)
    code = 'app.MyCronJob'

    def do(self):
        Tasks.objects.filter(plan_date__lte=datetime.today()).update(status=0)


CRON_CLASSES = [
    "modules.tasks.admin.MyCronJob",
    #  ...
]


class TasksAdmin(admin.ModelAdmin):
    list_display = ['user', 'note', 'status', 'create_date', 'done_date', 'plan_date']
    search_fields = ('status',)

    # Duruma göre arama
    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super(TasksAdmin, self).get_search_results(request, queryset, search_term)
        try:
            search_term_as_int = int(search_term)
        except ValueError:
            pass
        else:
            queryset |= self.model.objects.filter(status=search_term_as_int, user=request.user)
        return queryset, use_distinct


    # Giriş yapan kullanıcı sadece kendi tasklarını görür.
    def get_queryset(self, request):
        qs = super(TasksAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    # Giriş yapmış kullanıcı sadece kendi adına task ekler.
    def formfield_for_foreignkey(self, db_field, request, **kwargs):

        if db_field.name == 'user':
            kwargs['queryset'] = User.objects.filter(id=request.user.id)
            return super(TasksAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


class CommentsAdmin(admin.ModelAdmin):
    list_display = ['get_user', 'task', 'comment', ]

admin.site.register(Tasks, TasksAdmin)
admin.site.register(Comments, CommentsAdmin)
