from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from cmmedia.views import ImageViewSet


router = DefaultRouter()
router.register('images',ImageViewSet)


urlpatterns = patterns('',
    (r'^smedia/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)

urlpatterns += patterns('',
    url(r'^',include(router.urls,namespace='images')),
    url(r'^admin/', include(admin.site.urls)),
)
