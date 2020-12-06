from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.forms import ModelForm
from ..models.model_approver import Approver

def result(request, template_name='result.html'):
    schoolname = request.POST.get('schoolname')
    statename = request.POST.get('statename')
    return render(request, template_name, schoolname)
