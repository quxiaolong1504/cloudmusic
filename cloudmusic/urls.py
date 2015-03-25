from django.conf import settings
from django.conf.urls import patterns, include, url
# from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from account.views import UserRegView, AccountsView, AccountURLView
from api_map.views import api_root, get_api_root
from cmmedia.views import ResourceURLView, ImageView
from utils.routers import MyRouter as DefaultRouter



urlpatterns = patterns('',
                       (r'^smedia/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)

urlpatterns += patterns('accounts',
                        url(r'^accounts/', include('rest_framework.urls', namespace='rest_framework')),
                        url(r'^accounts/$', AccountURLView.as_view(), name="accounts"),
                        url(r'^accounts/profile/$', AccountsView.as_view(), name='accounts-profile'),
                        url(r'^accounts/reg/$', UserRegView.as_view(), name='accounts-reg'),
)

urlpatterns += patterns('resources',
                        url('^resources/$', ResourceURLView.as_view(), name="resources"),
                        url('resources/images/$', ImageView.as_view(), name="resource_image")
)

urlpatterns += format_suffix_patterns(urlpatterns)


urlpatterns += patterns('', url(r'^', get_api_root))



