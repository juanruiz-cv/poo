class Viajero_frecuente:
    __nro_viajero=0
    __dni=""
    __nombre=""
    __apellido=""
    __millas=0

    def __init__ (self, nro=0,d="",n="",a="",m=0):
        self.__nro_viajero=nro
        self.__dni=d
        self.__nombre=n
        self.__apellido=a
        self.__millas=m

    def cantidadTotaldeMillas (self):
        return self.__millas

    def acumularMillas (self, m):
        self.__millas+=m
        print("Las millas fueron acumuladas.")

    def canjearMillas (self, m):
        if self.__millas>=m:
            self.__millas=self.__millas-m
            print("Millas canjeadas.")
        else:
            print("Millas insuficientes para canjear.")

    