from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.db.models import Avg
# from django.contrib.auth import logout
from django.views.generic import (
  ListView,
  DetailView,
  CreateView,
  DeleteView,
  UpdateView,
  TemplateView
  )
# Create your views here.


class TempIphoneView(TemplateView):
  template_name = 'iphone/index.html'

