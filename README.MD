# 🏥 Sistema de Agendamento de Consultas Médicas

Um sistema moderno e eficiente para gerenciamento de consultas em clínicas médicas, desenvolvido em Python com arquitetura modular e aderência total aos padrões PEP 8.

---

## 📋 Sobre o Projeto

Este sistema foi projetado para resolver a ineficiência de agendamentos manuais em clínicas médicas. Permite gerenciamento digital, rápido e seguro de consultas, utilizando persistência em arquivo de texto plano (`.txt`) que simula um banco de dados.

O código segue estritamente os padrões da **PEP 8** e utiliza uma **Arquitetura Modular Procedural**, separando claramente as responsabilidades de interface, regra de negócio e acesso a dados.

### ✨ Diferencial

Ao invés de utilizar classes desnecessárias para a lógica, o projeto adota **Módulos Python** para organização, mantendo Classes apenas para a Entidade de Dados, resultando em código mais limpo e eficiente.

---

## 🚀 Funcionalidades

| Funcionalidade | Descrição |
|---|---|
| 📝 **Cadastrar Consulta** | Validação automática de datas e geração sequencial de IDs |
| 📊 **Listar Consultas** | Visualização tabular organizada de todos os agendamentos |
| ✏️ **Atualizar Dados** | Alteração de paciente, médico ou horário com busca inteligente por ID |
| 🗑️ **Excluir Consulta** | Remoção segura de registros com confirmação |
| 🔍 **Pesquisar** | Filtro avançado por nome do paciente, médico ou data específica |
| 💾 **Persistência** | Todos os dados salvos automaticamente em `data/repositorio.txt` |

### 🔄 Busca Inteligente
Digite apenas "1" e o sistema encontra automaticamente registros como "Cons01", facilitando a navegação.

---

## 🏗️ Arquitetura do Projeto

O projeto segue uma arquitetura modular bem definida:

```
projeto_agendamento/
│
├── app/
│   ├── metadata.py      # 🔧 Configurações globais (Constantes, Caminhos)
│   ├── entities.py      # 🗂️ Definição da Classe de Dados (Consulta)
│   ├── repositories.py  # 💾 Camada de Acesso a Dados (Leitura/Escrita)
│   ├── services.py      # ⚙️ Camada de Regra de Negócio e Validações
│   └── ui.py            # 🖥️ Camada de Apresentação (Menus e Prints)
│
├── data/
│   └── repositorio.txt  # 📄 Base de dados em texto
│
├── main.py              # 🚀 Ponto de entrada da aplicação
├── requirements.txt     # 📦 Dependências do projeto
└── README.md            # 📖 Documentação
```

### 📐 Camadas de Arquitetura

- **Metadata**: Configurações centralizadas e constantes do sistema
- **Entities**: Definição estruturada da entidade Consulta
- **Repositories**: Operações de leitura e escrita em arquivo
- **Services**: Validações e lógica de negócio
- **UI**: Interface com o usuário (menus e exibição)

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x** - Linguagem principal
- **Tabulate** - Formatação de tabelas no console
- **Dataclasses** - Definição estruturada de entidades
- **Git** - Controle de versão

---

## 📦 Como Rodar o Projeto

### ✅ Pré-requisitos

- Python 3.8 ou superior instalado
- Git (para clonar o repositório)
- Opcional: Git Bash ou terminal compatível

### 🔧 Passo a Passo

#### 1. Clone o repositório

```bash
git clone https://github.com/davidmartins-ops/medical-scheduler.atualizado.git 
cd  C:\Users\giorg\OneDrive\Área de Trabalho\sistema_agendamentos
```

#### 2. Crie um ambiente virtual (recomendado)

**Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

#### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

#### 4. Execute a aplicação

```bash
python main.py
```

A aplicação abrirá um menu interativo no terminal. Siga as instruções na tela para usar o sistema.

---

## ⚙️ Configuração (Metadados)

O comportamento do sistema pode ser personalizado através do arquivo `app/metadata.py`. Você pode configurar:

```python
# Exemplo de configurações disponíveis
DATABASE_FILE = "data/repositorio.txt"      # Nome do arquivo de banco de dados
SEPARATOR = ";"                              # Separador do arquivo (`,` ou `;`)
DATE_FORMAT = "%d/%m/%Y"                     # Formato de data (BR ou ISO)
TIME_FORMAT = "%H:%M"                        # Formato de horário
```

### 🔄 Alterando Configurações

1. Abra `app/metadata.py`
2. Modifique os valores conforme necessário
3. Salve o arquivo
4. Execute novamente a aplicação

---

## 📖 Guia de Uso

### Menu Principal

```
════════════════════════════════════════
   SISTEMA DE AGENDAMENTO MÉDICO
════════════════════════════════════════
1. Cadastrar nova consulta
2. Listar todas as consultas
3. Atualizar consulta
4. Excluir consulta
5. Pesquisar consultas
0. Sair

Escolha uma opção: 
```

### Exemplo de Uso

#### Cadastrando uma Consulta
```
Paciente: João Silva Santos
Médico: Dr. Carlos Mendes
Data (DD/MM/YYYY): 25/12/2024
Horário (HH:MM): 14:30

✓ Consulta cadastrada com sucesso! ID: Cons001
```

#### Listando Consultas
```
╔─────────┬──────────────────┬─────────────────┬────────────┬─────────╗
║ ID      ║ Paciente         ║ Médico          ║ Data       ║ Horário ║
╠─────────╬──────────────────╬─────────────────╬────────────╬─────────╣
║ Cons001 ║ João Silva Santos║ Dr. Carlos      ║ 25/12/2024 ║ 14:30   ║
║ Cons002 ║ Maria Oliveira   ║ Dra. Ana Costa  ║ 26/12/2024 ║ 09:00   ║
╚─────────╴──────────────────┴─────────────────┴────────────┴─────────╝
```

---

## 🔒 Validações

O sistema implementa validações em múltiplas camadas:

- ✓ Verificação de data válida e não retroativa
- ✓ Validação de formato de entrada (data, hora)
- ✓ Prevenção de agendamentos duplicados
- ✓ Confirmação antes de exclusão de registros
- ✓ Tratamento de erros de I/O

---

## 📁 Estrutura de Dados

### Arquivo de Repositório (`data/repositorio.txt`)

```
Cons001;João Silva Santos;Dr. Carlos Mendes;25/12/2024;14:30
Cons002;Maria Oliveira;Dra. Ana Costa;26/12/2024;09:00
Cons003;Pedro Costa;Dr. Bruno Silva;27/12/2024;16:00
```

**Formato:** `ID;PACIENTE;MEDICO;DATA;HORARIO`

---

## 🤝 Contribuição

Gostaria de contribuir com o projeto? Siga os passos abaixo:

1. **Fork o projeto**
   ```bash
   # Clique no botão "Fork" no GitHub
   ```

2. **Crie uma Branch para sua Feature**
   ```bash
   git checkout -b feature/NovaFeature
   ```

3. **Faça o Commit das mudanças**
   ```bash
   git commit -m 'Add: NovaFeature com descrição clara'
   ```

4. **Faça o Push para a Branch**
   ```bash
   git push origin feature/NovaFeature
   ```

5. **Abra um Pull Request**
   - Descreva as mudanças realizadas
   - Explique o propósito da feature
   - Aguarde revisão

### 📋 Diretrizes

- Mantenha o código em conformidade com PEP 8
- Adicione comentários explicativos quando necessário
- Teste suas alterações antes de fazer commit
- Use nomes descritivos em commits e branches

---

## 📝 Licença

Este projeto foi desenvolvido para fins **acadêmicos e educacionais**.

---

## 🐛 Reportando Problemas

Encontrou um bug? Abra uma **Issue** descrevendo:

1. O que esperava que acontecesse
2. O que realmente aconteceu
3. Passos para reproduzir o problema
4. Versão do Python e SO utilizados

---

## 👥 Desenvolvedores

Este projeto foi desenvolvido por:

| Nome | Função |
|------|--------|
| **[David Donizeti Martins]** | Desenvolvedor |
| **[Bruna Dayanne Simões Souza]** | Desenvolvedor |
| **[Felipe Riogi Sacamoto]** | Desenvolvedor |
| **[Matheus da Silva Ferreira Souza]** | Desenvolvedor |
| **[Pedro Komatsubara Carbonaro Cruz]** | Desenvolvedor |

---

## 🎓 Referências e Recursos

- [PEP 8 - Python Enhancement Proposal](https://www.python.org/dev/peps/pep-0008/)
- [Dataclasses - Python Documentation](https://docs.python.org/3/library/dataclasses.html)
- [Tabulate - GitHub](https://github.com/astanin/python-tabulate)
- [Clean Code Principles](https://en.wikipedia.org/wiki/Code_smell)

---

## 🙏 Agradecimentos

Agradecemos a todos que contribuem ou utilizam este projeto. Sua participação é fundamental para a melhoria contínua!

---

<div align="center">

**Desenvolvido com ❤️ para fins acadêmicos**

⭐ Se este projeto foi útil, considere dar uma estrela!

</div>
