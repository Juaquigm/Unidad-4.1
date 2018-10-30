palabra = input("Introduce una palabra: ")

palabra_diccionario = {}

letra = 0
for letra in palabra:
    if letra in palabra_diccionario:
        palabra_diccionario[letra] = palabra_diccionario[letra] + 1
        
    else:
        palabra_diccionario[letra] = 1
        
print(palabra_diccionario)