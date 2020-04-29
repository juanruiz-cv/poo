# Ejercicio N° 4

# Métodos y Constructores con valores por defecto
# a- Defina una clase FechaHora que registre: día, mes, año, hora, minutos y segundos, en el formato de 24 horas.
# b- Implemente los métodos necesarios, para que pueda ejecutarse el Main que a continuación se propone.
# En los métodos y constructor que se utilizan para fijar una determinada hora en el reloj deberá comprobarse que la fecha y hora son válidas.
 
# if __name__ == '__main__':
#     d=int(input("Ingrese Dia: "))
#     mes=int(input("Ingrese Mes: "))
#     a=int(input("Ingrese Año: "))
#     h=int(input("Ingrese Hora: "))
#     m=int(input("Ingrese Minutos: "))
#     s=int(input("Ingrese Segundos: "))
#     r = FechaHora () #  inicilizar día, mes, año con 1/1/2020, y hora, minutos y 
#                               #  segundos con 0h, 0m, 0s.
#     r1 = FechaHora(d,mes,a); # inicializar con 0h 0m 0s
#     r2= FechaHora(d,mes,a,h, m, s)
#     r.Mostrar()
#     r1.Mostrar()
#     r2.Mostrar()
#     input()
#     r.PonerEnHora(5) # solamente la hora
#     r.Mostrar()
#     input()
#     r2.PonerEnHora(13,30) #hora y minutos
#     r2.Mostrar()
#     input()
#     r.PonerEnHora(14, 30, 25) #hora, minutos y segundos
#     r.Mostrar()
#     input()
#     r.AdelantarHora(3) #sumar 3 horas a la hora actual
#     r.Mostrar()
#     input()
#     r1.AdelantarHora(1,15) #sumar 1 hora y 15 minutos a la hora actual
#     r1.Mostrar()
#     input()

# Nota: tener en cuenta que 60 segundos suman 1 minuto; 60 minutos suman 1hora; 24 horas suman 1 día. Las operaciones que adelanten el reloj, deben controlar:

# a) Que la hora al llegar a 24, debe ponerse en 0 e incrementar un día.
# b) Al incrementar un día, puede cambiar el mes.
# c) Si el mes es diciembre, puede producirse el cambio de año.
# d) El programa debe validar la cantidad de días de cada año.
# e) El programa deberá validar años bisiestos (divisible por 4, y si es divisible por 100, debe ser divisible por 400), por ejemplo, 1900 es divisible por 4, pero no fue bisiesto porque no fue divisible por 400.

