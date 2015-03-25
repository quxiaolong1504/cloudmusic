from django.conf import settings
from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from account.views import UserRegView, AccountsView, AccountURLView
from api_map.views import get_api_root
from cmmedia.views import ResourceURLView, ImageView, ArtistViewSet, AlbumViewSet, MusicViewSet


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
                        url(r'^resources/$', ResourceURLView.as_view(), name="resources"),
                        url(r'resources/images/$', ImageView.as_view(), name="resource_image"),
                        url(r'^resources/albums/$',AlbumViewSet.as_view({'get':'list','post':'create'}), name="albums-list"),
                        url(r'^resources/albums/(?P<pk>\d+)/$',AlbumViewSet.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'}), name="albums-detail"),
                        url(r'^resources/artists/$',ArtistViewSet.as_view({'get':'list','post':'create'}), name="artists-list"),
                        url(r'^resources/artists/(?P<pk>\d+)/$',ArtistViewSet.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'}), name="artists-detail"),
                        url(r'^resources/musics/$',MusicViewSet.as_view({'get':'list','post':'create'}), name="musics-list"),
                        url(r'^resources/musics/(?P<pk>\d+)/$',MusicViewSet.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'}), name="musics-detail"),

)


urlpatterns += format_suffix_patterns(urlpatterns)


urlpatterns += patterns('', url(r'^$', get_api_root))



