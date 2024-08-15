from rest_framework import serializers
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
	location = serializers.CharField(source='meta.location.name', default=None)
	department = serializers.CharField(source='meta.department.name', default=None)
	category = serializers.CharField(source='meta.category.name', default=None)
	subcategory = serializers.CharField(source='meta.sub_category.name', default=None)
	
	class Meta:
		model = Product
		fields = ['id','name','description','location','department','category','subcategory','is_deleted']

	# If needed any modification in response structure we can make use of to_representation method
