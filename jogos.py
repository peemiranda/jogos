import forca
import adivinhacao
import pedrapapeltesoura


def choose_game():
    print("Escolha qual jogo você quer jogar!")

    print("(1) Adivinhação (2) Forca (3) Pedra papel ou tesoura")

    game = int(input("Qual jogo você pretende jogar? "))

    if game == 1:
        print("Jogando Adivinhação")
        adivinhacao.play()
    elif game == 2:
        print("Jogando Forca")
        forca.play()
    else:
        print("Jogando Pedra papel ou tesoura")
        pedrapapeltesoura.play()


if __name__ == "__main__":
    choose_game()


#    while game() not in (1, 2, 3):
#    game() = input("pedra, papel, ou tesoura?: ").lower()
#    print("Escolha qual jogo você quer jogar!")
#    print("(1) Adivinhação (2) Forca (3) Pedra papel ou tesoura")
