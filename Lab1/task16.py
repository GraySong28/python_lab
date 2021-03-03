# Напишитескрипт, который на основе списка из 16 названий футбольных  команд  случайным  образом  формирует  4  группы
# по  4 команды,  а  также  выводит  на  консоль  календарь  всех  игр  (игры должны проходить по средам, раз в 2 недели,
# начиная с 14 сентября текущего года).Даты игр необходимо выводить в формате «14/09/2016, 22:45».
# Используйте модули randomи itertools.


import random
from datetime import datetime, timedelta


teams_file = open(r"teams.txt", 'r')
command_list = [line.strip() for line in teams_file]
random.shuffle(command_list)
command_list = [command_list[i:i + 4] for i in range(0, 16, 4)]
teams_file.close()

print('\t Список групп:')
print('Группа 1:', command_list[0], '\n'
      'Группа 2:', command_list[1], '\n'
      'Группа 3:', command_list[2], '\n'
      'Группа 4:', command_list[3])


now_date = datetime.now()
now_date = now_date.replace(2021, 9, 14)
games_list_file = open(r'games.txt', 'r+')
start = datetime(2021, 9, 14)
step = timedelta(days = 14)
while start <= datetime(2022, 8, 14):
    start += step
    games_list_file.write('%s/%s/%s' % (start.day, start.month, start.year) + ', 20:00\n')
print('\t Список матчей:')
for line in games_list_file:
    print(line, end = '')
games_list_file.close()
