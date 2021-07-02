#! /usr/bin/python3.9

num_1 = int(input(""))
Val = 0
Val_Set = []
if 1 <= num_1 <= 20:
    while num_1-1 >= Val:
        Val_Set.append(Val)
        Val += 1
for SqVal in Val_Set:
    print(SqVal*SqVal)
