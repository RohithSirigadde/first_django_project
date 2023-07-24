from django.db import models

# Create your models here.
class Product(models.Model):
	tag		 = models.CharField(max_length=120) # max_length = required
	report   = models.TextField(blank=True,null=True)
	fare     = models.DecimalField(decimal_places=2,max_digits=10000)
	summary	 = models.TextField(blank=False, null=False)
	prominent= models.BooleanField(default=True) # null=True, default=True

 	def get_absolute_url(self):
        return reverse("products:product-detail", kwargs={"id": self.id}) #f"/products/{self.id}/"