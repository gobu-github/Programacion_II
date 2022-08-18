"""
1) Plantear una clase que administre dos listas de 5 nombres de alumnos y sus notas. Mostrar un menú de opciones que permita:
1- Cargar alumnos.
2- Listar alumnos.
3- Mostrar alumnos con notas mayores o iguales a 7.
4- Finalizar programa.
"""

class students:

    def __init__(self):
        self.names = []
        self.grades = []

    def menu(self):
            option = 0
            while option != 4:
                print("1- Upload students")
                print("2- List students")
                print("3- Students grades greater or equal to 7")
                print("4- End program execution")
                
                option=int(input("Enter an option: "))
                
                if option==1:
                    self.upload()
                elif option==2:
                    self.list()
                elif option==3:
                    self.high_grades()

    def upload(self):
            for x in range(5):
                name=input("Enter a student name: ")
                self.names.append(name)
                grade=int(input("Student grade: "))
                self.grades.append(grade)

    def list(self):
        print("Complete list of students")
        for x in range(5):
            print(self.names[x],self.grades[x])
        print("_____________________")            

    def high_grades(self):
        print("Students with grades greater or equal to 7")
        for x in range(5):
            if self.grades[x]>=7:
                print(self.names[x],self.grades[x])
        print("_____________________")                


student1 = students()
student1.menu()



"""
2) Confeccionar una clase que administre una agenda personal. Se debe almacenar el nombre de la persona, teléfono y mail
Debe mostrar un menú con las siguientes opciones:
1- Carga de un contacto en la agenda.
2- Listado completo de la agenda.
3- Consulta ingresando el nombre de la persona.
4- Modificación de su teléfono y mail.
5- Finalizar programa.
"""




"""
3) Plantear una clase Club y otra clase Socio.
La clase Socio debe tener los siguientes atributos: nombre y la antigüedad en el club (en años).
En el método __init__ de la clase Socio pedir la carga por teclado del nombre y su antigüedad.
La clase Club debe tener como atributos 3 objetos de la clase Socio.
Definir una responsabilidad para imprimir el nombre del socio con mayor antigüedad en el club.
"""




"""
4) Un banco tiene 3 clientes que pueden hacer depósitos y extracciones. También el banco requiere
que al final del día calcule la cantidad de dinero que hay depositado.
Lo primero que hacemos es identificar las clases: Podemos identificar la clase Cliente y la clase
Banco. Luego debemos definir los atributos y los métodos de cada clase
"""