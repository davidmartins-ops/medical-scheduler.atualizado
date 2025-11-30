"""Módulo de Entidades do Sistema de Agendamento de Consultas."""

from dataclasses import dataclass
from app.metadata import SEPARADOR_CSV

@dataclass
class Consulta:
    """Representa uma consulta médica agendada."""

    id_consulta: str
    nome_paciente: str
    nome_medico: str
    data_consulta: str
    horario_consulta: str

    def to_csv(self) -> str:
        """Converte o objeto para o formato salvo no TXT usando o separador padrão."""

        return (f"{self.id_consulta}{SEPARADOR_CSV}"
                f"{self.nome_paciente}{SEPARADOR_CSV}"
                f"{self.nome_medico}{SEPARADOR_CSV}"
                f"{self.data_consulta}{SEPARADOR_CSV}"
                f"{self.horario_consulta}")

    @staticmethod
    def from_csv(line: str) -> 'Consulta':
        """Cria um objeto a partir de uma linha do TXT."""
        parts = line.strip().split(SEPARADOR_CSV)
        if len(parts) < 5:
            raise ValueError(f"Linha inválida ou corrompida: {line}")

        return Consulta(
            id_consulta=parts[0],
            nome_paciente=parts[1],
            nome_medico=parts[2],
            data_consulta=parts[3],
            horario_consulta=parts[4]
        )
