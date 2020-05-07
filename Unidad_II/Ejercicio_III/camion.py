class camion:
    __idCamion = 0
    __nombreConductor= ""
    __patenteCamion= ""
    __marcaCamion= ""
    __tara = 0

    def __init__(self,idCamion= 0, nombreConductor= "", patenteCamion= "", marcaCamion= "", tara= 0):
        self.__idCamion = idCamion
        self.__nombreConductor = nombreConductor
        self.__patenteCamion = patenteCamion
        self.__marcaCamion = marcaCamion
        self.__tara = tara
    