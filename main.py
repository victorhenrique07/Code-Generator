import random


def random_code(new_shuffled):
    lista = random.sample(new_shuffled, 8)
    j = ''
    for i in lista:
        j += i
    print(j)

    while True:
        run_again = str(input('Do you wanna generate another code? [S/n]: ')).upper()
        if run_again == 'S':
            random_code('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
        else:
            break
        return
