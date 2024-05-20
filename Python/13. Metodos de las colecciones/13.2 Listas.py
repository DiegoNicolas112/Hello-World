lista = [1,2,3,4,5,6]
lista.append(7)
#Agrega el número 7 al final de la lista.

lista.clear()
lista
#Borra todos los elementos que forman la lista.

l1 = [1,2,3]
l2 = [4,5,6]
l1.extend(l2)
#Permite unir listas.

["Hola", "mundo", "mundo"].count("mundo")
#Cuenta cuantas veces aparece la palabra mundo en la lista.

["Hola", "mundo", "mundo"].index("Hola")
#Nos indica en el indice que aparece la palabra. Solo busca el primer elemento.

l = [1,2,3]
l.insert(0,0)
print(l)
#Permite añadir un elemento en una determinada posición indicando el indice.

l = [5,10,15,25]
l.insert(-1,20)
#Permite añadir un elemento en una determinada posición indicando el indice.

l = [5,10,15,25]
l.insert(20,9999)
print(l)
#Permite añadir un elemento en una determinada posición indicando el indice, si no hay mas valores lo agrega al final y se comporta como un append.

l = [10,20,30,40,50]
l.pop()
print(l)
#pop permite borrar el último elemento de la lista pero también podemos indicarlo con el indice.

l = [10,20,30,40,50]
l.remove(30)
print(l)
#Permite eliminar un elemento de la lista

l = [10,20,30,30,30,40,50]
l.remove(30)
print(l)
#Solo elimina un elemento y no todos los 30 que aparecen.

l.reverse()
print(l)
#reverse permite revertir la lista.No es posible en una cadena.

lista = list("Hola mundo")
print(lista)
lista.reverse()
print(lista)
#De esta forma podemos invertir una cadena dentro de la lista.

cadena = "".join(lista)
print(cadena)
#Una cadena volteada gracias a la conversión de una cadena a lista.

lista = [5,-10,35,0,-65,100]
lista.sort()
print(lista)
#Permite ordenar la lista de menor a mayor.

lista.sort(reverse=True)
print(lista)
#Permite ordenar la lista de mayor a menor.