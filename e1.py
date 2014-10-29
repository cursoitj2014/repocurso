class Student(object):

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hola(self):
        return self.nombre

    def esMayor(self):
        if self.edad <= 10:
            return True
        else:
            return False


def main():
    e = Student("Benito Contreras", 4)
    print e.hola()
    print e.esMayor()


if __name__ == "__main__":
    main()