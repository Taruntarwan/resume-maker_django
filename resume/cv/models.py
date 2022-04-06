from django.db import models
from django.contrib.auth.models import User


class Detal(models.Model):
	user = models.ForeignKey(User,on_delete = models.CASCADE)
	name = models.CharField(max_length =100)
	mobile = models.CharField(max_length =100)
	email = models.CharField(max_length =100)
	school = models.CharField(max_length =100)
	degree = models.CharField(max_length =100)
	skill = models.CharField(max_length =100)
	project = models.TextField(max_length =1000)
	previous_work = models.TextField(max_length =1000)
	certification = models.TextField(max_length =1000)
	about = models.TextField(max_length =1000)


