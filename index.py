import os #imported os module

#make dir if not exist
try:
    os.makedirs('tables')
except OSError as e:
    if e.errno != FileExistsError:
        pass


a = input(">>> Choose the mode of table : \n 1.single \n 2.Multiple \n").lower()



if a == "1" or a == "single":
    b = int(input("Of which table you want?: "))
    with open(f"tables/Multiplication_table_of_{b}.txt" , 'w') as f:
        for i in range(1 ,11):
            f.write(f"{b} x {i} = {b*i}")
            if i != 10:
                    f.write("\n") 
    print(f"Mutiplication table of {b} was successfully saved in tables folder")




if a == "2" or a == "multiple":
    b = int(input("From where the table starts?: "))
    c = int(input("Where the table ends?: "))
    c = c + 1
    for i in range(b , c):
        with open(f"tables/Multiplication_table_of_{i}.txt", 'w') as f:
            for j in range(1,11):
                f.write(f"{i} x {j} = {i*j}")
                if j != 10:
                    f.write("\n") 


    c = c -1
    print(f"Mutiplication table from {b} to {c} was successfully saved in tables folder")