from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

UNIT_CHOICES = (
    ('UN','UN'),
    (' M ', ' M '),
    ('KG ','KG '),
    ('LTS','LTS'),
)

PRIORITY_CHOICES = (
    ('5','5_Urgente'),
    ('4','4_Alta'),
    ('3','3_Media'),
    ('2','2_Normal'),
    ('1','1_Baja'),

)

STATUS_CHOICES = (
    ('Aprobado','Aprobado'),
    ('Revisado','Revisado'),
    ('enRevision','enRevisión'),
    ('enEdicion', 'en Edición'),
    ('Inicial','Inicial'),
   )


class Articulo(models.Model):
    SYS_local = models.BooleanField(  default=False)
    SYS_Prioridad = models.CharField(max_length=8, choices=PRIORITY_CHOICES, default='1')
    SYS_EsActivo = models.BooleanField(  default=True)
    SYS_EsVisible = models.BooleanField(   default=True)
    SYS_EsOBSOLETO = models.BooleanField(  default=False)   # ej ARA290151
    SYS_ESTADO = models.CharField(max_length=10, choices = STATUS_CHOICES, default='Inicial')
    SYS_lastESTADO = models.CharField(max_length=10, choices = STATUS_CHOICES, default='Inicial')
    SYS_dataEntryAuthor     = models.ForeignKey( User, related_name='data_entries',  blank=True, null=True , on_delete=models.PROTECT)
    SYS_RevisedByAuthor     = models.ForeignKey( User, related_name='revisers',  blank=True, null=True , on_delete=models.PROTECT)
    SYS_ApprovedByAuthor    = models.ForeignKey( User, related_name='approvers',  blank=True, null=True , on_delete=models.PROTECT)

    SYS_Approver_Notes = models.CharField(max_length=250, blank=True, default="")
    SYS_Reviser_Notes  = models.CharField(max_length=250, blank=True, default="")


    SYS_locked = models.BooleanField(blank=True,  default=False)
    SYS_lastModif_date = models.DateTimeField( default=timezone.now, blank=True, null=True)

    KIT = models.BooleanField(  default=False)

    ordering = ['SYS_Prioridad']
    numeroParte = models.CharField(max_length=15 , blank=False, default="ARA"  )
    titulo = models.CharField(max_length=250, blank=False, default="sin título" )
    unidad = models.CharField(max_length=4, choices=UNIT_CHOICES, default='UN')
    Descripcion = models.TextField(max_length=1500, blank=True,  default="") # incrementar cantidad



    imagen_Pri_Nombre = models.CharField(max_length=250, default='no_image.png', blank=True )
    imagen_pri = models.ImageField(upload_to = './pic_folder/', default = './no_image.png', blank=True)
    #image = models.ImageField(upload_to = 'pic_folder/', default = 'no_image.png')

    marca = models.CharField(max_length=50, blank=True, default="")
    modelo_NumParte = models.CharField(max_length=50, blank=True, default="")
    linea = models.CharField(max_length=50, blank=True, default="")
    comentario = models.CharField(max_length=50, blank=True, default="")

    Reemplazable = models.BooleanField(blank=True,  default=False)
    Fab_a_Pedido = models.BooleanField(blank=True,  default=False)
    Plano = models.BooleanField(blank=True,  default=False)

    Ensayos = models.TextField(max_length=500, blank=True, default="")

    Referencia1 = models.CharField(max_length=250, blank=True, default="")
    Referencia2 = models.CharField(max_length=250, blank=True, default="")
    Referencia3 = models.CharField(max_length=250, blank=True, default="")
    Referencia4 = models.CharField(max_length=250, blank=True, default="")
    Referencia5 = models.CharField(max_length=250, blank=True, default="")




    def __str__(self):
        return self.numeroParte
        #return [self.name.lower()]

"""
class Kit(models.Model):
    #kitNumeroParte = models.CharField(max_length=15 , blank=False, default=""  )
    parte = models.ForeignKey( Articulo, related_name='parteAsociada',  blank=True, null=True , on_delete=models.PROTECT)
    #parte = models.ForeignKey( Articulo)
    cantidad = models.PositiveSmallIntegerField(  default=0)

    #def __str__(self):
    #   return self.parte.numeroParte
    #   #return self.parte
"""
