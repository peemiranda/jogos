import random


def play():
    while True:
        choices = ["pedra", "papel", "tesoura"]

        computer = random.choice(choices)
        player = None

        while player not in choices:
            player = input("pedra, papel, ou tesoura?: ").lower()

        if player == computer:
            print("Computador: ", computer)
            print("Jogador: ", player)
            print("Empate!")

        elif player == "pedra":
            if computer == "papel":
                print("Computador: ", computer)
                print("Jogador: ", player)
                print("Você perdeu!")
            if computer == "tesoura":
                print("Computador: ", computer)
                print("Jogador: ", player)
                print("Você ganhou!")

        elif player == "tesoura":
            if computer == "pedra":
                print("Computador: ", computer)
                print("Jogador: ", player)
                print("Você perdeu!")
            if computer == "papel":
                print("Computador: ", computer)
                print("player: ", player)
                print("Você ganhou!")

        elif player == "papel":
            if computer == "tesoura":
                print("Computador: ", computer)
                print("Jogador: ", player)
                print("Você perdeu!")
            if computer == "pedra":
                print("Computador: ", computer)
                print("Jogador: ", player)
                print("Você ganhou!")

        play_again = input("Quer jogar novamente? (sim/não): ").lower()

        if play_again != "sim":
            break

    print("Obrigado por jogar! Tchau!!")


if __name__ == "__main__":
    play()
