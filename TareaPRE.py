   
#Usamos el mismo ejemplo de C# para python 
# Declaramos la primera variable empleado 
class Empleado:
    # Propiedades que describen al empleado 
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    # Mostramos la informacion y mandamos a imprimir la informacion del empleado 
    def mostrar_info(self):
        print(f"Empleado: {self.nombre}, Salario: ${self.salario}")

# Clase 2 copiamos lo mimso de la clase 1 de (empleado)
class Gerente(Empleado):
    # Constructor
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)  # Llama al constructor de la clase padre
        self.departamento = departamento

    # Declaramos el metodo de gerente 
    def mostrar_departamento(self):
        print(f"{self.nombre} es gerente del departamento de {self.departamento}.")

# Aqui corremos el codigo para poder ver el resultado  
def main():
    # Creamos un objeto que es el empleado y le añadimos su salario 
    empleado = Empleado("Juan Pérez", 2100)
    empleado.mostrar_info()  # Llama al método de la clase1

    # Crear un objeto que seria el gerente y su salario 
    gerente = Gerente("Ana López", 7500, "Recursos Humanos")
    gerente.mostrar_info()  # Llama al método heredado de la clase1
    gerente.mostrar_departamento()  # Llama al método específico de la clase2

# Ejecutamos la función principal
if __name__ == "__main__":
    main()
