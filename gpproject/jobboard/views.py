from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import staff_member_required
from .models import JobPost
fromdjango.utils import timezone
# Create your views here.

@staff_member_required()
class JobBoardView(TemplateView):
     template_name = "jobs.html"
     posts = JobPost.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

# def JobBoardView(request):
#     posts = JobPost.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#     return render(request, 'jobboard/jobs.html', {'posts': posts})