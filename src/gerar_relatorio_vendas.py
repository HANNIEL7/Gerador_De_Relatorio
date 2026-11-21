import os
import gspread
from datetime import datetime
from google.oauth2.service_account import Credentials
from gspread_formatting import format_cell_range, CellFormat, NumberFormat

def autenticar_google():
    """Autentica com as APIs do Google usando o arquivo credenciais.json"""
    if not os.path.exists("credenciais.json"):
        raise FileNotFoundError("Arquivo credenciais.json não encontrado.")
    
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]
    credenciais = Credentials.from_service_account_file("credenciais.json", scopes=scopes)
    return gspread.authorize(credenciais)

def criar_planilha(gc, nome_planilha, email_compartilhar=None):
    """Cria a planilha e compartilha com o e-mail (opcional)"""
    planilha = gc.create(nome_planilha)
    
    if email_compartilhar:
        planilha.share(email_compartilhar, perm_type='user', role='writer')
    
    return planilha

def formatar_valores(aba, intervalo='D2:D100'):
    """Formata a coluna de totais como moeda"""
    moeda_format = CellFormat(numberFormat=NumberFormat(type='CURRENCY', pattern='R$ #,##0.00'))
    format_cell_range(aba, intervalo, moeda_format)

def preencher_dados(aba):
    """Insere os dados na planilha e calcula os totais"""
    aba.update_title("Vendas")

    cabecalhos = ["Produto", "Quantidade", "Preço Unitário", "Total"]
    dados = [
        ["Caneta", 10, 1.50],
        ["Caderno", 5, 10.00],
        ["Borracha", 20, 0.75],
        ["Lápis", 30, 0.50]
    ]

    for item in dados:
        item.append(item[1] * item[2])

    aba.update([cabecalhos] + dados)

    linha_total = len(dados) + 2
    aba.update(f"C{linha_total}", "Total Geral:")
    aba.update(f"D{linha_total}", f"=SUM(D2:D{linha_total - 1})")

    data_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    aba.update('F1', f"Relatório gerado em: {data_atual}")

    formatar_valores(aba)

def gerar_relatorio():
    """Função principal para executar o processo completo"""
    nome_planilha = "Relatório de Vendas"
    email_destino = "SEU_EMAIL@gmail.com"  # <- Substitua aqui

    print(" Autenticando...")
    gc = autenticar_google()

    print(" Criando planilha...")
    planilha = criar_planilha(gc, nome_planilha, email_destino)

    print(" Preenchendo dados...")
    aba = planilha.sheet1
    preencher_dados(aba)

    print(" Relatório criado com sucesso no Google Drive!")

if __name__ == "__main__":
    gerar_relatorio()
