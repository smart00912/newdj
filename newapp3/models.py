from django.db import models

# Create your models here.

class Auth(models.Model):
	uname = models.CharField(max_length=10)
	pwd = models.CharField(max_length=10)
	islogin = models.BooleanField(default=False)
	
	def __unicode__(self):
		return self.uname


