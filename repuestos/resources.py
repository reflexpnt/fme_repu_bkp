from import_export import resources
from .models import Articulo

class ArticuloResource(resources.ModelResource):
    class Meta:
        model = Articulo
        #fields = ('id','Year', 'Make', 'Model',)
        #export_order = ('id', 'price', 'author', 'name')
        #exclude = ('imported', )
        #https://django-import-export.readthedocs.io/en/latest/getting_started.html#creating-import-export-resource