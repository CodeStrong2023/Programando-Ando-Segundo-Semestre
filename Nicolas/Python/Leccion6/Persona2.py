
class Persona2:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalles(self):
        print(f"Los datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad}")
        
    @property # decorador
    def nombre(self):  #Metodo Getter
        print("estamos usando el metodo get")
        return self._nombre
        
    @nombre.setter
    def nombre(self, nombre): # Metodo Setter
        print("estamos usando el metodo set")
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido
        
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido
        
    @property
    def edad(self):
        return self._edad
        
    @edad.setter
    def edad(self, edad):
        self._edad = edad
    
    def __del__(self):
        print(f"Persona: {self._nombre} {self._apellido} {self._edad}")
if __name__ == "__main__":   
    persona1 = Persona2("Nicolas", "Sini" , 23)     
    print(persona1.nombre) # Llamamos al metodo getter 
    persona1.nombre = "Nicolas" # Llamamos al metodo setter
    print(persona1.nombre) # Otra vez como el metodo getter
    print(persona1.mostrar_detalles()) # Llamamos al metodo mostrar detalles
    print(persona1.edad)

    # Tarea crear dos objetos mas, utilizando los metodos getter and setter
    # para modificar y mostrar los cambios con el metodo mostrar_detalles

    persona2 = Persona2("Sabrina", "Gutierrez", 24)
    persona2.nombre = "Sabrina"
    persona2.apellido = "Gutierrez"
    persona2.edad = "24"
    print(f"Imprimimos datos con metodo mostrar_detalles {persona2.mostrar_detalles()}")
    print(persona2.nombre)
    print(persona2.apellido)
    print(persona2.edad) 

    persona3 = Persona2("Lionel", "Messi", 36)
    persona3.nombre = "Lionel"
    persona3.apellido = "Messi"
    persona3.edad = 36
    print("Llamamos metodo mostrar_detalles: ")
    print(persona3.mostrar_detalles())
    print("Utilizamos getters and setters para imprimir atributos modificados")
    print(f"Nombre {persona3.nombre}")
    print(f"Apellido: {persona3.apellido}")
    print(f"Edad: {persona3.edad}")

    print(__name__)

     