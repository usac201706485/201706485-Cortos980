#EXAMEN CORTO1 201706485

""" DIGITOS A USAR 485 DESDE 2 """


def fileWrite(fileName = 'collatz.txt'):
    #Si el archivo 'fileName' no existe, se crea uno nuevo con ese nombre.
    archivo = open(fileName,'w') #Abrir para SOBREESCRIBIR el archivo existente
    archivo.write('Sobreescribiendo archivo...\n')
    print('Espere, sobreescribiendo el archivo...')
    for i in range(484):
        archivo.write(str(listaI))
    archivo.close() #Siempre cerrar el archivo al finalizar la escritura


entrada = 2
listaI = [] #Lista que se irá reciclando para guardar la secuencia de collatz
while entrada <= 485:
    numero = entrada
    listaI = []
    listaI.append(numero)
    while numero != 1: #Evaluacion si el numero actual es par
        if numero%2 == 0:
            numero /= 2
            listaI.append(numero)
            
        else:           #Evaluacion si el numero actual es impar
            numero = (numero * 3) + 1
            listaI.append(numero)
    fileWrite()
    print(listaI)        
    entrada += 1
    print('\n')


