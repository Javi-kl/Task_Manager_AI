from ..notes.notes import NoteManager
from .menu_options import ShowOptions

note_manager = NoteManager()


def main_menu():
    print("\n--- Bienvenido ---")
    while True:
        try:
            option = ShowOptions.main_menu_options()
        except ValueError as e:
            print(f"Error: {e}")
            continue

        match option:
            case "1":
                title = input("Introduce el título de la nota: ")
                content = input("Introduce el contenido de la nota: ")
                note = note_manager.create_note(title, content)
                print(f"Nota creada con ID: {note.id}")

            case "2":
                notes_list_extracted = note_manager.extract_notes()
                if len(notes_list_extracted) == 0:
                    print("No hay notas disponibles.")
                else:
                    notes_menu()

            case "3":
                print("Funcionalidad de asistente IA aún no implementada.")
            case "4":
                break


def notes_menu():
    print("\nNotas actuales: ")
    for note in note_manager.extract_notes():
        print(f"ID: {note['id']} - Título: {note['title']}")

    try:
        option_notes = ShowOptions.notes_submenu()
    except ValueError as e:
        print(f"Error: {e}")
        return

    if option_notes == "4":
        print("\nVolviendo al menú principal")
        return

    elif option_notes == "1":
        id_check = input("\nIntroduce el ID de la nota: ")
        try:
            note_manager.verify_id_existence(int(id_check))

        except ValueError as e:
            print(f"Error: {e}")
            print("Volviendo a menú")
            return

        try:
            print(f"\nNota encontrada {id_check}")
            option_existing_notes = ShowOptions.submenu_existing_notes()
        except ValueError as e:
            print(f"Error: {e}")
            return

        match option_existing_notes:
            case "1":
                print("\nLeyendo nota...")
                print(note_manager.show_full_note(id_check))

            case "2":
                print(f"\nModificando nota: {id_check}")
                new_content = input("Introduce el nuevo contenido de la nota: ")
                note_manager.edit_note(int(id_check), new_content)

            case "3":
                print(f"\nEliminando nota: {id_check}")
                note_manager.delete_note(int(id_check))

            case "4":
                print("\nVolviendo al menú principal")
                return
