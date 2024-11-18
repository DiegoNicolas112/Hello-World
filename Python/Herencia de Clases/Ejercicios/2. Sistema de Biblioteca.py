class Publicacion:
    def __init__(self, titulo, autor, año):
        self.titulo = titulo
        self.autor = autor
        self.año = año

    def __str__(self):
        return """
Titulo: {}
Autor: {}
Año: {}""".format(self.titulo, self.autor, self.año)

class Libro(Publicacion):
    def __init__(self, titulo, autor, año, genero):
        super().__init__(titulo, autor, año)
        self.genero = genero
    
    def __str__(self):
        return """
Titulo: {}
Autor: {}
Año: {}
Genero: {}""".format(self.titulo, self.autor, self.año, self.genero)

class Revista(Publicacion):
    def __init__(self, titulo, autor, año, numero):
        super().__init__(titulo, autor, año)
        self.numero = numero

    def __str__(self):
        return """
Titulo: {}
Autor: {}
Año: {}
Numero: {}""".format(self.titulo, self.autor, self.año, self.numero)
    
#Creando instancias
publicacion = Publicacion("El monje que vendió su Ferrari", "Robin Sharma", 1997)
libro = Libro("El principito", "Antoine de Saint-Exupéry", 1943, "Ficción")
revista = Revista("National Geographic", "Varios autores", 2024, 123)

print(publicacion)
print(libro)
print(revista)