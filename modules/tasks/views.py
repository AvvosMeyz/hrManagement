#-*- coding: utf-8 -*-
from django.shortcuts import render,get_object_or_404, redirect
from .models import Tasks, Comments,User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from django.contrib.auth import authenticate,login
from django.views.generic import View
from datetime import date,datetime
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import forms
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from modules.tasks.forms import LoginForm


def index(request):
    context = {'user_list': User.objects.all()}
    return render(request, 'tasks/index.html', context)


@login_required(login_url="login/")
def home(request):
    username = None
    if request.user.is_authenticated():
        username = request.user.get_full_name()
    result = Tasks.objects.filter(user=request.user).order_by('create_date' )
    context = {'username': username,
               'result': result}
    return render(request, 'tasks/tasks.html', context)

#class IndexView(generic.ListView):
 #   template_name = 'tasks/index.html'
  #  context_object_name = 'all_user'

   # def get_queryset(self):
    #    return User.objects.all()





''' def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserForm()

    return render(request, 'tasks.html', {'form': form})
'''


#class DetailView(generic.DetailView):
 #   model = Tasks
  #  template_name = 'tasks/tasks.html'
   # context_object_name = 'all_notes'

    #def get_queryset(self):
     #   return Tasks.objects.filter(create_date__lte=datetime.today())



'''
class UserFormView(View):
    form_class = UserForm
    template_name = 'tasks/login.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, 'tasks/login.html')

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('tasks/index.html')

        return render(request, self.template_name, 'tasks/login.html') '''


