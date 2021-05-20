from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from apis.hr import views as hr_views
from apis.cmdb import views as cmdb_views
from apis.hr_action import employee as hr_action

router = routers.DefaultRouter()
router.register(r'hr_people_view_itd', hr_views.PeopleViewItdViewSet, basename='hr_people_view_itd')
router.register(r'hr_office', hr_views.PeopleOfficeViewSet, basename='hr_office')
router.register(r'hr_department', hr_views.PeopleDepartmentViewSet, basename='hr_department')
router.register(r'cmdb_host', cmdb_views.HostViewSet, basename='cmdb_host')

urlpatterns = [
    path('', include(router.urls)),
    path('docs/', include_docs_urls(title='docs')),
    path('hr_action/',hr_action),
]
