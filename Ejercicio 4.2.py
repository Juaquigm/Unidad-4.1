#Ejercicio 4.2
def contador(palabra):
    palabra_diccionario={}
    letra = 0
    for letra in palabra:
        if letra in palabra_diccionario:
            palabra_diccionario[letra] = palabra_diccionario[letra] + 1

        else:
            palabra_diccionario[letra] = 1

        return palabra_diccionario

palabra = input("Introduce una palabra: ")

palabra_diccionario = contador(palabra)

print(palabra_diccionario)