from django.db import models
from django.db.models.functions import Upper


class Location(models.Model):
	name = models.CharField(max_length=45)
	is_deleted = models.BooleanField(default=False)
	createdon = models.DateTimeField(auto_now_add=True)
	modifiedon = models.DateTimeField(auto_now=True)
	
	class Meta:
		db_table = 'LOCATIONS'
		constraints = [
            models.UniqueConstraint(Upper('name'), name='unique_upper_name_location')
        ]
		

class Department(models.Model):
	name = models.CharField(max_length=45)
	is_deleted = models.BooleanField(default=False)
	createdon = models.DateTimeField(auto_now_add=True)
	modifiedon = models.DateTimeField(auto_now=True)
	
	class Meta:
		db_table = 'DEPARTMENTS'
		constraints = [
            models.UniqueConstraint(Upper('name'), name='unique_upper_name_department')
        ]
	

class Category(models.Model):
	name = models.CharField(max_length=45)
	is_deleted = models.BooleanField(default=False)
	createdon = models.DateTimeField(auto_now_add=True)
	modifiedon = models.DateTimeField(auto_now=True)
	
	class Meta:
		db_table = 'CATEGORY'
		constraints = [
            models.UniqueConstraint(Upper('name'), name='unique_upper_name_category')
        ]
	

class SubCategory(models.Model):
	name = models.CharField(max_length=45)
	is_deleted = models.BooleanField(default=False)
	createdon = models.DateTimeField(auto_now_add=True)
	modifiedon = models.DateTimeField(auto_now=True)
	
	class Meta:
		db_table = 'SUBCATEGORY'
		constraints = [
            models.UniqueConstraint(Upper('name'), name='unique_upper_name_subcategory')
        ]
		

class MetaData(models.Model):
	location = models.ForeignKey(Location,on_delete=models.CASCADE,related_name='meta_locations')
	department = models.ForeignKey(Department,on_delete=models.CASCADE,related_name='meta_departments')
	category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='meta_categories')
	sub_category = models.ForeignKey(SubCategory,on_delete=models.CASCADE,related_name='meta_subcategories')
	is_deleted = models.BooleanField(default=False)
	createdon = models.DateTimeField(auto_now_add=True)
	modifiedon = models.DateTimeField(auto_now=True)
	
	class Meta:
		db_table = 'META_DATA'
		unique_together = ('location', 'department', 'category', 'sub_category')