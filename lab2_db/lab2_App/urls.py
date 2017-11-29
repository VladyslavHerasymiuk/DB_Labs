from django.conf.urls import url

from lab2_App import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'insert/$', views.insert, name='insert'),
    url(r'insert_admin/$', views.insert_admin, name='insert_admin'),
    url(r'insert_post/$', views.insert_post, name='insert_post'),
    url(r'admin_add/$', views.post_admin_add, name='admin_add'),
    url(r'admin_del/$', views.post_admin_del, name='admin_del'),
    url(r'admin_edit/$', views.post_admin_edit, name='admin_edit'),
    url(r'admin_search_range/$', views.post_admin_search, name='admin_search_range'),
    url(r'admin_update/$', views.admin_update, name='admin_update'),
    url(r'search_word/$', views.search_word, name='search_word'),
    url(r'search_string/$', views.search_string, name='search_string'),
    url(r'xml_dump/$', views.xml_dump, name='dump')
]