#Ejemplo_while_2
cont = 0
num = int(input('Ingrese un numero (cero (0) para terminar): '))
while num != 0:
    if num > 10:
        cont = cont + 1
    
    num = int(input('Ingrese otro numero (o cero (0) para terminar): '))
print('Cantidad de números mayores a 10 es:', cont)