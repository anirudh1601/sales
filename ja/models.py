from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Sales(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
	identity = models.CharField(max_length=200)
	name = models.CharField(max_length=400)


	def __str__(self):
		return (self.identity)


class SalesForceModel(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	username = models.CharField(max_length=400)
	password=models.CharField(max_length=400)
	security_token=models.CharField(max_length=400)

	def __str__(self):
		return (self.username)
