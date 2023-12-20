list = [1, 22, 3, 5, 22]
new = []
for element in list:
    print(element)
    element = element + 1
    print(element)
    new.append(element)

print(new)
