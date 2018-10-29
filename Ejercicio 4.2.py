#Ejercicio 4.2
def contador (letra,palabra):
    i = 0
    numero_veces = 0
    while i < len(palabra):
        if letra == palabra[i]:
            numero_veces = numero_veces + 1
        i = i + 1
        return numero_veces

indice = 0
palabra = input("Introduzca una palabra: ")

while indice <  len(palabra):
    veces = 0
    letra = palabra[indice]
    veces = contador(letra,palabra)
    print(veces,letra, end="")
    indice = indice + 1
