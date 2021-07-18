from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
from django.http import HttpResponse, Http404

from .models import Enrollment
from .forms import EnrollmentFrom
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView, ListView

class create(CreateView):
    model = Enrollment
    form_class = EnrollmentFrom
    template_name = 'enrollments/create.html'
    success_url = '/enrollments/enrollments'

class delete(DeleteView):
    model = Enrollment
    template_name = 'enrollments/delete.html'
    success_url = '/enrollments/enrollments'

class update(UpdateView):
    model = Enrollment
    form_class = EnrollmentFrom
    template_name = 'enrollments/update.html'
    success_url = '/enrollments/enrollments'

class detailView(DetailView):
    model = Enrollment
    template_name = 'enrollments/detailView.html'

class listView(ListView):
    model = Enrollment
    template_name = 'enrollments/listView.html'
    paginate_by = 3


