from django.conf.urls import url
from WebClient.views import *

app_name = "GitGood"
urlpatterns = [
    url(r'^$', website.views.index, name='index'),    
    url(r'^login$', website.views.login_user, name='login'),
    url(r'^logout$', website.views.user_logout, name='logout')    
]
