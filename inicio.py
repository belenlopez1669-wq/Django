# Inicializamos las variables
nombre = input("Ingrese su nombre: ... ")
apellido = input("Ingrese su apellido: ... ")
id_de_docente = input("Ingrese su ID de docente: ... ")

# Hacer que el número de teléfono/docente sea opcional
num_de_docente = input("Ingrese el número del docente (Presione ENTER para omitir): ... ")

# Si el usuario no escribió nada (dio ENTER), lo guardamos como None (el NULL de Python)
if num_de_docente == "":
    num_de_docente = None  

# Pedimos el correo obligatoriamente
correo = input("Ingrese su correo: ... ")

# Guardamos todo de forma limpia (por ejemplo, en un diccionario)
docente = {
    "nombre": nombre,
    "apellido": apellido,
    "id_de_docente": id_de_docente,
    "telefono": num_de_docente,
    "correo": correo
}