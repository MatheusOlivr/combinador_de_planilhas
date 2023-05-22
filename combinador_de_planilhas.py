import pandas as pd
import os
dir = input("Digite o diretório onde está os arquivos \n")
list_file = os.listdir(dir)
join_file = pd.DataFrame()
print("--------------------------------- Script iniciado ---------------------------------")
for i in list_file:
    if (i != "planilha_unificada.xlsx"):
        file = os.path.join(dir,i)
        df = pd.read_excel(file)
        join_file = pd.concat([join_file,df],ignore_index=True)
        print("O arquivo "+i+" foi armazenado com sucesso na planilha")
    else:
        os.remove(file)
join_file.to_excel(os.path.join(dir,'planilha_unificada.xlsx'), index=False)
print("--------------------------------- FOI CRIADA A PLANILHA UNIFICADA ---------------------------------")
