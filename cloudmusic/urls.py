from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from account.views import UserRegView, AccountsView
from cmmedia.views import ImageViewSet


router = DefaultRouter()
router.register('images',ImageViewSet)


urlpatterns = patterns('',
    (r'^smedia/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)

urlpatterns += patterns('api-auth',
    url(r'^',include(router.urls,namespace='images')),

)
urlpatterns += patterns('account',

    url(r'^accounts/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^accounts/profile/$',AccountsView.as_view(),name='accounts-profile'),
    url(r'^accounts/reg/$', UserRegView.as_view(),name='user-reg'),
)



