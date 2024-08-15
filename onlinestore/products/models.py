from django.db import models
from django.db.models.functions import Upper
from meta.models import MetaData

# Create your models here.

class Product(models.Model):
	name = models.CharField(max_length=45)
	description = models.CharField(max_length=100)
	meta = models.ForeignKey(MetaData, on_delete=models.CASCADE)
	is_deleted = models.BooleanField(default=False)
	createdon = models.DateTimeField(auto_now_add=True)
	modifiedon = models.DateTimeField(auto_now=True)
	
	
	class Meta:
		db_table = 'PRODUCTS'
		constraints = [
            models.UniqueConstraint(Upper('name'), name='unique_upper_name_product')
        ]