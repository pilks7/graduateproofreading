from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
	# First/last name is not a global-friendly pattern
	name = models.CharField(blank=True, max_length=255)
	#email = 

	def __str__(self):
		return self.email