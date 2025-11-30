"""Módulo de Metadados e Configurações."""

import os


DIR_DADOS = 'data'
NOME_ARQUIVO = 'repositorio.txt'
SEPARADOR_CSV = ','


# Formato para exibição e entrada do usuário (Brasil) e formato saida ISO
FORMATO_DATA_DISPLAY = "%d-%m-%Y"
FORMATO_DATA_STORAGE = "%Y-%m-%d"

HEADERS_TABELA = ["ID", "Paciente", "Médico", "Data", "Hora"]
MSG_SUCESSO = ">> Operação realizada com sucesso."
MSG_ERRO_ID = ">> Erro: ID não encontrado."
MSG_DATA_INVALIDA = f">> Data inválida! Use o formato {FORMATO_DATA_DISPLAY.replace('%', '')}."
