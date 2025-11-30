"""Modulo de Serviços de Agendamento de Consultas."""

from typing import List
from app.entities import Consulta
from app import repositories


def _gerar_novo_id() -> str:
    """Gera um novo ID sequencial (ex: Cons05 -> Cons06).
    
    Returns:
        str: O novo ID gerado.

    """
    consultas = repositories.listar_todas()
    if not consultas:
        return "Cons01"
    
    last_id = consultas[-1].id_consulta
    try:
        num_str = ''.join(filter(str.isdigit, last_id))
        num = int(num_str)
        return f"Cons{num + 1:02d}"
    except ValueError:
        return f"Cons{len(consultas) + 1:02d}"


def _normalizar_id(id_input: str) -> str:
    """Normaliza a entrada do usuário para o padrão do sistema.
    Ex: '1' vira 'Cons01', 'cons5' vira 'Cons05'.

    """
    id_input = id_input.strip()
    
    if id_input.isdigit():
        return f"Cons{int(id_input):02d}"
    if id_input.lower().startswith("cons"):
        parts = ''.join(filter(str.isdigit, id_input))
        if parts:
            return f"Cons{int(parts):02d}"
            
    return id_input


def criar_agendamento(paciente: str, medico: str, data: str, horario: str) -> Consulta:
    """Cria uma nova entidade Consulta e solicita ao repositório que a salve."""

    novo_id = _gerar_novo_id()
    nova_consulta = Consulta(novo_id, paciente, medico, data, horario)
    repositories.salvar_nova(nova_consulta)
    return nova_consulta


def obter_todas() -> List[Consulta]:
    """Retorna todas as consultas do repositório."""

    return repositories.listar_todas()


def buscar_por_termo(termo: str) -> List[Consulta]:
    """Filtra consultas onde o termo aparece no nome do paciente, médico ou data."""

    todas = repositories.listar_todas()
    termo = termo.lower()
    return [
        c for c in todas 
        if termo in c.nome_paciente.lower() 
        or termo in c.nome_medico.lower() 
        or termo in c.data_consulta
    ]


def atualizar_dados(id_alvo: str, **kwargs) -> bool:
    """Atualiza campos específicos de uma consulta baseada no ID.
    
    Returns:
        bool: True se encontrou e atualizou, False caso contrário.

    """
    id_formatado = _normalizar_id(id_alvo)
    consultas = repositories.listar_todas()
    encontrado = False
    
    for i, c in enumerate(consultas):
        if c.id_consulta == id_formatado:
            if kwargs.get('paciente'):
                c.nome_paciente = kwargs['paciente']
            if kwargs.get('medico'):
                c.nome_medico = kwargs['medico']
            if kwargs.get('horario'):
                c.horario_consulta = kwargs['horario']
            
            consultas[i] = c
            encontrado = True
            break
    
    if encontrado:
        repositories.sobrescrever_arquivo(consultas)
        
    return encontrado


def remover_agendamento(id_alvo: str) -> bool:
    """Remove uma consulta baseada no ID.
    
    Returns:
        bool: True se removeu, False se não encontrou.

    """
    id_formatado = _normalizar_id(id_alvo)
    consultas = repositories.listar_todas()
    nova_lista = [c for c in consultas if c.id_consulta != id_formatado]
    
    if len(consultas) != len(nova_lista):
        repositories.sobrescrever_arquivo(nova_lista)
        return True
    return False