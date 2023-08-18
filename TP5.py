'''1. Escriba una función redondear() que permita redondear un número decimal de acuerdo al criterio: Si el número es mayor a 3.50, devolver el entero siguiente (en este caso, 4), si no devolver el entero inmediatamente anterior (3).'''
# def redondear(data):
#     if data >3.50:
#         print(int(data)+1)
#     else:
#         print(int(data)-1)

# data=float(input("Ingrese un valor =  "))
# redondear(data)

'''2. Coloque el módulo del ejercicio anterior dentro de un paquete. En un módulo que esté fuera de ese paquete, cree una función de suma de decimales que redondee el resultado haciendo uso de la función redondear() del paquete recién creado.'''

# from libreria import redondear 

# def suma(numero1,numero2):
#     algebra=numero1+numero2
#     print(f"la suma es {redondear(algebra)}")

# numero1=float(input("Ingres un valor 1 = "))

# numero2=float(input("Ingres un valor 2 = "))

# suma(numero1,numero2)

'''3. Usando el módulo datetime, escribe un programa que muestre la fecha y hora actuales del sistema.'''

# from datetime import date
# hoy = date.today()
# print(f"Hoy es {hoy} ")

'''4. Escriba un programa que devuelva un número par al azar entre 2 y 10
(pista: para comprobar si se pueden generar todos los números, pruebe
ejecutar el programa dentro de un ciclo infinito).'''
# import random

# def randonn():
#    while True: 
#     numero = random.randrange(2, 12, 2) 
#     print(f"Número par es: {numero}")
# randonn()

'''5. Bola mágica: La bola mágica (Magic 8 ball) es un popular juguete usado para la adivinación o para buscar consejo. Su mecanismo es muy simple: ante una pregunta del usuario, la bola responde con una de 8 posibles respuestas:
- Es seguro que sí
- Las chances son buenas
- Puedes contar con ello
- Pregúntame de nuevo más tarde
- Concéntrate y pregunta de nuevo
- No veo con claridad, intenta de nuevo
- Mi respuesta es no
- Mis fuentes me dicen que no
Escriba una función en Python para simular la bola mágica.'''

# import random

# def randonn():
#     numero = random.randrange(1, 7, 1) 
#     print(f"Número seleccionado es: {numero}")

#     def Consulta(numero):
#             if numero == 1: 
#                 print("Es seguro que sí")
#             elif numero == 2:
#                 print("Las chances son buenas")
#             elif numero == 3:
#                 print("Puedes contar con ello")
#             elif numero == 4:
#                 print("Pregúntame de nuevo más tarde")
#             elif numero == 5:
#                 print("Concéntrate y pregunta de nuevo")
#             elif numero == 6:
#                 print("Mi respuesta es no")
#             elif numero == 7:
#                 print("Mis fuentes me dicen que no")
#             else:
#                 print("Opción no válida.")
#     Consulta(numero)
# randonn()

'''6. Encuentre el tiempo de ejecución de los programas de los ejercicios anteriores (pista: use el módulo time)'''
# import random
# import time

# def randonn():
#     numero = random.randrange(1, 7, 1) 
#     print(f"Número seleccionado es: {numero}")

#     def Consulta(numero):
#             if numero == 1: 
#                 print("Es seguro que sí")
#             elif numero == 2:
#                 print("Las chances son buenas")
#             elif numero == 3:
#                 print("Puedes contar con ello")
#             elif numero == 4:
#                 print("Pregúntame de nuevo más tarde")
#             elif numero == 5:
#                 print("Concéntrate y pregunta de nuevo")
#             elif numero == 6:
#                 print("Mi respuesta es no")
#             elif numero == 7:
#                 print("Mis fuentes me dicen que no")
#             else:
#                 print("Opción no válida.")
#     Consulta(numero)

# start_time = time.time()
# randonn()
# print(f"Tiempo de ejecucuion = {start_time}")

'''8. (Opcional) Escriba una función que pida al usuario ingresar su fecha de nacimiento y sea capaz de devolver la cantidad de días desde su nacimiento hasta hoy.'''
# from datetime import datetime

# def CantidadDias():
#     fecha_nacimiento= datetime.strptime(fecha,"%Y-%m-%d")
#     hoy = datetime.now()
#     totaldias=(hoy-fecha_nacimiento).days
#     print(f"total de dias es {totaldias}")

# fecha=input("Ingrese el la fecha de naciomiento con siguiente fotmato (YYYY-MM-DD): ")
# CantidadDias()
