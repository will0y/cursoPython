#Exercicio03: atualizar valores de células 

import openpyxl 

#Carregar a planilha existente 
wb = openpyxl.load_workbook('exercicio1.xslx')
ws = wb.active 

#Atualizar valores de células 
ws['B3'] =33

# Salvar a planilha atualizada
wb.save('exercicio01.xsls')

#Fechar a planila 
wb.close()
