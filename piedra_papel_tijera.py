import random

def nuevo_juego():
    print("***Piedra, Pepel o Tijera***")
    opciones = ["piedra", "papel", "tijera"]

    while True:
        usuario_elije = input("Elija una opción (piedra, papel o tijera): ").lower()
        if usuario_elije not in opciones:
            print("Opción no valida. Favor elija una opción y escriba en minúsculas")
        else:
            computadora_elije = random.choice(opciones)
            print("Comprutadora elijió: ", computadora_elije)

            if usuario_elije == computadora_elije:
                print("Empate")
            elif(usuario_elije == "piedra" and computadora_elije == "tijera") or \
                (usuario_elije == "papel" and computadora_elije == "piedra") or \
                (usuario_elije == "tijera" and computadora_elije == "papel"):
                print("Ganaste")
                break
            else:
                print("Perdiste")
                break
nuevo_juego()

seguir_jugando = input("Jugar de Nuevo? y/n: ")
respuesta = seguir_jugando

if respuesta == "y":
    nuevo_juego()
else:
    exit()
                
    
