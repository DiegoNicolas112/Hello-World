# Herencias Multiples

class A:
    def __init__(self):
        print("Soy de clase A")

class B:
    def __init__(self):
        print("Soy de clase B")

class C(A,B):
    pass

c = C()
#Esto va a imprimir el mensaje = "Soy de clase A". Esto es porque le da prioridad a la clase que este al lado izquierdo (A,B).

#Ejemplo 2:
class A:
    def __init__(self):
        print("Soy de clase A")
    def a(self):
        print("Este método lo heredo de A")

class B:
    def __init__(self):
        print("Soy de clase B")
    def b(self):
        print("Este método lo heredo de B")  

class C(A,B):
    def c(self):
        print("Este método es de C")

c = C()
c.a()
c.b()
c.c()

#Podemos gestionar atributos y métodos heredados de varias clases a la vez.