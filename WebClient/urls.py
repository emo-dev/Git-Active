from django.conf.urls import url
from django.contrib.auth import views as auth_views
import WebClient.views

app_name = "WebClient"
urlpatterns = [
    url(r'^login/$', WebClient.views.login_user, name='login'),
    url(r'^test_view/$', WebClient.views.test_view, name='test_view')
]
