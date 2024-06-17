from random import randint

NUM_ADIV_FACIL = 10
NUM_ADIV_DIFICIL = 5
MIN_NUM = 1
MAX_NUM = 100


def set_difficulty():
    """
    Solicita al usuario que seleccione un nivel de dificultad para el juego.
    El usuario puede elegir entre 'facil' y 'dificil'.

    Return:
        int: El numero de intentos que depende del nivel de dificultad seleccionado.
    """
    nivel = input("Elige un nivel de dificultad: (facil/dificil) \n")
    if nivel == 'facil':
        return NUM_ADIV_FACIL
    elif nivel == 'dificil':
        return NUM_ADIV_DIFICIL
    else:
        print("Nivel incorrecto. Intentalo de nuevo.")
        return set_difficulty()

def determine_num_guess(players_guess, target, guess_number):
    """
    Determina si el numero del jugador es correcto y cambia el numero de intentos restantes.

    Parametros:
        players_guess (int): El numero del jugador.
        target (int): El numero que el jugador debe adivinar.
        guess_number (int): El numero de intentos restantes.

    Return:
        int: El numero de intentos restantes.
    """
    if players_guess > target:
        if guess_number == 1:
            print("Demasiado alto.")
        else:
            print("Demasiado alto. Adivina de nuevo")
        return guess_number - 1
    elif players_guess < target:
        if guess_number == 1:
            print("Demasiado bajo.")
        else:
            print("Demasiado bajo. Adivina de nuevo")
        return guess_number - 1

def game():
    """
    Ejecuta el juego. Genera un numero aleatorio que el jugador debe adivinar y maneja el ciclo de juego.
    """
    print("Estoy pensando en un numero entre 1 y 100.")
    number_of_guesses = set_difficulty()

    number = randint(1,100)
    # Para probar
    print(f"Numero correcto: {number}")

    while number_of_guesses > 0:
        print(f"Tienes {number_of_guesses} intentos restantes para adivinar el numero.")
        guess =  input('Adivina el numero: ')
        if guess.isdigit() and MIN_NUM <= int(guess) <= MAX_NUM:
            guess = int(guess)
        else:
            print("Numero invalido. Intentalo de nuevo.")
            continue

        if guess == number:
            print("¡Has adivinado correctamente el numero!")
            return

        number_of_guesses = determine_num_guess(guess, number, number_of_guesses)

        if number_of_guesses == 0:
            print(f"No tienes mas intentos. El numero correcto era {number}")
            return

if __name__ == '__main__':
    game()