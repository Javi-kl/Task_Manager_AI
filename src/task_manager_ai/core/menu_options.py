class ShowOptions:
    @staticmethod
    def validate_option(option, valid_options):
        options_formatted = valid_options[0] + "-" + valid_options[-1]
        if option not in valid_options:
            raise ValueError(f"Debes introducir un digito: {options_formatted}")

    @staticmethod
    def main_menu_options():
        print("\n--- Menú principal ---")
        print("1 -> Nueva nota")
        print("2 -> Listar notas")
        print("3 -> asistente IA")
        print("4 -> Salir")
        option = input("-> ")
        ShowOptions.validate_option(option, ["1", "2", "3", "4"])
        return option

    @staticmethod
    def notes_submenu():
        print("1 -> Seleccionar nota por 'ID'")
        print("4 -> Volver atrás")
        option = input("-> ").lower()
        ShowOptions.validate_option(option, ["1", "4"])
        return option

    @staticmethod
    def submenu_existing_notes():
        print("1 -> Leer nota")
        print("2 -> Modificar nota")
        print("3 -> Borrar nota")
        print("4 -> Volver atrás")
        option = input("-> ")
        ShowOptions.validate_option(option, ["1", "2", "3", "4"])
        return option
