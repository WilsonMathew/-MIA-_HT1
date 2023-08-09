import pickle

#Structs/classes
class Profesor:
    def __init__(self, Tipo, Id_profesor, CUI, Nombre, Curso):
        self.Tipo           = Tipo
        self. Id_profesor   = Id_profesor
        self.CUI            = CUI
        self.Nombre         = Nombre
        self.Curso          = Curso
    
    def __repr__(self) -> str:
        return f"Profesor ({self.Tipo} , {self.Id_profesor} , {self.CUI} , {self.Nombre} , {self.Curso}) \n"

class Estudiante:
    def __init__(self, Tipo, Id_estudiante, CUI, Nombre, Carnet):
        self.Tipo           = Tipo 
        self.Id_estudiante  = Id_estudiante
        self.CUI            = CUI
        self.Nombre         = Nombre 
        self.Carnet         = Carnet

    def __repr__(self) -> str:
        return f"Estudiante ({self.Tipo} , {self.Id_estudiante} , {self.CUI} , {self.Nombre}  , {self.Carnet}) \n"

file_name = r"binarytext.bin"
file_object = open(file_name, "ab")


#Menu
def print_menu():
    print("- Gaspar Wilson Laynez Mateo - ")
    print("--------- 201602755 ---------")
    print("----------- USAC -----------")
    print("1. Registro de profesor")
    print("2. Registro de estudiante")
    print("3. Ver registros")
    print("4. Salir")
    print("----------------------------")

# Leer el archivo binario
def read_binary():
    #leer archivo
    file_name = r"binarytext.bin"
    file_object = open(file_name, "rb")
    content = file_object.read()
    text_content = content.decode("utf-8")

    print("Content: \n", text_content)
    file_object.close()
    # leer archivo

# Registrar profesor
def register_profesor():
    print("--- Registrando profesor --- \n")
    file_object = open(file_name, "ab")

    new_tipo    = input("Ingrese tipo: ")
    new_id      = input("Ingrese id: ")
    new_CUI     = input("Ingrese CUI: ")
    new_nombre  = input("Ingrese Nombre: ")
    new_curso   = input("Ingrese Curso: ")
    new_profesor = Profesor(new_tipo, new_id, new_CUI, new_nombre, new_curso)
    #lista_profesores.append(new_profesor)
    file_object.write(str(new_profesor).encode("utf-8"))

    file_object.close()

# Registrar profesor
def register_estudiante():
    print("--- Registrando estudiante ---")
    file_object = open(file_name, "ab")


    new_tipo_e      = input("Ingrese tipo: ")
    new_id_e        = input("Ingrese id: ")
    new_CUI_e       = input("Ingrese CUI: ")
    new_nombre_e    = input("Ingrese nombre: ")
    new_carnet_e    = input("Ingrese carnet: ")
    new_estudiante  = Estudiante(new_tipo_e, new_id_e, new_CUI_e, new_nombre_e, new_carnet_e)
    file_object.write(str(new_estudiante).encode("utf-8"))
    file_object.close()

option = ""

while option != "4":

    print_menu()
    option = input("Seleccionar opcion >> ")

    if option == "1":
        register_profesor()
    elif option == "2":
        register_estudiante()
    elif option == "3":
        read_binary()
    elif option == "4":
        file_object.close()
        print("--- Hasta luego! :) ---  \n")
    else:
        print ("Opcion invalida")