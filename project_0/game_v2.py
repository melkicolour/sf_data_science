'''Игра "Угадай число", компьютер сам загадывает и сам угадывает.'''


import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Заданное число. Defaults to 1.

    Returns:
        int: число попыток
    """
    count = 0
    while True:
        count += 1
        predict_number = np.random.randint(1, 101)
        if predict_number == number:
            break
    return count

def score_game(random_predict) -> int:
    """За какое кол-во попыток в среднем угадываем

    Args:
        random_predict (_type_): функция угадывания

    Returns:
        int: среднее кол-во попыток
    """
    count_ls = list()
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls))
    print(f'Ваш алгоритм угадывает число за {score} попыток.')
    return score

if __name__ == '__main__':
    score_game(random_predict)