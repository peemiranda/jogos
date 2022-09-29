import random


def play():
    while True:
        print_start_message()
        secret_word = load_secret_word()
        correct_letters = initialize_right_letters(secret_word)

        hanged = False
        acertou = False
        errors = 0

        print(correct_letters)

        while not hanged and not acertou:

            chute = order_chute()

            if chute in secret_word:
                mark_correct_chute(chute, correct_letters, secret_word)
            else:
                errors += 1
                desenha_forca(errors)

            hanged = errors == 7
            acertou = "_" not in correct_letters
            print(correct_letters)

        if acertou:
            print_winner_message()
        else:
            print_looser_message(secret_word)

        play_again = input("Quer jogar novamente? (sim/não): ").lower()

        if play_again != "sim":
            break
        print("Obrigado por jogar! Tchau!!")


def mark_correct_chute(chute, correct_letters, secret_word):
    index = 0
    for letra in secret_word:
        if chute == letra:
            correct_letters[index] = letra
        index += 1

    remaining_letters = str(correct_letters.count('_'))
    print('Ainda faltam acertar {} letras'.format(remaining_letters))
    return


def desenha_forca(errors):
    print("  _______     ")
    print(" |/      |    ")

    if errors == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if errors == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if errors == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if errors == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if errors == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if errors == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if errors == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")
        print(" |            ")
        print("_|___         ")
        print()


def print_winner_message():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def print_looser_message(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def order_chute():
    chute = chute = input("Qual a letra?").strip().upper()
    return chute


def initialize_right_letters(word):
    return ["_" for word in word]


def print_start_message():
    print("Bem vindo ao jogo da Forca!")


def load_secret_word():
    file = open("palavras.txt", "r")
    words = []

    for line in file:
        line = line.strip()
        words.append(line)
    file.close()

    number = random.randrange(0, len(words))
    secret_word = words[number].upper()
    return secret_word


if __name__ == "__main__":
    play()

    input("Qual letra? ")
