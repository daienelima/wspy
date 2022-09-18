import csv
import pandas as pd
import shutil 

with open('alunos.csv', 'r') as file, open('alunos_copia.csv', 'w') as fileCopy:
    rows = csv.reader(file)
    writer = csv.writer(fileCopy)
    
    shutil.copyfile('alunos.csv','alunos_copia.csv') #copiar arquivo usando shutil
    for row in rows:
        #print(row)
        writer.writerow(row)
  
df = pd.read_csv("alunos_copia.csv")
df['Média'] = (df['Prova_1'] + df['Prova_2'] + df['Prova_3'] + df['Prova_4'])/ 4
df.to_csv("alunos_copia.csv", index=False)

print(df)
