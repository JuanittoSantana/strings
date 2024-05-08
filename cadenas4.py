""" Los teléfonos de una empresa tienen el siguiente formato prefijo-número 
donde el prefijo es el código del país +52 (por ejemplo +52-622-126-1307). Escribir un 
programa que pregunte por un número de teléfono con este formato en la consola y muestre 
por pantalla el número de teléfono sin el prefijo. """

tel = input("Introduce un número de teléfono con el formato +xx--xxx-xxx-xxxx: ")
print('El número de teléfono es ', tel[4:16])