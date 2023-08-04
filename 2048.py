import random

def up(x):
    for i in range(0,4):
        for j in range(0,4):
            if i != 3:   
                    x[i][j]= x[i][j]+x[i+1][j]
                    x[i+1][j]=0
            else :
                x[i][j]=0
    return x
def down(x):
    for i in range(-1, -5, -1):
        for j in range(-1, -5, -1):
            if i != -4:
                x[i][j] = x[i][j] + x[i-1][j]
                x[i-1][j] = 0

            else:
                x[i][j]=0
    return x
def left(x):
    for i in range(0,4):
        for j in range(0,4):
            if j != 3:
                x[i][j]= x[i][j]+x[i][j+1]
                x[i][j+1]=0
            else:
                x[i][j]=0
    return x
def right(x):
    for i in range(-1, -5, -1):
        for j in range(-1, -5, -1):
            if j != -4:
                x[i][j] = x[i][j] + x[i][j-1]
                x[i][j-1] = 0
            else:
                x[i][j]=0
    return x
def table_maker():
    return [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    
def int_maker(x):
    y = random.choice([2,4])
    i = random.randint(0,3)
    j = random.randint(0,3)
    if x[i][j]!=0:
        while True :   
            i = random.randint(0,3)
            j = random.randint(0,3)
            if x[i][j]==0:
                break
    x[i][j]=y
    return x
def gameloop():
    table = table_maker()
    table = int_maker(table)
    table = int_maker(table)
    table = int_maker(table)
    table = int_maker(table)

    print(table)
    for row in table:
        for element in row:
            print(element, end="  ") 
        print()  
    while True:
        move = input("Enter yor move by (W/S/A/D) or Q for quit").lower()
        if move == "w":
            table = up(table)
            for row in table:
                for element in row:
                    print(element, end="  ") 
                print()
            table = int_maker(table)  
        elif move == "s":
            table = down(table)
            for row in table:
                for element in row:
                    print(element, end="  ") 
                print()  
            table = int_maker(table)
        elif move == "a":
            table = left(table)
            for row in table:
                for element in row:
                    print(element, end="  ") 
                print()  
            table = int_maker(table)
        elif move == "d":
            table = right(table)
            for row in table:
                for element in row:
                    print(element, end="  ") 
                print()  
            table = int_maker(table)
        elif move == "q" :
            break
        else :
            print("not valid")

if __name__ == "__main__":
    gameloop()
