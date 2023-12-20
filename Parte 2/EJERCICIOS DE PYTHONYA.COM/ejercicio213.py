# Importamos el modufo de wxPython
import wx

# iniciamos la aplicacion
aplicacion = wx.App()
# Creamos una ventana con el nombre Hola Mundo
ventana = wx.Frame(parent=None,title="Hola Mundo")
# Mostramos la ventana
ventana.Show()
# Ejecuta el main
aplicacion.MainLoop()