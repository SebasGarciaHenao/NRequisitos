class Crear_Usuario:
    def __init__(self,Nombre: str,Apellido: str,Edad: int,Cedula:str):
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.Edad = Edad
        self.Cedula = Cedula
      

    def Usuario_Crear(self):
        
        if self.Edad >=18:
             print("El usuario se puede crear: ")
             print("El registro del usuario es: ",self.Nombre , self.Apellido,"y su cedula junto a su edad ",self.Cedula )

        else: print("El usuario ",self.Nombre,"No puede tener un registro ya que no cumple con la edad minima de 18 años")

    def Usuario_creado(self):
        if  self.Edad <18:
            return None
        
        else:  print("El usuario de nombre",self.Nombre, " y de apellido ",self.Apellido, "con numero de cedula",self.Cedula,"a sido creado")
     




