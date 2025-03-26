#todo:Definimos la clase Carro
class Carro:
    #!Definimos un iniciador    
    def _init_(self, Nombre,Color,Precio):
        self.Nombre= Nombre
        self.Color= Color
        self.Precio=Precio
    #todo: Agregamos un metodo para mostrar los datos capturados
    def mostrar(self):
        print(f"El nombre del carro es {self.Nombre}")
        print(f"El color del carro es {self.Color}")
        print(f"Precio del carro es {self.Precio}")
#!Procedemos a imprimir y capturar datos con variables
print(f"Bienvenido, ingrese el nombre del carro: ")
Nombre=input();
print(f"Ingrese el color del carro")
Color=input();
print(f"Ingrese el precio del carro")
Precio=input();
#? Creamos un metodo con su captura 
Mi_Carro=Carro(Nombre,Color,Precio)
#! Mostramos el mensaje Final
Mi_Carro.mostrar()
