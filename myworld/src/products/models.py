from django.db import models

# Create your models here.
class Product(models.Model):
	tag		 = models.TextField()
	report   = models.TextField()
	fare     = models.TextField()
	summary	 = models.TextField(default='this is summary, which is cool!')
