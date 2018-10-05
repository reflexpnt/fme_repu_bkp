from django import forms
from tinymce import TinyMCE
from .models import Articulo


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False

class ArticuloForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCEWidget(  attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )
    class Meta:
        model = Articulo
        fields = ( 'SYS_Prioridad','SYS_ESTADO','SYS_lastESTADO','SYS_lastModif_date' ,  'SYS_Reviser_Notes', 'Descripcion',  'imagen_pri' , 'marca' , 'modelo_NumParte', 'linea' , 'comentario' , 'Reemplazable' ,  'Fab_a_Pedido' , 'Plano' , 'Ensayos' , 'Referencia1', 'Referencia2', 'Referencia3', 'Referencia4', 'Referencia5' , 'content'  )
        #fields = '__all__'
        #fields['titulo'].widget.attrs['size'] = 2
