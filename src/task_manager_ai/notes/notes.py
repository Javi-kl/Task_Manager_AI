import json
from datetime import datetime


class Note:
    def __init__(self, id: int, title: str, content: str):
        self.id = id
        self.title = title
        self.content = content
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def update_content(self, new_content: str):
        self.content = new_content
        self.updated_at = datetime.now()

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }


class NoteManager:
    def __init__(self):
        self.file_path = "notes.json"
        self.next_id = self._calculate_next_id()

    def _calculate_next_id(self):
        notes_list_extracted = self.extract_notes()
        if not notes_list_extracted:
            return 1
        return max(note["id"] for note in notes_list_extracted) + 1

    def extract_notes(self):
        with open(self.file_path, "r") as file:
            notes = json.load(file)
            return notes

    def save_note(self, notes):
        with open(self.file_path, "w") as file:
            json.dump(notes, file, indent=4)

    def verify_id_existence(self, note_id: int) -> bool:
        notes_list_extracted = self.extract_notes()
        for note in notes_list_extracted:
            if note["id"] == note_id:
                return True
        return False

    def create_note(self, title: str, content: str) -> Note:
        note = Note(self.next_id, title, content)
        notes_list_extracted = self.extract_notes()
        notes_list_extracted.append(note.to_dict())
        self.save_note(notes_list_extracted)
        return note

    def show_full_note(self, title: str) -> str:
        notes_list_extracted = self.extract_notes()
        for note in notes_list_extracted:
            if note["title"] == title:
                return (
                    f"  [{note['id']}] {note['title']}\n"
                    f"   {note['content']}\n"
                    f"   Creada: {datetime.fromisoformat(note['created_at']).strftime('%d/%m/%Y %H:%M')}"
                )

    def edit_note(self, note_id: int, new_content: str) -> bool:
        notes_list_extracted = self.extract_notes()
        for note in notes_list_extracted:
            if note["id"] == note_id:
                note["content"] = new_content
                note["updated_at"] = datetime.now().isoformat()
                self.save_note(notes_list_extracted)
                return True
        return False

    def delete_note(self, note_id: int) -> bool:
        notes_list_extracted = self.extract_notes()
        for i, note in enumerate(notes_list_extracted):
            if note["id"] == note_id:
                del notes_list_extracted[i]
                self.save_note(notes_list_extracted)
                return True
        return False
