from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics.charts.barcharts import HorizontalBarChart
from reportlab.graphics.charts.legends import Legend
from reportlab.graphics.charts.piecharts import Pie
from reportlab.pdfbase.pdfmetrics import stringWidth, EmbeddedType1Face, registerTypeFace, Font, registerFont
from reportlab.graphics.shapes import  _DrawingEditorMixin, Rect
from reportlab.lib.colors import PCMYKColor
from django.shortcuts import render, get_object_or_404
from .models import Articulo

class MyBarChartDrawing(Drawing):
    def __init__(self, width=400, height=200, *args, **kw):
        Drawing.__init__(self,width,height,*args,**kw)
        self.add(HorizontalBarChart(), name='chart')

        self.add(String(200,180,'Hello World'), name='title')

        #set any shapes, fonts, colors you want here.  We'll just
        #set a title font and place the chart within the drawing
        self.chart.x = 20
        self.chart.y = 20
        self.chart.width = self.width - 20
        self.chart.height = self.height - 40

        self.title.fontName = 'Helvetica-Bold'
        self.title.fontSize = 12

        self.chart.data = [[100,157,200,235]]


if __name__=='__main__':
    #use the standard 'save' method to save barchart.gif, barchart.pdf etc
    #for quick feedback while working.
    MyBarChartDrawing().save(formats=['gif','png','jpg','pdf'],outDir='.',fnRoot='barchart')


class PieChart04(_DrawingEditorMixin,Drawing):
    '''
        Chart Features
        --------------

        This Pie chart itself is a simple chart with exploded slices:

        - **self.pie.slices.popout = 5**
    '''



    def __init__(self,width=600,height=308,*args,**kw):
        Drawing.__init__(self,width,height,*args,**kw)
        fontName = 'Helvetica'
        fontSize = 12

        articulos_inicial_state     = Articulo.objects.filter(SYS_local=1).filter(SYS_ESTADO="Inicial").count()
        articulos_enEdicion_state   = Articulo.objects.filter(SYS_local=1).filter(SYS_ESTADO="enEdicion").count()
        articulos_enRevision_state  = Articulo.objects.filter(SYS_local=1).filter(SYS_ESTADO="enRevision").count()
        articulos_Revisado_state    = Articulo.objects.filter(SYS_local=1).filter(SYS_ESTADO="Revisado").count()
        articulos_Aprobado_state    = Articulo.objects.filter(SYS_local=1).filter(SYS_ESTADO="Aprobado").count()



        self._add(self,Pie(),name='pie',validate=None,desc=None)
        self._add(self,Legend(),name='legend',validate=None,desc=None)
        self.pie.height = 252
        self.pie.sameRadii          = 1
        self.pie.direction          = 'clockwise'
        self.pie.startAngle         = 90
        self.background = Rect(0, 0, self.width, self.height, strokeColor=PCMYKColor(100,0,0,0), fillColor=PCMYKColor(15,0,0,0))
        self.background.strokeWidth = 0.25
        #self.pie.slices[0].fillColor             = PCMYKColor(0,0,0,100)
        colors = [ PCMYKColor(100,0,0,0), PCMYKColor(100,67,0,23), PCMYKColor(0,95,100,0), PCMYKColor(0,0,0,40), PCMYKColor(10,0,100,11)]
        for i, color in enumerate(colors): self.pie.slices[i].fillColor =  color
        #self.pie.slices.strokeColor      = PCMYKColor(0,0,0,0)
        #self.pie.slices.strokeWidth      = 0.5
        self.legend.y               = 101
        self.legend.fontSize        = fontSize
        self.legend.fontName        = fontName
        self.legend.dx              = 8
        self.legend.dy              = 8
        self.legend.yGap            = 0
        self.legend.deltay          = 16
        self.legend.strokeColor     = PCMYKColor(0,0,0,0)
        self.legend.strokeWidth     = 0
        self.legend.columnMaximum   = 6
        self.legend.alignment       ='right'
        # sample data
        #self.pie.data = [40.0, 20.0, 20.0, 14.0, 6.0]
        self.pie.data = [  articulos_inicial_state , articulos_enEdicion_state , articulos_enRevision_state, articulos_Revisado_state, articulos_Aprobado_state ]


        names = 'BP', 'Shell Transport & Trading', 'Liberty International', 'Persimmon', 'Royal Bank of Scotland',
        colorsList = PCMYKColor(100,0,0,0,alpha=100), PCMYKColor(0,42,88,0,alpha=100), PCMYKColor(0, 86, 0, 2,alpha=100), PCMYKColor(38, 86, 0, 2,alpha=100), PCMYKColor(98, 0, 96, 51,alpha=100),
        self.pie.slices[0].fillColor             = PCMYKColor(100,0,0,0,alpha=85)
        self.pie.slices[1].fillColor             = PCMYKColor(0,42,88,0,alpha=85)
        self.pie.slices[2].fillColor             = PCMYKColor(0, 86, 0, 2,alpha=85)
        self.pie.slices[3].fillColor             = PCMYKColor(38, 86, 0, 2,alpha=85)
        self.pie.slices[4].fillColor             = PCMYKColor(98, 0, 96, 51,alpha=85)
        self.background.fillColor        = None
        #self.legend.colorNamePairs = [(PCMYKColor(66,13,0,22,alpha=100), ('Inicial', str(articulos_inicial_state) )), (PCMYKColor(0,100,100,40,alpha=100), ( 'enEdicion', str(articulos_enEdicion_state)  )), (PCMYKColor(100,60,0,50,alpha=100), (  'enRevision', str(articulos_enRevision_state)  )), (PCMYKColor(23,51,0,4,alpha=100), ( 'Revisado', str(articulos_Revisado_state)   )), ( PCMYKColor(66,13,0,22,alpha=100), ( 'Aprobado', str(articulos_Aprobado_state)   ))]
        self.legend.colorNamePairs = [(PCMYKColor(100,0,0,0,alpha=100), ('Inicial', str(articulos_inicial_state) )), (PCMYKColor(0,42,88,0,alpha=100), ( 'enEdicion', str(articulos_enEdicion_state)  )), (PCMYKColor(0, 86, 0, 2,alpha=100), (  'enRevision', str(articulos_enRevision_state)  )), (PCMYKColor(38, 86, 0, 2,alpha=100), ( 'Revisado', str(articulos_Revisado_state)   )), ( PCMYKColor(98, 0, 96, 51,alpha=100), ( 'Aprobado', str(articulos_Aprobado_state)   ))]


        self.width       = 600
        self.height      = 300
        self.pie.width            = 150
        self.pie.x                = 25
        self.pie.y                = -25
        self.legend.x              = 225
        self.legend.subCols.rpad      = 12
        self.pie.slices.popout       = 6


if __name__=="__main__": #NORUNTESTS
    PieChart04().save(formats=['pdf'],outDir='.',fnRoot=None)
