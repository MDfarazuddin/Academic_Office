from django.db import models

# Create your models here.
class Admins(models.Model):
	A_id = models.CharField(max_length = 3)
	A_name = models.CharField(max_length = 20)
	A_password=models.CharField(max_length=50)
	def __str__(self):
		return self.A_name
