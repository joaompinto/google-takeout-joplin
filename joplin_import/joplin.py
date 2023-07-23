from .http import post

def create_folder(name: str):
    """Create a folder in Joplin"""
    return post("folders/", payload={"title": name})

def create_note(note, folder):
    """ Create a note in a folder """
    payload = {
                "parent_id": folder["id"],
                "title": note["title"],
                "body": note["textContent"],
                "created_time": note["createdTimestampUsec"],
                "updated_time": note["userEditedTimestampUsec"],
        }
    return post("notes/", payload=payload)
