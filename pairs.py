# Finding pairs whose sum amounts to 10
values = [2,7,1,4,3,6]
count = 0
for i in range(0,len(values)):
    for j in range(i+1,len(values)):
        if values[i] + values[j] == 10:
                count+=1
print(f"The number of pairs that add up to 10 are {count}")

