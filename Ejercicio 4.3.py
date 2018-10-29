#Ejercicio 4.3
import random
ahorcado = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']
palabras_azar = 'cerillas patrulla papel azor alerones conversar sollozo manzana'.split()

def palabra_elegida(listapalabras_azar): #En esta funcion nos devuelve la palabra que tenemos que averiguar
    palabra_elegida = random.randint(0, len(listapalabras_azar) - 1)
    return listapalabras_azar[palabra_elegida]


def pantalla(ahorcado, letra_incorrecta, letra_correcta, palabra_acertar):
    print(ahorcado[len(letra_incorrecta)])
    print("")
    fin = " "
    print('Letras incorrectas:', fin)
    for letra in letra_incorrecta:
        print(letra, fin)
    print("")
    espacio = '_' * len(palabra_acertar)
    for i in range(len(palabra_acertar)):  # Aqui reemplazamos el espacio en blanco por la letra acertada
        if palabra_acertar[i] in letra_correcta:
            espacio = espacio[:i] + palabra_acertar[i] + espacio[i + 1:]
    for letra in espacio: #Aqui se muestra la palabra a acertar entre espacios
        print (letra, end= fin)
    print ("")


def letra_sola(letra_alguna):
    # Aqui nos aseguramos de que el usuario introduce una letra y no cualquier cosa
    while True:
        print('Adivina una letra:')
        letra = input()
        letra = letra.lower()
        if len(letra) != 1:
            print('Introduce una sola letra.')
        elif letra in letra_alguna:
            print('Letra repetida. ¿Qué tal si pruebas con otra?')
        elif letra not in 'abcdefghijklmnopqrstuvwxyz':
            print('Introduzca una letra.')
        else:
            return letra


def Comenzar():
    #Funcion para ver si el jugador quiere volver a jugar. True para seguir y false para acabar
    print('Otra partida? (Si o No)')
    return input().lower().startswith('s')


print("Bienvenido al")
print("-------------")
print("A H O R C A D O")
letra_incorrecta = ""
letra_correcta = ""
palabra_acertar = palabra_elegida(palabras_azar)
fin_juego = False
while True:
    pantalla(ahorcado, letra_incorrecta, letra_correcta, palabra_acertar)
    #El jugador mete una letra
    letra = letra_sola(letra_incorrecta + letra_correcta)
    if letra in palabra_acertar:
        letra_correcta = letra_correcta + letra
        
        letras_encontradas = True
        for i in range(len(palabra_acertar)):
            if palabra_acertar[i] not in letra_correcta:
                letras_encontradas = False
                break
        if letras_encontradas:
            print("OLEEEE!!!! Has acertado la palabra a acertar era '",palabra_acertar,"' y has salvado al monigote!!!")
            fin_juego = True
    else:
        letra_incorrecta = letra_incorrecta + letra
        #Mira la cantidad de letras metida por el jugar y ver si ha perdido
        if len(letra_incorrecta) == len(ahorcado) - 1:
            pantalla(ahorcado, letra_incorrecta, letra_correcta, palabra_acertar)
            print("Vaya! No ha logrado salvar al monigote, la palabra correcta era '",palabra_acertar, "'")
            print("D.E.P Amigo")
            fin_juego = True
    # Pregunta al jugador si quiere jugar de nuevo
    if fin_juego:
        if Comenzar():
            letra_incorrecta = ""
            letra_correcta = ""
            fin_juego = False
            palabra_acertar = palabra_elegida(palabras_azar)
        else:
            break