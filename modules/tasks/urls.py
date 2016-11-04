from django.conf.urls import url,include
from . import views
from modules.tasks.forms import LoginForm


app_name = 'tasks'

urlpatterns = [
    #home
    url(r'^$', views.home, name='home'),

]