import random
from colorama import Fore

# Función para iniciar el juego
def jugar():
    print(Fore.BLUE + "--- ¡Bienvenido al juego de Adivina el Número! ---")
    print(Fore.GREEN + "\nEstoy pensando en un número entre 1 y 100.")
    print(Fore.GREEN + "¿Puedes adivinar cuál es?")

    # El programa elige un número aleatorio entre 1 y 100
    numero_secreto = random.randint(1, 100)

    # Variable para controlar si el jugador ha adivinado
    adivinado = False
    intentos = 0

    while not adivinado:
        try:
            # Pedimos un número al jugador
            intento = int(input(Fore.GREEN + "\nIntroduce tu número: "))
            intentos += 1

            # Comparamos el intento con el número secreto
            if intento < numero_secreto:
                print(Fore.RED + "¡Número bajo! Intenta con un número más alto.")
            elif intento > numero_secreto:
                print(Fore.RED + "¡Número alto! Intenta con un número más bajo.")
            else:
                print(Fore.GREEN + f"¡Felicidades! Has adivinado el número en {intentos} intentos.")
                adivinado = True
        except ValueError:
            # Si el jugador no introduce un número válido
            print(Fore.RED + "Por favor, introduce un número válido.")

# Bucle principal del juego
while True:
    jugar()  # Inicia el juego
    # Preguntar si quiere jugar otra vez
    jugar_de_nuevo = input(Fore.BLUE + "\n¿Quieres jugar otra vez? (s/n): ").strip().lower()
    if jugar_de_nuevo != "s":
        print(Fore.BLUE + "¡Gracias por jugar! ¡Hasta luego!")
        break
