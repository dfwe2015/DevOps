from django.contrib.auth import authenticate,login
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView,FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from models import Group
from forms import GroupForm,HostForm,StorageForm

class ManagerGroupListView(LoginRequiredMixin,FormView):
    template_name= 'group.html'
    form_class=GroupForm

    def get_context_data(self, **kwargs):
        context= super(ManagerGroupListView, self).get_context_data(**kwargs)
        grouplist = Group.objects.all()

        context.update({'grouplist': grouplist,
                        })
        return context

    def get(self,request,*args, **kwargs):
        return super(ManagerGroupListView, self).get(request, *args, **kwargs)

class ManagerGroupModalView(LoginRequiredMixin,FormView):
    template_name = '_group_modal.html'
    form_class=GroupForm

    def get(self, request, *args, **kwargs):
        return super(ManagerGroupModalView, self).get(request, *args, **kwargs)

class ManagerHostListView(LoginRequiredMixin,FormView):
    template_name='host.html'
    form_class = HostForm

    def get_context_data(self, **kwargs):
        context= super(ManagerHostListView, self).get_context_data(**kwargs)
        grouplist = Group.objects.all()
        context.update({'grouplist': grouplist,
                        })
        return context

    def get(self,request,*args, **kwargs):
        return super(ManagerHostListView, self).get(request, *args, **kwargs)


class ManagerSearchListView(LoginRequiredMixin,TemplateView):
    template_name = 'search.html'

    def get(self, request, *args, **kwargs):
        return super(ManagerSearchListView,self).get(request,*args,**kwargs)

class ManagerStorageListView(LoginRequiredMixin,FormView):
    template_name = 'storage.html'
    form_class=StorageForm

    def get(self, request, *args, **kwargs):
        return super(ManagerStorageListView,self).get(request,*args,**kwargs)