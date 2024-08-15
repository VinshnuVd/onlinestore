from django.urls import path
from meta import views

urlpatterns = [
	path('locations/',views.LocationsList.as_view(), name='locations'),
	path('locations/<int:location_id>/departments/',views.DepartmentsList.as_view(), name='departments'),
	path('locations/<int:location_id>/departments/<int:department_id>/categories/',views.CategoryList.as_view(), name='categories'),
	path('locations/<int:location_id>/departments/<int:department_id>/categories/<int:category_id>/subcategories',views.SubCategoryList.as_view(), name='categories'),

]