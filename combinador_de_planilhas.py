import pandas as pd
import os
dir = r'C:\Users\Matheus\OneDrive\Nuvem\ELSC\PROJETOS\SGBDIT - CHESF - PREENCHIMENTO PLANILHAS\LOGS-DE-ENVIO'
list_file_in_dir_main = os.listdir(dir)
for i in list_file_in_dir_main:
    print("--------------------------------- "+i+" ---------------------------------")
    dir_folder_main = os.path.join(dir,i)
    if (os.path.isdir(dir_folder_main)):
        dir_folder_files = os.path.join(dir_folder_main,'VERIFICADOS')
        list_file_in_folder = os.listdir(dir_folder_files)
        join_file = pd.DataFrame()
        for file in list_file_in_folder:
            if (file != "planilha_unificada.xlsx"):
                dir_file = os.path.join(dir_folder_files,file)
                df = pd.read_excel(dir_file)        
                join_file = pd.concat([join_file, df], ignore_index=True)
                print("O arquivo "+file+" foi armazenado com sucesso na planilha")
            else:
                os.remove(os.path.join(dir_folder_files,file))
        join_file.to_excel(os.path.join(dir_folder_files,'planilha_unificada.xlsx'), index=False)
        print("--------------------------------- FOI CRIADA A PLANILHA UNIFICADA ---------------------------------")
print("Todas as planilhas foram geradas com sucesso")
