from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
from django.http import HttpResponse, Http404

from .models import Course
from .forms import CourseForm
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView, ListView

class create(CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'courses/create.html'
    success_url = '/courses/course'

class delete(DeleteView):
    model = Course
    template_name = 'courses/delete.html'
    success_url = '/courses/course'

class update(UpdateView):
    model = Course
    form_class = CourseForm
    template_name = 'courses/update.html'
    success_url = '/courses/course'

class detailView(DetailView):
    model = Course
    template_name = 'courses/detailView.html'

class listView(ListView):
    model = Course
    template_name = 'courses/listView.html'
    paginate_by = 3

