"""Módulo responsável pela Interface do Usuário (UI) do sistema."""

from datetime import datetime
from tabulate import tabulate

from app import services
from app.metadata import (
    FORMATO_DATA_DISPLAY,
    FORMATO_DATA_STORAGE,
    HEADERS_TABELA,
    MSG_SUCESSO,
    MSG_ERRO_ID,
    MSG_DATA_INVALIDA,
)


def _limpar_tela() -> None:
    """Simula limpeza de tela exibindo quebras de linha."""
    print("\n" * 2)


def _ler_data_validada() -> str:
    """Solicita uma data ao usuário no formato exibido e valida a entrada.

    Returns:
        str: Data convertida para o formato de armazenamento (ISO).

    """
    while True:
        formato_exibicao = FORMATO_DATA_DISPLAY.replace("%", "")
        data_input = input(f"Data ({formato_exibicao}): ")

        try:
            dt = datetime.strptime(data_input, FORMATO_DATA_DISPLAY)
            return dt.strftime(FORMATO_DATA_STORAGE)
        except ValueError:
            print(MSG_DATA_INVALIDA)


def _exibir_tabela(dados) -> None:
    """Exibe uma tabela formatada contendo dados de consultas.

    Args:
        dados (list): Lista de objetos Consulta.

    """
    if not dados:
        print("\n>> Nenhuma consulta encontrada.")
        return

    tabela = [
        [
            c.id_consulta,
            c.nome_paciente,
            c.nome_medico,
            c.data_consulta,
            c.horario_consulta,
        ]
        for c in dados
    ]

    print(tabulate(tabela, headers=HEADERS_TABELA, tablefmt="simple_grid"))


def view_cadastrar() -> None:
    """Exibe o formulário de cadastro e cria uma nova consulta."""
    print("\n--- Nova Consulta ---")

    paciente = input("Nome do Paciente: ")
    medico = input("Nome do Médico: ")
    data_db = _ler_data_validada()
    horario = input("Horário (HH:MM): ")

    services.criar_agendamento(paciente, medico, data_db, horario)

    print(f"\n{MSG_SUCESSO}")
    input("Pressione Enter para voltar...")


def view_listar() -> None:
    """Lista todas as consultas cadastradas."""
    print("\n--- Lista Geral ---")

    dados = services.obter_todas()
    _exibir_tabela(dados)

    input("\nPressione Enter para voltar...")


def view_atualizar() -> None:
    """Realiza a atualização de uma consulta existente."""

    view_listar()

    print("\n--- Atualizar Dados ---")
    id_alvo = input("ID da consulta para alterar (ex: 1 ou Cons01): ")

    print("\n(Deixe em branco para manter o valor atual)")
    novo_paciente = input("Novo Nome Paciente: ")
    novo_medico = input("Novo Médico: ")
    novo_horario = input("Novo Horário (HH:MM): ")

    sucesso = services.atualizar_dados(
        id_alvo,
        paciente=novo_paciente,
        medico=novo_medico,
        horario=novo_horario,
    )

    if sucesso:
        print(f"\n{MSG_SUCESSO}")
    else:
        print(f"\n{MSG_ERRO_ID}")

    input("Pressione Enter para voltar...")


def view_excluir() -> None:
    """Exclui uma consulta selecionada pelo usuário."""
    view_listar()

    print("\n--- Excluir Consulta ---")
    id_alvo = input("ID da consulta para EXCLUIR: ")

    sucesso = services.remover_agendamento(id_alvo)

    if sucesso:
        print(f"\n{MSG_SUCESSO}")
    else:
        print(f"\n{MSG_ERRO_ID}")

    input("Pressione Enter para voltar...")


def view_pesquisar() -> None:
    """Executa uma busca de consultas pelo termo informado pelo usuário."""
    print("\n--- Relatório de Pesquisa ---")

    termo = input("Digite nome do paciente, médico ou data: ")
    resultados = services.buscar_por_termo(termo)

    _exibir_tabela(resultados)
    input("\nPressione Enter para voltar...")


def iniciar_menu() -> None:
    """Menu principal da aplicação."""

    opcoes = {
        "1": view_cadastrar,
        "2": view_listar,
        "3": view_atualizar,
        "4": view_excluir,
        "5": view_pesquisar,
    }

    while True:
        _limpar_tela()

        print("=== SISTEMA DE AGENDAMENTO DE CONSULTAS ===")
        print("1. Cadastrar nova consulta")
        print("2. Listar todas as consultas")
        print("3. Atualizar consulta")
        print("4. Excluir consulta")
        print("5. Relatório de pesquisa")
        print("0. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "0":
            print("Encerrando sistema...")
            break

        acao = opcoes.get(opcao)
        if acao:
            acao()
        else:
            print("Opção inválida!")
            input("Pressione Enter para continuar...")
