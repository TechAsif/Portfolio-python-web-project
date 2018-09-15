from django.db import models

# Create your models here.

class  Blog(models.Model):
	"""This is our blog class"""
	title=models.CharField(max_length=200)
	pub_date=models.DateTimeField()
	body = models.TextField()
	image=models.ImageField(upload_to='images/')

	def summary(self):
		return self.body[:100]

	def pub_date_prety(self):
		return self.pub_date.strftime('%b %e %y')

	def __str__(self):
		return self.title

	