from django.conf.urls import url 
from Api import views 
 
urlpatterns = [ 
    url(r'^api/Api$', views.Api_list),                      # GET, POST, DELETE
    url(r'^api/Api/([0-9]+)$', views.Api_detail),           # GET, PUT, DELETE
    url(r'^api/Api/published$', views.Api_list_published)   # GET
]