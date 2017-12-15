from django.conf.urls import url
from assignment import views
urlpatterns = [
    url(r'^$', views.index),

]