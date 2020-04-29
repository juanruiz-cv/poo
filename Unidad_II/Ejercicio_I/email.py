class Email:
    __idCuenta = ""
    __dom = ""
    __tipoDom = ""
    __contr = ""

#   ---===CONSTRUCTOR===---

    def __init__ (self,idCuenta,dom,tipoDom,contr):
        self.__idCuenta = idCuenta
        self.__dom = dom
        self.__tipoDom = tipoDom
        self.__contr = contr

#   ---===METODOS GET Y SET===---

    def returnEmail(self):
