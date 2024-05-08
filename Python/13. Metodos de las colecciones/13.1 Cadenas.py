# Cadenas

"Hola Mundo".upper()
#Todas las letras en mayuscula.

"Hola Mundo".lower()
#Todas las letras en miniscula.

"hola mundo".capitalize()
#Primera letra en mayuscula.

"hola mundo".title()
#Todas las palabras que forman la frase tuvieran la primera letra en mayuscula.

"Hola mundo".count('o')
#Cuantas veces aparece la letra o.

"Hola mundo".find('mundo')
#Indica el Indice donde empieza la palabra mundo.

"Hola mundo mundo mundo".rfind('mundo')
#Indica que el indice de la última aparición de la palabra mundo dentro de la cadena.

c = "100"
c.isdigit()
#Comprobar que todos los caracteres son números.

c2 = "ABC100de"
c2.isalnum()
#Comprobar que son caracteres del alfabeto.

c2.isalpha()
#Comprobar que son caracteres alfabeticos.

"Hola mundo".isalpha()
#False: Caracter espacio no cuenta como alfabetico.

"Hola mundo".islower()
#Si todo es miniscula

"Hola mundo".isupper()
#Si todo es mayuscula

"Hola Mundo".istitle()
#Si es título

"    ".isspace()
#Si todo es espacio

"Hola mundo".startswith("H")
#Comienza con H

"Hola mundo".endswith('o')
#Termina con o

"Hola mundo mundo".split()
#Método que permite separar una cadena a partir de los espacios:

"Hola mundo mundo".split()[0]
#Nos entrega la separacion del primer indice.

"Hola,mundo,mundo,mundo,otra,palabra".split(',')
#Separa palabras por ,

",".join("Hola mundo")
#Separe todos los caracteres de una cadena por ,

" ".join("Hola")
#Nos separa cada caracter por espacio.

"    Hola mundo    ".strip()
#Permite borrar los espacios del inicio y final.

"---Hola mundo---".strip('-')
#Permite borrar los guiones de inicio y final.

"Hola mundo".replace('o','0')
#Cambia o por 0.

"Hola mundo mundo mundo mundo mundo".replace('mundo','',3)
#Reemplaza mundo por espacio
