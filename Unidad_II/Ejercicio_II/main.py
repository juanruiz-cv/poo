import csv
import viajerofrecuente as v

def pedirNumeroEntero():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
     
    return num

def buscarViajero(n,lista):
    bandera= False
    i=0
    while not bandera:
        if lista[i].__nro_viajero==n:
            bandera=True
    return lista[i]

#n=v.Viajero_frecuente()                 #Prueba

if __name__ == "main":
    lista=[]
    archivo=open("viajero_frecuente.csv")
    rea=csv.reader(archivo,delimiter=",")
    for fila in rea:
        lista.append(nuevo=v.Viajero_frecuente(fila[0],fila[1],fila[2],fila[3],fila[4]))
    

    salir = False
    opcion = 0
    
    nro_a_consultar=int(input("Ingrese número de viajero frecuente:"))
    viajero=buscarViajero(nro_a_consultar,lista)
    while not salir:
    
        print ("1.-Consultar cantidad de millas:")
        print ("2.-Acumular millas:")
        print ("3.-Canjear millas:")
        print ("4. Salir")
        
        print ("Elige una opcion")
    
        opcion = pedirNumeroEntero()
    
        if opcion == 1:
            millas=int(viajero.cantidadTotaldeMillas())
            print("Cantidad de millas acumuladas: {}".format(millas))
        elif opcion == 2:
            ac=int(input("Ingrese las millas a aumular:"))
            viajero.acumularMillas(ac)
        elif opcion == 3:
            can=int(input("Ingrese la cantidad de millas a canjear:"))
            viajero.canjearMillas(can)
        elif opcion == 4:
            salir = True
        else:
            print ("Introduce un numero entre 1 y 3")
    
    print ("Fin")

    archivo.close()