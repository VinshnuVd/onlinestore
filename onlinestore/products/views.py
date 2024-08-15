import logging
from django.conf import settings

from rest_framework import views, status
from rest_framework.exceptions import ParseError
from rest_framework.response import Response

from meta.models import MetaData

from onlinestore.util import response_writer

from products.models import Product
from products.serializers import ProductSerializer


class ProductsList(views.APIView):
	http_method_names = ['post']
	
	def get_queryset(self):
		# Read Payload from POST BODY
		payload = self.request.data
		location = payload.get('location')
		department = payload.get('department')
		category = payload.get('category')
		subcategory = payload.get('subcategory')
		
		meta_data = MetaData.objects.filter()
		
		# Fetch MetaData ids based on payload filters
		if isinstance(location,str):
			meta_data = meta_data.filter(location__name__iexact=location)
		if isinstance(department,str):
			meta_data = meta_data.filter(department__name__iexact=department)
		if isinstance(category,str):
			meta_data = meta_data.filter(category__name__iexact=category)
		if isinstance(subcategory,str):
			meta_data = meta_data.filter(sub_category__name__iexact=subcategory)
			
		queryset = Product.objects.filter(meta__in=meta_data).select_related('meta')
		
		return queryset
	
	def post(self,request):
		try:
			queryset = self.get_queryset()
			products = ProductSerializer(queryset, many=True)
			return Response(response_writer(data=products.data),status=status.HTTP_200_OK)
		except ParseError:
			return Response(response_writer(status=400,error=settings.INVALID_JSON_PAYLOAD),status=status.HTTP_400_BAD_REQUEST)
		except Exception as error:
			print("Exception in ProductsList error: ",str(error))
			return Response(response_writer(status=500,error=settings.INTERNAL_SERVER_ERROR),status=status.HTTP_500_INTERNAL_SERVER_ERROR)
		