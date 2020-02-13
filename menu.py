import dev
import incl


if __name__ == '__main__':
    start()

def start(items):
    db_items = items

    exit = False
    while not exit:
        print("==========Incluid Manager v0.1.0=========")
        choice = int(input("1. Show people \n2. Add new incluid \n3. Delete incluid \n4. With file  \n0. Exit \n"))
        print("User choice =>", choice)
        if choice == 1:
            show_items(db_items)
        elif choice == 2:
            add_incl(db_items)
        elif choice == 3:
            delete_incl(db_items)
        elif choice == 4:
            file_params(db_items)
        elif choice == 0:
            exit = True
        else:
            print("Read menu and check N !!!")

def show_items(items):
    print(items)


def add_incl(items):
    name = input("Enter name :")
    surname = input("Enter surname :")
    age = int(input("Enter age :"))
    posada = input("Enter posada :")
    price = int(input("Enter price :"))
    item = {"name": name,
            "surname": surname,
            "age": age,
            "posada": posada,
            "price": price
            }
    items.append(item)


def delete_incl(items):
    delete_id = input("Enter name phone :")
        items.pop[delete_id]


def file_params(items):
    exit = False
    while not exit:
        print("==========FILE MANAGER=========")
        choice = int(input("1. Read \n2. Wride \n3. Append  \n0. Exit \n"))
        print("User choice =>", choice)
        if choice == 1:
            myfile = open("infoAll.txt", "r")
            myfile.close()
        elif choice == 2:
            myfile = open("infoAll.txt", "w")
            myfile.close()
        elif choice == 3:
            myfile = open("infoAll.txt", "a")
            myfile.close()
        else:
            print("Read menu and check N !!!")



# Krasche zapisatt kak v metanik v konce : 

# with open("hello.txt", "w") as somefile:
#     somefile.write("hello world")


# id += 1 nada sdelatt