### Diccionarios

colores = {"amarillo":"yellow","azul":"blue","verde":"green"}
colores['amarillo']

colores.get('negro','black')
#Devuelve el valor por defecto que es el segundo parametro.

'negro' in colores
#Falso: la clave no se encuentra dentro del diccionario.

'amarillo' in colores
#Verdadero: la clave se encuentra dentro del diccionario.

colores.keys()
#Nos devuelve las claves del diccionario.

colores.values()
#Nos devuelve los valores del diccionario.

colores.items()
#Devuelve una lista que contiene pequeñas tuplas en clave y valor.

for c in colores:
    print(colores[c])
#Solo mostramos los valores.

for c in colores.keys():
    print(c)
#Solo mostramos las claves.

for c in colores.items():
    print(c)
#Si queremos mostrar ambos utilizamos items.

for c,v in colores.items():
    print(c,v)
#Mostrar bajo clave y valor.

colores.pop('amarillo',"no se ha encontrado")
#Sacamos el valor amarillo y borramos clave y valor.

colores.pop('negro',"no se ha encontrado")
#Indica el valor "no se ha encontrado" porque el negro no se encuentra en colores.

colores.clear()
#Vacíamos los valores del diccionario.