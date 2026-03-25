"""
Crear clase nota con id, titulo, contenido, fecha de creación y fecha de modificación
"""

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
