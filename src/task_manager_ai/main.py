import time

from .core.core import main_menu


def ejecutar_programa():
    print("--- Iniciando ---")
    time.sleep(1)
    main_menu()
    print("--- Saliendo ---")
    time.sleep(1)


if __name__ == "__main__":
    ejecutar_programa()
