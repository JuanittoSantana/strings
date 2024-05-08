""" Escribir un programa que pregunte por consola el precio de un producto en pesos 
con dos decimales y muestre por pantalla el número de pesos y el número de centavos 
del precio introducido. """

precio = input("Introduce el precio del producto con dos decimales:  ")
print(precio[:precio.find('.')], 'pesos y', precio[precio.find('.')+1:], 'centavos.')