#new_list = [expression  for item in iterable]
squares = [i**2 for i in range (1, 11) if i % 2 == 0]
print(squares)
#for i in range(3, 10):
    #print(i)
squars = []  
for i in range(1, 11):
    if i % 2 == 0:
        squars.append(i**2)
print(squars)       