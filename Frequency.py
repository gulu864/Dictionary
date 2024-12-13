New_dict={"S":3,"R":10,"Re":9,"A":10}
print(New_dict)
val = 10 
count = 0
for i in New_dict:
    if New_dict[i] == val:
        count = count + 1
print("The number of times the value ", val, "is repeating :", count)