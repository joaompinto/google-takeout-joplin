#!/usr/enbv python
# -*- coding: utf-8 -*-

from pathlib import Path
import typer
from .joplin import create_folder, create_note
import json

def get_all_json_files(path: str):
    content_list = []
    for file in Path(path).glob("*.json"):
        with open(file, "r") as f:
            content = f.read()
            content_list.append(json.loads(content))
    return content_list

def main(takeout_keep_path: str):
    folder = create_folder("Google Keep Import")
    for note in get_all_json_files(takeout_keep_path):
        if not 'textContent' in note:
            print("Skipping note", note)
            continue
        print("Creating note", note)
        create_note(note, folder)

if __name__ == "__main__":
    typer.run(main)