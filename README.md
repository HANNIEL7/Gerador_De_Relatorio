# Gerador de Relatório de Vendas - Google Sheets

Este projeto Python cria automaticamente uma planilha de relatório de vendas no Google Sheets, insere dados de produtos e calcula os totais com fórmulas.

---

## Funcionalidades

- Autenticação com Google Sheets via `credenciais.json`
- Criação de nova planilha com título e aba personalizada
- Inserção de dados com cálculo automático de totais
- Cálculo de total geral com fórmula `=SUM()`
- Compartilhamento automático com um e-mail específico
- Formatação de moeda na coluna de totais
- Geração de data/hora na planilha

---

##  Requisitos

- Python 3.8+
- Conta do Google + Acesso à [Google Cloud Console](https://console.cloud.google.com/)
- Biblioteca `gspread` e `gspread-formatting`

---
