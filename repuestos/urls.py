from django.conf.urls import  include, url
from . import views
from repuestos.views import postsJson

urlpatterns = [
    url(r'^ajax_posts$', views.postsJson , name='ajax_posts'),
    url(r'^$', views.show, name='index'),
    url(r'^pdf/(?P<pdf_art_id>[0-9]+)/$', views.part_pdf, name='part_pdf'),
    #url(r'^(?P<pk>[0-9]+)/$', views.part_detail, name='part_detail'),
    url(r'^sapnum/(?P<numeroParte>[a-zA-Z0-9_]+)/$', views.ara_detail, name='ara_detail'),
    url(r'^revision/(?P<numeroParte>[a-zA-Z0-9_]+)/$', views.ara_revision, name='ara_revision'),
    url(r'^aprobacion/(?P<numeroParte>[a-zA-Z0-9_]+)/$', views.ara_aprobacion, name='ara_aprobacion'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^art/(?P<pk>[0-9]+)/edit/$', views.articulo_edit, name='articulo_edit'),
    url(r'^datatables', views.show, name='datatables'),
    url(r'^reporte/$', views.reporte, name='reporte'),
    url(r'^export/$', views.export, name='export'),
    url(r'^tinymce/', include('tinymce.urls')),

]


