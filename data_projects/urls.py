from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'data_projects.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^tweets', 'twitter_interpreter.views.tweets', name='tweets'),

    url(r'^admin/', include(admin.site.urls)),
)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)