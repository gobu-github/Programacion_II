# 1)Implementar una clase llamada Alumno que tenga como atributos su nombre y
# su nota. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar
# un mensaje si está regular (nota mayor o igual a 4)
# Definir dos objetos de la clase Alumno.

class alumno:
    def inicializar(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    def imprimir(self):
        print(f'El nombre del alumno es: {self.nombre}')
        print(f'Su nota es: {self.nota}')
    def esRegular(self):
        if self.nota >= 4:
            print('Es alumno regular')
        else:
            print('No es alumno regular')

print('\n')

alumno1 = alumno()
alumno1.inicializar('Carla', 9)
alumno1.imprimir()
alumno1.esRegular()

print('\n')

alumno2 = alumno()
alumno2.inicializar('Mauro', 3)
alumno2.imprimir()
alumno2.esRegular()



# 2) Confeccionar una clase que permita carga el nombre y la edad de una persona.
# Mostrar los datos cargados. Imprimir un mensaje si es mayor de edad (edad>=18)
# Definir dos objetos de la clase Persona.

class persona:
    def inicializar(self):
        self.nombre = input('Ingrese su nombre: ')
        self.nombre = self.nombre.capitalize()
        self.edad = int(input('ingrese su edad: '))
    def imprimir(self):
        print(f'\nSu nombre es: {self.nombre}')
        print(f'Su edad es de: {self.edad} años')
    def esMayor(self):
        if self.edad >= 18:
            print(f'\n{self.nombre}, usted es mayor de edad')
        else:
            print(f'\n{self.nombre}, usted es menor de edad')

print('\n')

persona1 = persona()
persona1.inicializar()
persona1.imprimir()
persona1.esMayor()


# 3) Confeccionar una clase que represente un empleado. Definir como atributos su
# nombre y su sueldo. En el método __init__ cargar los atributos por teclado y luego
# en otro método imprimir sus datos y por último uno que imprima un mensaje si debe
# pagar impuestos (si el sueldo supera a 3000)

class empleado:
    def __init__(self):
        self.nombre = input('Ingrese el nombre del empleado: ')
        self.nombre = self.nombre.capitalize()
        self.sueldo = float(input('Ingrese el sueldo del empleado: '))

    def imprimirDatos(self):
        print(f'\nSu nombre es: {self.nombre}')
        print(f'Su sueldo es de: ${self.sueldo}')

    def paga_impuestos(self):
        if self.sueldo > 3000:
            print(f'\n{self.nombre}, usted debe pagar impuestos')
        else:
            print(f'\n{self.nombre}, usted no debe pagar impuestos')

empleado1=empleado()
empleado1.imprimirDatos()
empleado1.paga_impuestos()


# 4) Implementar la clase Operaciones. Se deben cargar dos valores enteros por
# teclado en el método __init__, calcular su suma, resta, multiplicación y división, cada
# una en un método, imprimir dichos resultados.

class operaciones:
    def __init__(self):
        self.value1 = int(input('Ingrese un valor entero: '))
        self.value2 = int(input('Ingrese otro valor entero: '))
    
    def suma(self):
        suma = print(f'La suma de los valores es: {self.value1 + self.value2}')

    def resta(self):
        resta = print(f'La resta de los valores es: {self.value1 - self.value2}')
    
    def multiplicacion(self):
        multiplicacion = print(f'La multiplicacion de los valores es: {self.value1 * self.value2}')
    
    def division(self):
        division = print(f'La división de los valores es de: {self.value1 // self.value2}')
    
operacion1 = operaciones()
operacion1.suma()
operacion1.resta()
operacion1.multiplicacion()
operacion1.division()


