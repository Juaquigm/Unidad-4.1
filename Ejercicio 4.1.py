#Ejercicio 4.1
import string
try:
    indice = 0
    consonantes =" " #Variable donde se almacenan las consonantes de la palabra introducida
    vocales = " " #Variable donde se almacenan las vocales de la palabra introducida
    palabra = input("Introduzca texto: ")
    palabra_cambiada = " "
    while indice < len(palabra): #Recorrido de la palabra
        if palabra[indice] in "a,e,i,o,u":  #Condicion de que la letra de la palabra sea vocal
            vocales = vocales + palabra[indice]
            palabra_cambiada = palabra_cambiada + palabra[indice].upper() #Aqui cambiamos la vocal a mayuscula
        else:
            consonantes = consonantes + palabra[indice]
            palabra_cambiada = palabra_cambiada + palabra[indice]
        indice = indice + 1 #Aumentamos en 1 el indice

    print(consonantes) #Se muestran las consonantes de la palabra
    print(vocales) #Se muestran las vocales de la palabra
    print(palabra_cambiada) #Muestra la palabra con las mayusculas en las vocales
except:
    print("Ha introducido un elemento no valido para el programa.")






