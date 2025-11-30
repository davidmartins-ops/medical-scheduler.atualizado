"""modulo principal do sistema de agendamentos."""

from app.ui import iniciar_menu

if __name__ == "__main__":
    try:
        iniciar_menu()
    except KeyboardInterrupt:
        print("\n\nOperação interrompida pelo usuário.")
