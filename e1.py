import urllib2


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

    def getweb(self):
        try:
            web = urllib2.urlopen("http://itjiquilpan.edu.mx/")
            print web.read()
            web.close()
        except urllib2.HTTPError, e:
            print e
        except urllib2.URLError as e:
            print e

    def cast(self):
        listing = [1, 2, 3, "hola"]
        tupla = (1, 2, 3)
        dictionary = {"key1": "Raul", "key2": "Juan", "key3": "Pedro"}

        for i in listing:
            print i

        for i in tupla:
            print i

        print dictionary['key1']


def main():
    e = Student("Benito Contreras", 4)
    print e.hola()
    print e.esMayor()
    e.getweb()
    e.cast()


if __name__ == "__main__":
    main()