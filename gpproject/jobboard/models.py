from django.db import models
from datetime import datetime
from datetime import timedelta


# Create your models here.

def get_deadline():
    return datetime.today() + timedelta(days=3)

class JobPost(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    deadline = models.DateField(default=get_deadline)    
    wordcount = models.IntegerField()
    jobtaken = models.BooleanField(default=False)
    # client = models.User.username  
     
    class Meta:
        ordering = ["-created_at"]  

    def publish(self):
        self.published_date = timezone.now()
        self.save()




    def __str__(self):
        return "Job #{}".format(self.pk)


