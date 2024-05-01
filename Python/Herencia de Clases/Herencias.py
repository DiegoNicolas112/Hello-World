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