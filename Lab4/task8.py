# Скачайте файл с информацией овсех государствах мира по адресу: https://github.com/mledoze/countries/blob/master/dist/countries.csv.
# Спомощью модуля pandasотобразите:
# 1) 10 самых маленьких и самых больших странмирапо территории;
# 2) 10 самых маленькихи самых большихстранмирапо населению;
# 3) все франко язычные страны мира;
# 4) только островные государства;
# 5) все страны, находящиесяв  южном  полушарии.
# Сгруппируйте  страны  по  первой  букве;  по населению; по территории.
# Программно сохраните в таблицу Excel все страны  с  выборочной  информацией:  название,  столица, население,
# территория, валюта, широта, долгота


import csv
import pandas as pd
from pandas import read_csv


countries_file = 'E:\\Univer\\2 kurs\Python\Lab4\\countries.csv'


def write_to_excel(table):
    names = pd.Series([d.split(',')[0] for d in table.name])
    names.name = 'name'
    lat, lng = zip(*[d.split(',')
                     if isinstance(d, str)
                     else ['nan', 'nan']
                     for d in table.latlng])
    lat, lng = map(pd.Series, (lat, lng))
    lat.name = 'latitude'
    lng.name = 'longitude'
    for_export = pd.concat([names, table[['capital', 'ccn3', 'area', 'currencies']], lat, lng], axis=1)
    with pd.ExcelWriter('exported.xls') as excel_writer:
        for_export.to_excel(excel_writer)


table = read_csv(countries_file, ',')


print('1) 10 самых маленьких и самых больших странмирапо территории:')
print('- Маленькие')
print(table.nlargest(n=10, columns='area')[['area', 'name']])
print('- Большие')
print(table.nsmallest(10, ['area'])[['area', 'name']])


print('2) 10 самых маленькихи самых больших стран мира по населению: ')
print('- Маленькие')
print(table.nlargest(10, ['ccn3'])[['ccn3', 'name']])
print('- Большие')
print(table.nsmallest(10, ['ccn3'])[['ccn3', 'name']])


print('3) все франко язычные страны мира:')
print(table[table.languages == 'French'][['languages', 'area', 'name']])


print('4) только островные государства:')
print(table[table.borders.isnull()][['name']])
write_to_excel(table=table)


print('5) все страны, находящиесяв  южном  полушарии:')
print(table.where(pd.Series([float(str(d).split(',')[0]) < 0 for d in table.latlng])).name.dropna())


for i, group in table.groupby(table.area):
    print(str(i) + ': ')
    for j, name in enumerate(group.name, 1):
        print(str(j) + '.', name.split(',')[0])
