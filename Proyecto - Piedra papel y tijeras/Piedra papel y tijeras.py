# Online Python Compiler

#Become a Data Analyst
#Piedra papel y tijeras

# Import command for the 'random' library
import random

# Function to display game instructions
def display_instructions():
    print('Bienvenido a Piedra Papel y Tijeras.\n')
    print('Reglas:')
    print('1. Piedra gana Tijeras')
    print('2. Tijeras gana Papel')
    print('3. Papel gana Piedra')

# Function to ask for the number of rounds
def get_rounds():
    rounds = input('\nCuantas rondas quieres jugar? \nRondas: > ')
    rounds = int(rounds)
    return rounds

# Function to get the player's choice
def get_player_choice():
    player_choice = input('\nEscoge Piedra Papel o Tijeras: \n > ')
    return player_choice

# Function to get the computer's choice
def get_computer_choice():
    options = ['piedra', 'papel', 'tijeras']
    computer_choice = random.choice(options)
    print('La computadora escogio', computer_choice)
    return computer_choice

# Function to determine the winner of the round
def determine_round_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        print('Empate!')
    elif ((player_choice == 'piedra' and computer_choice == 'tijeras') or (player_choice == 'papel' and computer_choice == 'piedra') or (player_choice == 'tijeras' and computer_choice == 'papel')):
        print('Ganaste!')
        return 'jugador'
    elif (player_choice == 'piedra' and computer_choice == 'papel')or(player_choice == 'papel' and computer_choice == 'tijeras')or(player_choice == 'tijeras' and computer_choice == 'piedra'):
        print('Ganó la Computadora!')
        return 'computadora'


# Function to determine the winner of the game
def announce_game_winner(player_score, computer_score):
    print('\nPuntuacion final: Jugador', player_score, '| Computadora', computer_score)
    if player_score > computer_score:
        print('Tu Ganaste!')
    elif player_score < computer_score:
        print('La computadora ganó!')
    else:
        print('Es un empate!')

# Function to contain the flow of the whole program
def main():
    computer_score = 0
    player_score = 0
    display_instructions()
    rounds = get_rounds()
    for i in range(rounds):
        print(f'\nRonda {i+1}:')
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        winner = determine_round_winner(player_choice, computer_choice)
        if winner == 'jugador':
            player_score += 1
        elif winner == 'computadora':
            computer_score += 1
        else:
            pass
        print('Jugador:', player_score, '| Computadora:', computer_score)
    # Function call to determine the winner of the game
    announce_game_winner(player_score, computer_score)

main()