import requests as r
import datetime as dt
import csv

url = 'https://api.covid19api.com/country/brazil'
req = r.get(url)

raw_data = req.json()

final_data = []
for obs in raw_data:
    final_data.append([obs['Confirmed'], obs['Deaths'], obs['Recovered'], obs['Active'], obs['Date']])

final_data.insert(0, ['Confirmados', 'Obitos', 'Recuperados', 'Ativos', 'Data'])
    
CONTAMINADOS = 0
OBITOS = 1
RECUPERADOS = 2
ATIVOS = 3
DATA = 4

for i in range(1, len(final_data)):
    final_data[i][DATA] = final_data[i][DATA][:10]

    
with open('brasil-covid.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    for row in final_data:
       writer.writerow(row)
     
for i in range(1, len(final_data)):
    final_data[i][DATA] = dt.datetime.strptime(final_data[i][DATA], '%Y-%m-%d')

