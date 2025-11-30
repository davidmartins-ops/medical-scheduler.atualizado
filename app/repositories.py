"""Módulo de Repositório para Gerenciamento de Consultas."""

import os
from typing import List
from app.entities import Consulta
from app.metadata import DIR_DADOS, NOME_ARQUIVO


# Define o caminho absoluto para o arquivo de dados
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE_PATH = os.path.join(BASE_DIR, DIR_DADOS, NOME_ARQUIVO)


def _ensure_file_exists() -> None:
    """Garante que o diretório e o arquivo de dados existam."""
    os.makedirs(os.path.dirname(FILE_PATH), exist_ok=True)
    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'w', encoding='utf-8') as f:
            pass  # Cria arquivo vazio


def listar_todas() -> List[Consulta]:
    """
    Lê o arquivo de texto e retorna uma lista de objetos Consulta.
    
    Returns:
        List[Consulta]: Lista contendo todas as consultas cadastradas.
    """
    _ensure_file_exists()
    consultas = []
    
    try:
        with open(FILE_PATH, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    consultas.append(Consulta.from_csv(line))
    except (IOError, ValueError) as e:
        print(f"Erro ao ler banco de dados: {e}")
        
    return consultas


def salvar_nova(consulta: Consulta) -> None:
    """
    Adiciona (append) uma nova consulta ao final do arquivo.
    """
    _ensure_file_exists()
    with open(FILE_PATH, 'a', encoding='utf-8') as f:
        f.write(consulta.to_csv() + '\n')


def sobrescrever_arquivo(consultas: List[Consulta]) -> None:
    """
    Reescreve todo o arquivo com a lista fornecida.
    Usado para operações de Atualização e Exclusão.
    """
    _ensure_file_exists()
    with open(FILE_PATH, 'w', encoding='utf-8') as f:
        for c in consultas:
            f.write(c.to_csv() + '\n')