from django.shortcuts import render, get_object_or_404

# Create your views here.
# to import models: from .models import ...

def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    ###num_books=Book.objects.all().count()
    ###num_instances=BookInstance.objects.all().count()
    # Available books (status = 'a')
    ###num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    ###num_authors=Author.objects.count()  # The 'all()' is implied by default.
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={},
    )

def signup(request):
    return render(
        request,
        'signup.html',
        context={},
)

def jobs(request):
    return render(
        request,
        'jobs.html',
        context={},
)

def jobpost(request):
    return render(
        request,
        'jobs.html',
        context={},

)