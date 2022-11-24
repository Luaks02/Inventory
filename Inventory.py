from openpyxl import workbook, load_workbook
from openpyxl.utils import get_column_letter

#Abrindo a planilha e iniciando variavel de quantidade de linhas já usadas no Estoque
wb = load_workbook('Estoque.xlsx')
ws = wb["SmartHaus"]

end_row = len(ws["A"])

#Iniciando classe de objeto para organizar as informações de cada produto
class Produtos:
    def __init__(self,nome,qnt,valor,descricao,marca):
        self.nome = nome
        self.qnt = qnt
        self.valor = valor
        self.descricao = descricao
        self.marca = marca

#Subindo as informações da planilha banco de dados para o código
estoque = []

for row in range(2,end_row+1):
    estoque.append(Produtos(ws["A"+str(row)].value,ws["B"+str(row)].value,ws["C"+str(row)].value,ws["D"+str(row)].value,ws["E"+str(row)].value,))

#Adicionando novos produtos ao banco de dados
def adicionar_estoque():
    wb = load_workbook('Estoque.xlsx')
    ws = wb["SmartHaus"]
    while True:
        nome = input("Nome do produto:")
        if len(nome) != 0:
            break
        else:
            print("Campo obrigatório")
    while True:
        qnt = input("Quantos estão entrando no estoque?")
        if qnt.isdigit():
            break
        elif len(qnt) == 0:
            qnt = 0
            break
        else:
            print("Quantidade deve ser números")
    while True:
        valor = input("Valor por unidade:")
        if valor.isdigit():
            valor = int(valor)
            if valor > 0:
                break
            else:
                print("O valor não pode ser 0")
        else:
            print("O valor deve ser número")
    while True:
        descricao = input("Descrição do produto:")
        if len(descricao) == 0:
            descricao = "Produto sem descrição."
            break
        else:
            break
    while True:
        marca = input("Marca do produto:")
        if len(marca) != 0:
            break
        else:
            print("Campo obrigatório")
    end_row = len(ws["A"]) + 1
    ws["A" + str(end_row)] = nome
    ws["B" + str(end_row)] = qnt
    ws["C" + str(end_row)] = valor
    ws["D" + str(end_row)] = descricao
    ws["E" + str(end_row)] = marca
    estoque.append(Produtos(nome,qnt,valor,descricao,marca))
    print("Produto adicionado ao estoque!")
    wb.save('Estoque.xlsx')
    
#Adicionar qnt de um produto já existente
def Adicionar_qnt():
    produto = input("Qual produto gostaria de adicionar qnt?")
    produto = str(produto)
    wb = load_workbook('Estoque.xlsx')
    ws = wb["SmartHaus"]
    for row in range(2,end_row+1):
        if ws["A"+str(row)].value == produto:
            quantidade = input("Quantos produtos estão entrando no estoque?")
            if quantidade.isdigit():
                quantidade = int(quantidade)
                ws["B"+str(row)] = int(ws["B"+str(row)].value) + quantidade
                wb.save('Estoque.xlsx')
                print("Produtos adicionado ao estoque!")

Adicionar_qnt()