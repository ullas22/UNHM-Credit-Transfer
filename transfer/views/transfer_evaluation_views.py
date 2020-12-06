from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from ..models.model_transferevaluation import Transferevaluation
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.forms import ModelForm


class TransferevaluationForm(ModelForm):
    class Meta:
        model = Transferevaluation
        fields = ['course_id', 'major_req_id', 'sem_year_taken', 'expiration_date', 'approved_status', 'comment', 'approver_id']

def transfereval_list(request, template_name='transferevaluation_html/transfereval_home.html'):
    transfereval = Transferevaluation.objects.all()
    data = {}
    data['object_list'] = transfereval
    return render(request, template_name, data)

def transfereval_create(request, template_name='transferevaluation_html/transfereval_new.html'):
    form = TransferevaluationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('transfereval_home')
    return render(request, template_name, {'form':form})

def transfereval_detail(request, pk, template_name='transferevaluation_html/transfereval_detail.html'):
    transfereval = get_object_or_404(Transferevaluation, pk=pk)
    return render(request, template_name, {'object':transfereval})

def transfereval_update(request, pk, template_name='transferevaluation_html/transfereval_update.html'):
    transfereval= get_object_or_404(Transferevaluation, pk=pk)
    form = CourseForm(request.POST or None, instance=transfereval)
    if form.is_valid():
        form.save()
        return redirect('transfereval_home')
    return render(request, template_name, {'form':form})

def transfereval_delete(request, pk, template_name='transferevaluation_html/transfereval_delete.html'):
    transfereval = get_object_or_404(Transferevaluation, pk=pk)
    if request.method == 'POST':
        transfereval.delete()
        return redirect('transfereval_home')
    return render(request, template_name, {'object':transfereval})
