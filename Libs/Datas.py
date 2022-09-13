import datetime as dt

print(dt.time(12, 6, 21, 7), 'Hora Minuto Segundo Microsegundo')
print(dt.date(2022, 9, 13), 'Ano Mes Dia')
print(dt.datetime(2022, 9, 12, 12, 6, 21, 7), 'Ano Mes Dia Hora Minuto Segudo Microsegundo')

natal = dt.date(2020, 12, 25)
reveillon = dt.date(2021, 1, 1)

print(reveillon - natal)
print((reveillon - natal).days)
print((reveillon - natal).seconds)
print((reveillon - natal).microseconds)