from rest_framework import serializers
from meta.models import Location, Department, Category, SubCategory, MetaData


class LocationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Location
		fields = ['id','name']


class DepartmentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Department
		fields = ['id','name']


class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = ['id','name']


class SubCategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = SubCategory
		fields = ['id','name']
		

class MetaDataSerializer(serializers.ModelSerializer):
	location = LocationSerializer()
	department = DepartmentSerializer()
	category = CategorySerializer()
	subcategory = SubCategorySerializer()
	
	class Meta:
		model = MetaData
		fields = ['id','location','department','category','subcategory']