"""
1) Plantear una clase que administre dos listas de 5 nombres de alumnos y sus notas. 
Mostrar un menú de optiones que permita:
1- Cargar alumnos.
2- Listar alumnos.
3- Mostrar alumnos con notas mayores o iguales a 7.
"""
class students:

    def __init__(self):
        self.names = []
        self.grades = []

    def menu(self):
            option = 0
            while option != 1 or option != 2 or option != 3:
                print('\nMain menu\n')
                print("1- Upload students")
                print("2- List of students")
                print("3- Students grades greater or equal to 7")
                
                option = int(input("Please, enter an option: "))
                
                if option == 1:
                    self.upload()
                elif option == 2:
                    self.list()
                elif option == 3:
                    self.high_grades()

    def upload(self):
            for x in range(5):
                name = input("\nEnter a student name: ")
                name = name.capitalize()
                self.names.append(name)
                grade = int(input("Student grade: "))
                self.grades.append(grade)

    def list(self):
        print("\nComplete list of students")
        for x in range(5):
            print(self.names[x],self.grades[x])           

    def high_grades(self):
        print("\nStudents with grades greater or equal to 7")
        for x in range(5):
            if self.grades[x] >= 7:
                print(self.names[x],self.grades[x])               

student1 = students()
student1.menu()


"""
2) Confeccionar una clase que administre una agenda personal. 
Se debe almacenar el nombre de la persona, teléfono y mail. 
Los métodos de la clase son: 
1- Carga de un contacto en la agenda. 
2- Listado completo de la agenda. 
3- Consulta ingresando el nombre de la persona. 
4- Modificación de su teléfono y mail. 
"""
class diary:

    def __init__(self):
        self.contact = {}

    def menu(self):
        option = 0
        while option != 1 or option != 2 or option != 3 or option != 4:
            print('\nMain menu\n')
            print("1- Register a contact")
            print("2- Complete list of contacts")
            print("3- Query by name")
            print("4- Change phone number and email")
            option = int(input("Please enter an option: "))
            if option == 1:
                self.load()
            elif option == 2:
                self.list()
            elif option == 3:
                self.query()
            elif option == 4:
                self.modification()

    def load(self):
        name = input("\nEnter a contact name: ")
        name  =  name.capitalize()
        phone = input("Enter the phone number: ")
        mail = input("Enter the email: ")
        self.contact[name] = (phone,mail)
        
    def list(self):       
        print("\nComplete list of contacts")
        for name in self.contact:
            print(f'Name: {name}\nPhone number: {self.contact[name][0]}\nE-mail: {self.contact[name][1]}')

    def query(self):      
        name = input("\nPlease, enter the name of the contact to consult: ")
        if name in self.contact:
            print(f'Name: {name}\nPhone number: {self.contact[name][0]}\nE-mail: {self.contact[name][1]}')
        else:
            print("-Contact not found-")         

    def modification(self):       
        name = input("\nPlease, enter the name of the contact to modify the phone and email: ")
        if name in self.contact:
            phone = input("Enter the new phone number: ")
            mail = input("Enter the new mail: ")
            mail =  mail.lower()
            self.contact[name] = (phone,mail)
        else:
            print("-Contact not found-")        
        
new_diary = diary()
new_diary.menu()


"""
3) Plantear una clase Club y otra clase Socio. 
La clase Socio debe tener los siguientes atributos: nombre y la antigüedad en el club (en años). 
En el método __init__ de la clase Socio pedir la carga por teclado del nombre y su antigüedad. 
La clase Club debe tener como atributos 3 objetos de la clase Socio. 
Definir un método para imprimir el nombre del socio con mayor antigüedad en el club. 
"""
class member:

    def __init__(self):
        self.name = input("\nPlease, enter the member name of the club: ")
        self.name = self.name.capitalize()
        self.seniority = int(input("Enter the seniority: "))
    
    def show_seniority(self):
        print(f'{self.name} is the oldest member with {self.seniority} years')
    
    def return_seniority(self):
        return self.seniority

class club:

    def __init__(self):
        self.member1 = member()
        self.member2 = member()
        self.member3 = member()
    
    def greater_seniority(self):
        print("\nSenior members: ")
        if (self.member1.return_seniority()>self.member2.return_seniority() and
            self.member1.return_seniority()>self.member3.return_seniority()):
            self.member1.show_seniority()
        else:
            if self.member2.return_seniority()>self.member3.return_seniority():
                self.member2.show_seniority()
            else:
                self.member3.show_seniority()

club1 = club()
club1.greater_seniority()






"""
4) Un banco tiene 3 clientes que pueden hacer depósitos y extracciones. También el banco requiere 
que al final del día calcule la cantidad de dinero que hay depositado. 
Lo primero que hacemos es identificar las clases: Podemos identificar la clase Cliente y la clase 
Banco. Luego debemos definir los atributos y los métodos de cada clase 
"""