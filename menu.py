import os
import os.path
def A1():
    print("Выберите функцию:")
    print("1 - работа с файлом")
    print("2 - работа с папкой")
    print("3 - выйти")
def A2():
    print("Выберите функцию:")
    print(" 1 - удалить файл")
    print(" 2 - переименовать файл")
    print(" 3 - добавить текст в файл")
    print(" 4 - переписать текст файла")
    print(" 5 - возратиться в Меню")
def A3():
    print("Выберите функцию:")
    print(" 1 - переименовать папку")
    print(" 2 - количество файлов в папке")
    print(" 3 - количество папок")
    print(" 4 - список папок")
    print(" 5 - добавить файл в папку")
    print(" 6 - добавить папку")
    print(" 7 - возратиться в Меню")
def Menu():
    A1()
    a=int(input())
    if a==1:
        B1()
    elif a==2:
        B2()
    elif a==0:
        return 0
def B1():
    A2()
    n = int(input())
    if n == 1:
        name = input("Название файла:") + ".txt"
        try:
            os.remove(name)
        except FileNotFoundError:
            print("Файл не найден")
        else :print("Файл удалён")
        B1()
    elif n == 2:
        name = input("Название старого файла: ")+".txt"
        Newname = input("Название нового файла: ")+".txt"
        os.rename(name, Newname)
        print("Название файла изменён")
        B1()
    elif n == 3:
        name=input("Название файла: ")+".txt"
        Open=open(name, "at")
        content = input("Содержание текста: ")
        Open.write(content)
        Open.close()
        B1()
    elif n == 4:
        name=input("Название файла: ")+".txt"
        Open=open(name, "wt")
        content = input("Содержание текста:")
        Open.write(content)
        Open.close()
        B1()
    if n == 5:
        Menu()
def B2():
    A3()
    n = int(input())
    if n == 1:
        name = input("Название старой папки:")
        Nname = input("Название новой папки:")
        try:
            os.rename(name, Nname)
        except FileNotFoundError:
            print("Папка не найдена")
        else :
            print("Название папки изменён")
        B2()
    elif n == 2:
        num = 0
        for f in os.listdir():
            File = os.path.join(f)
            if os.path.isfile(File):
                num+=1
        print("Количество файлов в папке:", num)
        B2()
    elif n == 3:
        num = 0
        for f in os.listdir():
            Dir = os.path.join(f)
            if os.path.isdir(Dir):
                num+=1
        print("Количество папок:", num)
        B2()
    elif n == 4:
        for f in os.listdir():
            print(f)
        B2()
    elif n == 5:
        name = input("Название нового файла: ") + ".txt"
        Open=open(name, "tw")
        Open.close()
        print("Файл создан")
        B2()
    elif n == 6:
        name = input("Название новой папки: ")
        os.mkdir(name)
        print("Папка создана")
        B2()
    elif n == 7:
        Menu()
Menu()