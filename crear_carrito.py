from crear_bar import Bar
from crear_usuario import Crear_Usuario
class Crear_Carrito:
    
    
     bebidas = None
     precios = None
     conjunto = []
    


     def __init__(self, Nombre:Crear_Usuario):
        self.Nombre = Nombre
        print("El usuario",self.Nombre, "tiene las siguientes bebidas añadidas al carrtito: ")

     def agregar_bebida(self, bebida,precio):
       self.conjunto.append(bebida)
       self.conjunto.append(precio)
       self.total=self.conjunto
       print (self.conjunto)



    

