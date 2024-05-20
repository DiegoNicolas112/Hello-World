### Conjuntos

c = set()
c.add(1)
c.add(2)
c.add(3)
print(c)
#Permite agregar valores a este conjunto.

c.discard(1)
print(c)
#Permite quitar valores a este conjunto.

c.add(1)
c2 = c 
c2.add(4)
print(c)
#También se modifica c porque las colecciones están referencias en su dirección de memoria.

c2 = c.copy()
print(c2)
#Nos devuelve una copia de este contenedor.

c2.discard(4)
print(c2)
print(c)
#c2 elimina el 4 pero c se mantiene ya que c2 es una copia del contenedor.

c2.clear()
print(c2)
#Nos muestra set() que es un conjunto vacío ya que elimina todos los elementos.

# ---------- 3 Métodos: Nos permite saber 3 cosas -----
#1. Si un conjunto es disjunto, no hay ningún elemento en común entre 2 conjuntos.
#2. Si un conjunto es subconjunto, se encuentra completamente dentro de otro.
#3. Si es un conjunto contenedor de otro subconjunto.

c1 = {1,2,3}
c2 = {3,4,5}
c3 = {-1,99}
c4 = {1,2,3,4,5}

c1.isdisjoint(c3)
#Método 1: Es verdadero porque ningún elemento entre ellos.

c1.isdisjoint(c2)
#Método 2: Es Falso porque concuerdan algunos elementos.

c1.issubset(c4)
#Método 3: Es Verdadero porque también forma parte de el.

c4.issuperset(c1)
#Método 3: Es verdadero porque es un contenedor del primer conjunto.


"""Métodos Avanzados: Se utilizan para realizar uniones, diferencias entre otros """

c1.union(c2)
#Une 2 conjuntos.

c1.union(c2) == c4
#Verdadero la union de ambos conjuntos es c4.

c1.update(c2)
print(c1)
#c1 aparece unido con el conjunto c2.

c1 = {1,2,3}
c2 = {3,4,5}
c3 = {-1,99}
c4 = {1,2,3,4,5}

c1.difference(c2)
#Nos muestra los elementos distintos que tiene el conjunto 1 que no están en el conjunto 2.

c1.difference_update(c2)
c1
#Queda guardado en el conjunto c1 este resultado.

c1 = {1,2,3}
c2 = {3,4,5}
c3 = {-1,99}
c4 = {1,2,3,4,5}

c1.intersection(c2)
#La única intersección en ambos conjuntos.

c1.symmetric_difference(c2)
#Lo que es simetricamente diferente son todos los elementos que no concuerdan entre ambos conjuntos.