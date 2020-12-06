from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from ..models.model_major import Major
from django.urls import reverse_lazy
from django.forms import ModelForm

class MajorForm(ModelForm):
    class Meta:
        model = Major
        fields = ['major_id', 'major_name']


class MajorListView(ListView):
    # list view of the object of model Major
    model = Major
    template_name = 'major_html/major_home.html'

class MajorDetailView(DetailView):
    #detail view of all the object of model major
    model = Major
    template_name = 'major_html/major_detail.html'

class MajorCreateView(CreateView):
    # creates object in model Major
    model = Major
    template_name = 'major_html/major_new.html'
    fields = ['major_name']
    success_url = reverse_lazy('major_home')

def major_update(request, pk, template_name='major_html/major_update.html'):
    major= get_object_or_404(Major, pk=pk)
    form = MajorForm(request.POST or None, instance=major)
    if form.is_valid():
        form.save()
        return redirect('major_home')
    return render(request, template_name, {'form':form})

def major_delete(request, pk, template_name='major_html/major_delete.html'):
    major = get_object_or_404(Major, pk=pk)
    if request.method=='POST':
        major.delete()
        return redirect('major_home')
    return render(request, template_name, {'object':major})
