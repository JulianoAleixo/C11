"""
By: Juliano Moreira Aleixo
https://julianoaleixo.dev
"""

import numpy as np

table = np.zeros([2, 2])
bomb_row = np.random.randint(0, 2)
bomb_col = np.random.randint(0, 2)

table[bomb_row, bomb_col] = 1

tries = 0
while True:
    print()
    while True:
        row_pos = int(input('Entre com o índice da linha (0 ou 1): '))
        if row_pos == 0 or row_pos == 1:
            break

    while 1:
        col_pos = int(input('Entre com o índice da coluna (0 ou 1): '))
        if col_pos == 0 or col_pos == 1:
            break

    if table[row_pos, col_pos] == 1:
        print('Game Over! :( Try Again!')
        break

    if table[row_pos, col_pos] == 2:
        print('Posição já testada, tente novamente...')

    if table[row_pos, col_pos] == 0:
        table[row_pos, col_pos] = 2
        print('A bomba não está aqui!')
        tries += 1
        if tries == 3:
            print('Congratulations! You beat the game! :)')
            break
