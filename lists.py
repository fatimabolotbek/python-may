cities = ['New York', 'Los Angeles', 'Chicago', 'Huston', 'Boston']
#print(cities[:-2])
# for city in cities: 
#     print(city)

#cities.insert(-3, "Phoenix")

#print(cities)
# for index in range(len(cities)):
#     print("Corent index:", index, '| Current city: ', cities[index])
    
    
    # set a emty list 
    
# cities = []
# while len(cities) <= 5:
#     usr_input = input("Pleas anter city name:")
#     if usr_input in cities:
#         print("City alredy exist", usr_input)
#         break
# else:
#         cities.append(usr_input)  




cities[0], cities[4], cities[0]
# print(cities)


# a, b = cities[4], cities[0]
# print(cities)


spendings = [32.45, 18.65, 23.45, 78.32, 5.23]
sum = 0.0
for spending in spendings:
    sum += spending
#print("Many spendt:", sum)    
spendings.sort(reverse=True)
#print(spendings)
words = ["banana", "appl", "Chery", "Fatima"]
words.sort()
#print(words)
# in = followed by the list and the element you want to check.  

# copyinfg list 

original_list = [1, 2, 3, 4, 5]
new_list = original_list.copy()
#print(new_list)
new_list.append(6)
print(original_list, new_list)