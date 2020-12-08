win = int(input('Сколько побед одержала команда - '))
draw = int(input('Сколько игр было сыграно вничью - '))
loss = int(input('Сколько игр было проиграно - '))


def count_points(win, draw, loss):
    return (win * 3) + (draw * 1) + (loss * 0)


print('Итоговое количество очков: ' + str(count_points(win, draw, loss)))