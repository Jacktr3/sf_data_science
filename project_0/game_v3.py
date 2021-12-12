import numpy as np


def game_core_v3(number: int = 1) -> int:
    """Сначала задаем число, середина диапозона поиска числа, а потом уменьшаем
    или увеличиваем его в зависимости от того, больше оно или меньше загаданного числа.
       Функция принимает загаданное число и возвращает число попыток за которое алгоритм определил загаданное число arrow_up в readme
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь

    count = 0   # счетчик попыток
    prdict_number_min = 1  # нижняя граница поиска числа
    prdict_number_max = 100  # верхняя граница поиска числа
    predict_number = (prdict_number_max + prdict_number_min) // 2 # предполагаемое число
   
    
    while number!=predict_number:
        count+=1
        
        if number > predict_number:
            if number-predict_number > 20:
                predict_number+=20      # увеличиваем предполагаемое число на 20
            elif number-predict_number <= 20 and number-predict_number >= 10:
                predict_number+=10      # увеличиваем предполагаемое число на 10
            elif number-predict_number < 10:
                predict_number+=1       # увеличиваем предполагаемое число на 1

        elif number < predict_number:
            if predict_number-number > 20:
                predict_number-=20      # уменьшаем предполагаемое число на 20
            elif predict_number-number <= 20 and predict_number-number >= 10:
                predict_number-=10      # уменьшаем предполагаемое число на 10
            elif predict_number-number < 10:
                predict_number-=1       # уменьшаем предполагаемое число на 1

    # Ваш код заканчивается здесь

    return count

def score_game(game_core_v3) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм
    Args:
        game_core_v3 ([type]): функция угадывания
    Returns:
        int: среднее количество попыток
    """

    count_ls = []  # список для сохранения количества попыток
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(game_core_v3(number))

    score = int(np.mean(count_ls))  # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return score

if __name__ == '__main__':
    # RUN
    score_game(game_core_v3)

print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)