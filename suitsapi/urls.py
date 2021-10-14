from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns = [
    url('^$',views.getAllQuotes),
    url(r'^(?P<id>[0-9]+)/$',views.getDelQuote),
    url(r'^addquote/$',views.addQuote),
    ]