#Clase
class Producto:
    def __init__(self, referencia, tipo, nombre, 
                 pvp,  descripcion, productor=None, 
                 distribuidor=None, isbn=None, autor=None):
        self.referencia = referencia
        self.tipo = tipo
        self.nombre = nombre
        self.pvp = pvp
        self.descripcion = descripcion
        self.productor = productor
        self.distribuidor = distribuidor
        self.isbn = isbn
        self.autor = autor

adorno = Producto('000A','ADORNO','Vaso Adornado',15,
                  'Vaso de porcelana con dibujos') 

print(adorno)
print(adorno.tipo) 

class Producto:
    def __init__(self, referencia, nombre, 
                 pvp,  descripcion):
        self.referencia = referencia
        self.nombre = nombre
        self.pvp = pvp
        self.descripcion = descripcion
        
    def __str__(self):
        return """
REFERENCIA:\t{}
NOMBRE:\t\t{}
PVP:\t\t{}
DESCRIPCIÓN:\t{}""".format(self.referencia,self.nombre,self.pvp,self.descripcion)

#Creamos una clase que sea hija de producto.

class Adorno(Producto):
    pass

a = Adorno(2034, "Vaso adornado",15,"Vaso de porcelana adornado con árboles")
print(a)

class Alimento(Producto):
    productor = ""
    distribuidor = ""

    def __str__(self):
        return """\
REFERENCIA:\t{}
NOMBRE:\t\t{}
PVP:\t\t{}
DESCRIPCIÓN:\t{}
PRODUCTOR:\t{}
DISTRIBUIDOR:\t{}""".format(self.referencia,self.nombre,self.pvp,self.descripcion,self.productor,self.distribuidor)

al = Alimento(2035, "Botella de Aceite",5,"250ml")
al.productor = "Belmonte"
al.distribuidor = "Distribuidor S.A"

print(al)

class Libro(Producto):
    isbn = ""
    autor = ""

    def __str__(self):
        return """\
REFERENCIA:\t{}
NOMBRE:\t\t{}
PVP:\t\t{}
DESCRIPCIÓN:\t{}
ISBN:\t\t{}
AUTOR:\t\t{}""".format(self.referencia,self.nombre,self.pvp,self.descripcion,self.isbn,self.autor)
    
l = Libro(2036,"El Club de las 5 am",10,"Liderazgo y Crecimiento Personal/Profesional")
l.isbn = "010101"
l.autor = "Robin Sharma"

print(l)

# Clases heredadas y polimorfismo
#Tengo una jerarquía de productos de la cual quiero trabajar con ellos de una forma cómoda.

#Para ello, debo tener los productos agrupados de alguna forma
productos = [a,al]
productos.append(l)
productos

#Para recorrer dentro de los productos
for p in productos:
    print(p,"\n")

#Para hacer referencias a los atributos de estos objetos
for p in productos:
    print(p.referencia,p.nombre)

#No es posible hacer referencias de un objeto si no cuenta con atributos, para ello vamos a identificar la subclase que tienen estos productos.
for p in productos:
    if( isinstance(p,Adorno) ):
        print(p.referencia,p.nombre)
    elif( isinstance(p,Alimento) ):
        print(p.referencia,p.nombre,p.productor)
    elif( isinstance(p,Libro) ):
        print(p.referencia,p.nombre,p.isbn)

#Es posible crear una función que permita modificar atributos de los productos
#Función: Rebajar el precio de un producto.
def rebajar_producto(p, rebaja):
    """Devuelve un producto con una rebaja en % de su precio """
    p.pvp = p.pvp - (p.pvp/100 * rebaja)
    return p

al_rebajado = rebajar_producto(al,10)
print(al_rebajado)
print(al)

#Al modificar la copia de un objeto, también se modifica el objeto original

copia_al = al
copia_al.referencia = 2038
print(copia_al)

#También aplica con las colecciones
l = [1,2,3]

#Para duplicar una lista, utilizar [:]
l2 = l[:]
l2.append(4)
l

#Si se requiere copiar un objeto se debe utilizar un módulo externo coppi
import copy

copia_a = copy.copy(a)
print(copia_a)

copia_a.pvp = 25
print(copia_a)

#Polimorfia: Propiedad de la herencia en que objetos de distintas subclases pueden responder una misma acción
#En python todas las clases son a su vez subclases de la superclase Object, es decir, son polimórficas por defecto.