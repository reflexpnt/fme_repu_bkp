from django.contrib import admin
from .models import Articulo
from .models import Kit
from .models import KitB
from .models import KitC

#from django.contrib.auth.models import User
#from . import models
from import_export.admin import  ImportExportMixin




class KitCInline(admin.TabularInline):
    model = KitC
    extra = 0
    raw_id_fields = ("kitNumSAP_C",)
    #max_num = 10
	#extra = 0


#class ArticuloAdmin(admin.ModelAdmin ):
class ArticuloAdmin(ImportExportMixin, admin.ModelAdmin  ):

    #____  Los campos a mostrar en la version LISTA en ADmin____
    list_display = ('numeroParte', 'titulo',  'SYS_Prioridad','SYS_ESTADO','SYS_dataEntryAuthor','SYS_RevisedByAuthor','SYS_ApprovedByAuthor' , 'SYS_lastModif_date')

    ordering = ('-SYS_Prioridad','-SYS_local','numeroParte',) # The negative sign indicate descendent order
    search_fields = ('numeroParte', 'titulo',  )
    list_filter = ('SYS_ESTADO','SYS_Prioridad','KIT','SYS_local','SYS_EsActivo', 'SYS_EsVisible', 'SYS_locked')


    inlines = [
        KitCInline,
    ]


    """
    # como se mostraran los campos en la edicion (ADMIN) - los campos entre parentesis se muestran en horizontal
    fields = ['numeroParte', ('titulo','unidad'),('SYS_local','SYS_EsActivo','SYS_EsVisible','SYS_locked','SYS_EsOBSOLETO'),('SYS_Prioridad','SYS_ESTADO'),('SYS_lastESTADO', 'SYS_lastModif_date'), \
              ('SYS_dataEntryAuthor','SYS_RevisedByAuthor','SYS_ApprovedByAuthor'),('SYS_Approver_Notes','SYS_Reviser_Notes'), \
              'Descripcion','imagen_Pri_Nombre','imagen_pri','marca','modelo_NumParte','linea','comentario',('Reemplazable','Fab_a_Pedido','Plano'),'Ensayos', \
              'Referencia1','Referencia2','Referencia3','Referencia4','Referencia5']
    """

    #Podemos configurarlas en diferentes secciones añadiendo sig texto  a nuestra clase
    #Cada sección tiene su propio título (o None, si no quieres un título) y una grupo de campos asociada en un diccionario
    fieldsets = (
        ('Sistema', {
            'fields': (('SYS_local','SYS_EsActivo','SYS_EsVisible','SYS_locked','SYS_EsOBSOLETO','KIT'),'SYS_Prioridad',('SYS_ESTADO','SYS_lastESTADO', 'SYS_lastModif_date'), \
              ('SYS_dataEntryAuthor','SYS_RevisedByAuthor','SYS_ApprovedByAuthor'),('SYS_Approver_Notes','SYS_Reviser_Notes'))
        }),
        ('Articulo Info', {
            'fields': ('numeroParte', ('titulo','unidad'),'Descripcion','imagen_Pri_Nombre','imagen_pri','marca','modelo_NumParte','linea','comentario',('Reemplazable','Fab_a_Pedido','Plano'),'Ensayos', \
              'Referencia1','Referencia2','Referencia3','Referencia4','Referencia5','partekit')
        }),
    )


    def view_homepage_link(self, obj):
        return '<a href="%s" target="_blank">%s</a>' % (obj.numeroParte, obj.numeroParte,)
    view_homepage_link.allow_tags = True
    view_homepage_link.short_description = 'numeroParte' # Optional




### =============================================================================================
admin.site.register(Articulo, ArticuloAdmin )
admin.site.register(Kit)
admin.site.register(KitB)
admin.site.register(KitC)
