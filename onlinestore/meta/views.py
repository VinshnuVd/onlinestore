from django.conf import settings

from rest_framework import views, status
from rest_framework import views
from rest_framework.response import Response

from meta.models import MetaData,Location,Department, Category, SubCategory
from meta.serializers import LocationSerializer, DepartmentSerializer, CategorySerializer, SubCategorySerializer
# Create your views here.

from onlinestore.util import response_writer



class LocationsList(views.APIView):
	http_method_names = ['get']
	
	def get_queryset(self):
		return Location.objects.filter(is_deleted=False)
		
	def get(self, request):
		try:
			queryset = self.get_queryset()
			locations = LocationSerializer(queryset, many=True)
			return Response(response_writer(data=locations.data),status=status.HTTP_200_OK)
		except Exception as error:
			print(error)
			return Response(response_writer(status=500,error=settings.INTERNAL_SERVER_ERROR),status=status.HTTP_500_INTERNAL_SERVER_ERROR)
		


class DepartmentsList(views.APIView):
	http_method_names = ['get']
	
	def get_queryset(self):
		location_id = self.kwargs['location_id']
		return Department.objects.filter(is_deleted=False,meta_departments__location_id=location_id).distinct()
		
	def get(self, request, location_id):
		try: 
			queryset = self.get_queryset()
			print(queryset.query)
			locations = DepartmentSerializer(queryset, many=True)
			return Response(response_writer(data=locations.data),status=status.HTTP_200_OK)
		except Exception as error:
			print(error)
			return Response(response_writer(status=500,error=settings.INTERNAL_SERVER_ERROR),status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class CategoryList(views.APIView):
	http_method_names = ['get']
	
	def get_queryset(self):
		return Category.objects.filter(
												is_deleted=False,
												meta_categories__location_id=self.kwargs['location_id'],
												meta_categories__department=self.kwargs['department_id'],
												).distinct()
		
	def get(self, request, location_id, department_id):
		try: 
			queryset = self.get_queryset()
			print(queryset.query)
			locations = CategorySerializer(queryset, many=True)
			return Response(response_writer(data=locations.data),status=status.HTTP_200_OK)
		except Exception as error:
			print(error)
			return Response(response_writer(status=500,error=settings.INTERNAL_SERVER_ERROR),status=status.HTTP_500_INTERNAL_SERVER_ERROR)
		

class SubCategoryList(views.APIView):
	http_method_names = ['get']
	
	def get_queryset(self):
		return SubCategory.objects.filter(
												is_deleted=False,
												meta_subcategories__location_id=self.kwargs['location_id'],
												meta_subcategories__department=self.kwargs['department_id'],
												meta_subcategories__category=self.kwargs['category_id'],
												).distinct()
		
	def get(self, request, location_id, department_id, category_id):
		try: 
			queryset = self.get_queryset()
			print(queryset.query)
			locations = SubCategorySerializer(queryset, many=True)
			return Response(response_writer(data=locations.data),status=status.HTTP_200_OK)
		except Exception as error:
			print(error)
			return Response(response_writer(status=500,error=settings.INTERNAL_SERVER_ERROR),status=status.HTTP_500_INTERNAL_SERVER_ERROR)