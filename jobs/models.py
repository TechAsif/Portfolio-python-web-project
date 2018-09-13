from django.db import models

# Create your models here.

class  Job(models.Model):
	"""docstring for  Job"""
	image=models.ImageField(upload_to='images/')
	summery=models.CharField(max_length=200)

