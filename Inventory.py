from openpyxl import workbook, load_workbook
from openpyxl.utils import get_column_letter

class Produtos:
    def __init__(self,nome,qnt,valor,descricao,marca):
        self.nome = nome
        self.qnt = qnt
        self.valor = valor
        self.descricao = descricao
        self.marca = marca

estoque = []
estoque.append(Produtos("micro_inversor_151506_4",0,2998,"SUN2000G3-US-220 2KW MONOFASICO 220V 4MPPT MONITORAMENTO","DEYE"))
estoque.append(Produtos("inversor_hibrido_177342_2",0,8639,"SUN-3K-SG04LP1-EU 3KW MONOFASICO 220V MPPT MONITORAMENTO","DEYE"))
estoque.append(Produtos("inversor_hibrido_177343_6",0,10879,"SUN-5K-SG04LP1-EU 5KW MONOFASICO 220V 2MPPT MONITORAMENTO","DEYE"))
estoque.append(Produtos("inversor_hibrido_177346_8",0,19719,"SUN-8K-SG04LP1-EU 8KW MONOFASICO 127/220V 2MPPT MONITORAMENTO","DEYE"))
estoque.append(Produtos("inversor_hibrido_177345_4",0,24139,"SUN-10K-SG04LP1-EU 10KW TRIFASICO 380V 2MPPT MONITORAMENTO","DEYE"))
estoque.append(Produtos("inversor_on_grid_68207_0",0,2229,"MIC 1500 TL-X 1.5KW MONOFASICO 220V 1MPPT MONITORAMENTO","GROWATT"))
estoque.append(Produtos("inversor_on_grid_68208_4",0,2449,"MIC 2000 TL-X 2KW MONOFASICO 220V 1MPPT MONITORAMENTO","GROWATT"))
estoque.append(Produtos("inversor_on_grid_68210_5",0,2539,"MIC 2500 TL-X 2.5KW MONOFASICO 220V 1MPPT MONITORAMENTO","GROWATT"))
estoque.append(Produtos("inversor_on_grid_68211_9",0,2719,"MIC 3000 TL-X 3KW MONOFASICO 220V 1MPPT MONITORAMENTO","GROWATT"))
estoque.append(Produtos("inversor_on_grid_68202_0",0,3509,"MIC 3000 TL-X 3KW MONOFASICO 220V 2MPPT MONITORAMENTO","GROWATT"))

wb = load_workbook('Estoque.xlsx')
ws = wb["SmartHaus"]

end_row = len(ws["A"])

for row in range(2,end_row+1):
    for produto in  estoque:
        if produto.nome == ws["A"+str(row)].value:
            produto.qnt = ws["B"+str(row)].value
            print("O produto {} ainda tem {} unidades".format(produto.nome,produto.qnt))
