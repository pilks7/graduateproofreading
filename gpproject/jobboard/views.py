from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import staff_member_required
from .models import JobPost
from django.utils import timezone
# Create your views here.

# @staff_member_required()
# class JobBoardView(TemplateView):
#      template_name = "jobs.html"
#      posts = JobPost.objects.filter(published_date__lte=timezone.now()).order_by('pub_date')

#changed published_date to pub_date in .models
def jobs(request):
    #posts = JobPost.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    
    latest_post_list = JobPost.objects.order_by('-pub_date')
    context: {
        'posts': posts, 
        'deadline': deadline,
        'created_at': created_at, 
        'wordcount':wordcount, 
        'jobtaken':jobtaken
    }
    return render(request, 'jobboard/jobs.html', context=context)

