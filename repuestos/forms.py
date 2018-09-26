from django import forms
from .models import Articulo


class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ( 'SYS_Prioridad','SYS_ESTADO','SYS_lastESTADO','SYS_lastModif_date' ,  'SYS_Reviser_Notes', 'Descripcion',  'imagen_pri' , 'marca' , 'modelo_NumParte', 'linea' , 'comentario' , 'Reemplazable' ,  'Fab_a_Pedido' , 'Plano' , 'Ensayos' , 'Referencia1', 'Referencia2', 'Referencia3', 'Referencia4', 'Referencia5'  )

        #fields['titulo'].widget.attrs['size'] = 2
