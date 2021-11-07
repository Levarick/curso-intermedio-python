def read():
    numbers = []
    with open("./files/numbers.txt", "r", encoding="UTF-8") as file:
        for line in file: 
            numbers.append(int(line))
    print(numbers)

def write():
    names = ["Dioney", "Eloy", "Crucito", "Orlando", "Ricardo"]
    with open("./files/names.txt", "w", encoding="UTF-8") as file:
        for name in names: 
            file.write(name + "\n")

def run():
    read()



if __name__  == '__main__':
    write()
