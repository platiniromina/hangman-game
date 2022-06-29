import os
import time

def palabra_secreta():
    os.system('cls')
    palabra_secreta = input('Ingresá palabra a adivinar: ')
    while not palabra_secreta.isalpha() or ' ' in palabra_secreta:
        palabra_secreta = input('La palabra sólo puede contener letras, y tiene que ser una sola,\
ingresá otra vez:')
    return palabra_secreta.lower()

def ahorcado():
    # variables iniciales
    palabra = palabra_secreta()
    os.system('cls')    # borro pantalla así el jugador no ve la palabra
    vidas = 5
    jugar = True
    estado_inicial = '_ ' * len(palabra)    # cantidad de letras de la palabra
    estado_actual = estado_inicial
    letras_jugadas = []
    print('Bienvenido al juego del ahorcado!')      # reglas de juego
    print('Tenés 5 vidas para adivinar la palabra secreta, letra por letra')
    time.sleep(2)   # espero 2 segundos ...
    print('Perdés una vida cada vez que ingresás una letra que no está en la palabra')
    print('Y si te quedás sin vidas, perdés :(')
    print('Buena suerte!')
    time.sleep(2) 
    print(estado_inicial)
    continuar = input('-> Apretá cualquier tecla para continuar ')
    
    while jugar:
        os.system('cls')
        letra = input('Decime una letra: ')
        letra = letra.lower()
        if len(letra) != 1 or (not letra.isalpha()):
            print(f'Eso no es una letra. Intentá de nuevo')
        elif letra in letras_jugadas:
            print('Ya jugaste esa letra. Probá con otra')
        else:
            letras_jugadas.append(letra) # guardo las letras jugadas en una lista
            if letra in palabra:
                print(f'Buenísimo! La letra {letra.upper()} está en la palabra')
                estado_actual = '' # para imprimir los espacios y las letras que ya se adivinaron
                for letra in palabra:
                    if letra in letras_jugadas:
                        estado_actual += f'{letra} '
                    else:
                        estado_actual += '_ '
                print(estado_actual)
            else:
                vidas -= 1
                print(f'Uy! Esa letra no está en la palabra. Intentá de nuevo')
                print(f'Te quedan {vidas} vidas.')
                print(estado_actual)
        
        continuar = input('-> Apretá cualquier tecla para continuar ')
        if vidas == 0:
            jugar = False
            print(f'Perdiste! La palabra era {palabra.upper()}')
        
        if '_' not in estado_actual:
            jugar = False
            print(f'Ganaste! la palabra era {palabra.upper()}')
        

ahorcado()


#  __________
# |         O
# |        /|\
# |        / \
# |

