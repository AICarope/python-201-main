#functions
def sayhello(Robot):
    return f"hello {Robot}"
Robots = ['CP66', 'R2D2', 'C3PO']

for Robot in Robots:
    if Robot == 'R2D2':
        print('R2D2 has been found')
        break
    
    print(sayhello(Robot))