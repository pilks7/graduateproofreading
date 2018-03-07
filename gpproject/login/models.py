from django.db import models

# Create your models here.
class User(models.Model):

	 username = models.CharField(max_length=150, help_text="Enter Your User Name Here")

	 password = models.CharField(max_length=400, help_text="Enter Your Password Here")