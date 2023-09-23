from crear_usuario import Crear_Usuario
from crear_bar import Bar
from crear_carrito import Crear_Carrito

usuario1 = Crear_Usuario("Sebas","Garcia",20,"1000192834")
usuario1.Usuario_Crear()
usuario1.Usuario_creado()
usuario1 = Crear_Carrito("Sebas")
usuario1 = Bar()
usuario1.agregar_bebida("Guaro",25000)
usuario1.agregar_bebida("ron",100000)



usuario2 = Crear_Usuario("Oscar","Lopez",17,"1234592834")
usuario2.Usuario_Crear()
usuario2.Usuario_creado()