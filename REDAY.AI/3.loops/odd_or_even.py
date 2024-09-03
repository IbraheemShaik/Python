even = []
odd = []

for x in range(1, 51):
    if x % 2 == 0:
        even.append(x) 
    else:
        odd.append(x) 

print("Even:", even)
print("Odd:", odd)
