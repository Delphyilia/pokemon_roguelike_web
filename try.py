def int_input(prompt):
    while True:
        i = input(prompt)
        if i.isdecimal():
            i = int(i)
            break
        print(f"{i}は数値である必要があります")
    return i

idx = 1
while True:
    while idx == 1:
        n = int_input(":")
        if n == 3:
            idx = 2
    
    while idx == 2:
        print("ok")
        exit()
