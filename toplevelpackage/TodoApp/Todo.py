# pylint: disable=missing-docstring

import json
from datetime import datetime

todo = []
path = "Opdracht2/Python/toplevelpackage/TodoApp/lijst.json"

def updateFile():
    with open(path, "w") as bestand:
        json.dump(todo, bestand)
    bestand.close()

def openFile():
    with open(path, "r") as bestand:
        S = json.load(bestand)
        for item in S:
            todo.append(item)
            print(item)
    bestand.close()

def addItem(item):
    now = datetime.now()
    todo.append([item , now.strftime("%d/%m/%Y - %H:%M:%S")])
    updateFile()

def deleteItem(item):
    todo.remove(item)
    updateFile()

def showList():
    print("Todo List:")
    for item in todo:
        print(f"- {item[0]}, {item[1]}")

    input("")
    
def clearList():
    todo.clear()
    updateFile()
