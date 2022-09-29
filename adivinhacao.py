import random


def play():
    while True:
        print("Bem vindo ao jogo de adivinhação")

        secret_number = random.randrange(0, 101)
        total_attempts = 0
        points = 1000

        print("Qual nível de dificuldade?")
        print("(1) Fácil (2) Médio (3) Difícil")

        level = int(input("Defina o nível desejado: "))

        if level == 1:
            total_attempts = 20
        elif level == 2:
            total_attempts = 10
        else:
            total_attempts = 5

        for rounds in range(1, total_attempts + 1):
            chute_str = (input("Digite um número entre 1 e 100:"))
            print("Tentativa {} de {}".format(rounds, total_attempts))
            print("Você digitou", chute_str)
            chute = int(chute_str)

            if chute < 1 or chute > 100:
                print("Você deve digitar um número entre 1 e 100!")
                continue

            right = chute == secret_number
            bigger = chute > secret_number
            smaller = chute < secret_number

            if right:
                print("Você acertou e fez {} pontos!".format(points))
                break
            else:
                if bigger:
                    print("Você errou :( O seu chute foi maior do que o número secreto!")
                elif smaller:
                    print("Você errou :( O seu chute foi menor do que o número secreto!")
                lost_numbers = abs(secret_number - chute)
                points = points - lost_numbers

        print("Fim do jogo!")

        play_again = input("Quer jogar novamente? (sim/não): ").lower()

        if play_again != "sim":
            break


    print("Obrigado por jogar! Tchau!!")


if __name__ == "__main__":
    play()
