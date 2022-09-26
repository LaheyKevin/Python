import TodoApp.Todo as Todo
import os

def Menu():
    os.system("cls")
    print("################")
    print("      Todo")
    print("1. Bekijk lijst")
    print("2. Voeg item toe")
    print("3. Verwijder item")
    print("4. Maak lijst leeg")
    print("################")
    invoer = input("Geef een nummer in: ")
    match invoer:
        case "1":
            Todo.showList()
        case "2":
            print("Geef het item op dat u wilt toevoegen")
            Todo.addItem(input())
        case "3":
            print("Geef het item op dat u wilt verwijderen")
            Todo.deleteItem(input())
        case "4":
            Todo.clearList()
    os.system("cls")
    Menu()

def main():
    Todo.openFile()
    Menu()

if __name__ == "__main__":
    main()