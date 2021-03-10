# Напишитескрипт, который на основе списка из 16 названий футбольных  команд  случайным  образом  формирует  4  группы
# по  4 команды,  а  также  выводит  на  консоль  календарь  всех  игр  (игры должны проходить по средам, раз в 2 недели,
# начиная с 14 сентября текущего года).Даты игр необходимо выводить в формате «14/09/2016, 22:45».
# Используйте модули randomи itertools.


from random import shuffle
import itertools
from time import strftime
import time
from datetime import timedelta, datetime


def task16():
    format = "%d/%m/%Y, %H:%M"
    start = datetime.strptime("14/09/2021, 22:45", format)
    teams_file = open(r"teams.txt", 'r')
    teams = [line.strip() for line in teams_file]
    teams_file.close()
    shuffle(teams)
    teams = [teams[i*4:i*4+4] for i in range(0, 4)]
    games = []
    for t in teams:
        games.append([c for c in itertools.combinations(t, 2)])
    games_list_file = open(r'games.txt', 'r+')
    for i in range(0, 6):
        print(start.strftime(format))
        games_list_file.writelines(start.strftime(format) + '\n')
        print("Игра:", i + 1)
        games_list_file.writelines("Игра:" + str(i + 1) + '\n')
        print(games[0][i])
        games_list_file.writelines(str(games[0][i]) + '\n')
        print(games[1][i])
        games_list_file.writelines(str(games[1][i]) + '\n')
        print(games[2][i])
        games_list_file.writelines(str(games[2][i]) + '\n')
        print(games[3][i])
        games_list_file.writelines(str(games[3][i]) + '\n')
        start = start + timedelta(days=14)
    print("Окончание чемпионата")
    print(start.strftime(format))
    games_list_file.close()


task16()
