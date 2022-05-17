#Ejercicio de Scripts
#El objetivo del script es descomponer el número en unidades,decenas,centenas y miles.
import sys

if len(sys.argv) == 2:
    numero = int(sys.argv[1])
    if numero < 0 or numero > 9999:
        print("Error - Número es incorrectos")
        print("Ejemplo: Descomposicion.py [0-9999]")
    else: 
        #Aquí va la lógica
        cadena = str(numero)
        longitud = len(cadena)

        for i in range(longitud):
            print("{:04}".format(int(cadena[longitud-1-i])* 10 ** i))


else: 
    print("Error - Argumentos incorrectos")
    print("Ejemplo: Descomposicion.py [0-9999]")