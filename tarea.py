# -*- coding: utf-8 -*-
__author__ = 'venomsoft'


class HomeWork(object):

    def dictionary(self):
        dic = {"user": "root", "password": "t3r354", "level": "administrator"}
        for i in dic:
            print "Del diccionario: %s" % dic[i]

    def list(self):
        lis = ["benito", "daniel", "laura", "gonzalo", "raul", "martin"]
        for i in lis:
            print "De la lista: %s" % i

    def tupl(self):
        lis = ("benito", "daniel", "laura", "gonzalo", "raul", "martin")
        for i in lis:
            print "Ahora en tupla: %s" % i

    def lisdic(self):
        lis = []
        elements = 10
        i = 0
        for n in range(elements):
            lis.append({"user_%s" % i: "root_%s" % i, "password_%s" % i: "t3r354_%s" % i, "level_%s" % i: "admin_%s" % i})
            i += 1

        for n in lis:
            print n

        print lis[0]['user_0']

    def detvocal(self, vocal):
        if vocal == "a" or vocal == "e" or vocal == "i" or vocal == "o" or vocal == "u":
            print "SUCCESSFUL! It's a vocal"
        else:
            print "Oops! It's not a vocal"

    def major(self, a, b):
        if a > b:
            print "El mayor es: %d" % a
        else:
            print "El mayor es: %d" % b

    def leng(self, str):
        print "La longitud de ésta cadena es: %d" % len(str)

    def sumlis(self):
        lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        print "La suma del vector es %d" % sum(lis)


def main():
    d = HomeWork()
    d.dictionary()
    d.list()
    d.tupl()
    d.lisdic()
    d.detvocal("g")
    d.major(12, 7)
    d.leng("Hola mundo")
    d.sumlis()

if __name__ == "__main__":
    main()