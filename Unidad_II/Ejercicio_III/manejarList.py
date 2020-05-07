import csv
from camion import camion
class manejarList:
    __manejaList = []
    def __init(self):
        self.__manejaList = []

    def agregarList(self, unList):
        self.__manejaList.append(unList)

    def openArchi (self):
        archivo = open ('camiones.csv')
        reader = csv.reader(archivo, delimiter= ',')
        for row in reader:
            unList = camion(row[0],row[1],row[2],row[3],row[4])
            self.agregarList(unList)