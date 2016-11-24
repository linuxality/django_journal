from django.conf.urls import url
from . import views
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    url(r'^$', views.index),
    url(r'^([0-9])+/$', views.detail, name = 'detail'),
    url(r'^addevent/$', views.addevent, name = 'addevent'),
    url(r'^addevent/submitevent/$', views.submitevent, name  = 'submitevent'),
    url(r'^user/(\w+)/$', views.user_profile, name='user_profile'),
    url(r'^login/$', views.login_view, name='Login'),
    url(r'^logout/$', views.logout_view, name='Logout'),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve,
        {'document_root' : settings.MEDIA_ROOT,}),
    ]
