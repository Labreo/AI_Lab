print('''
    Rule 1:Fill 4 gallon jug
    Rule 2:Fill 3 gallon jug
    Rule 3:Empty 4 gallon jug
    Rule 4:Empty 3 gallon jug
    Rule 5:Empty 4 gallon into 3 gallon till it is full
    Rule 6:Empty 3 gallon jug into 4 gallon till it is full''')

jugA = 0
jugB = 0
jugAF = int(input('Enter Goal state of 3 gallon jug: '))
jugBF = int(input('Enter Goal state of 4 gallon jug: '))

print("|   |  |   |")
print(f"| {jugA} |  | {jugB} |")
print("|___|  |___|")
print('3 gallon jug',' 4 gallon jug')

while jugA!=jugAF or jugB!=jugBF:
    rule = int(input('Enter the rule:'))
    
    if(rule==1):
        if(jugB<4):
            jugB=4
            print('|   |',' |   |')
            print('|',jugA,'|  |',jugB,'|')
            print('|___|',' |___|')
        else:
            print('4 gallon jug is already full')
            
    elif(rule==2):
        if(jugA<3):
            jugA=3
            print('| |',' | |')
            print('|',jugA,'| |',jugB,'|')
            print('|___|',' |___|')
        else:
            print('3 gallon jug is full')
            
    elif(rule==3):
        if(jugB>0):
            jugB=0
            print('| |',' | |')
            print('|',jugA,'| |',jugB,'|')
            print('|___|',' |___|')
        else:
            print('4 gallon jug is already empty')

    elif(rule==4):
        if(jugA>0):
            jugA=0
            print('| |',' | |')
            print('|',jugA,'| |',jugB,'|')
            print('|___|',' |___|')
        else:
            print('3 gallon jug is already empty')

    elif(rule==5):
        if(jugB!=0):
            if(jugA<3):
                transfer = min(jugB, 3 - jugA)
                jugA += transfer
                jugB -= transfer
                print('| |',' | |')
                print('|',jugA,'| |',jugB,'|')
                print('|___|',' |___|')
            else:
                print('3 gallon jug is already full')
        else:
            print('4 gallon jug is empty')
            print('| |',' | |')
            print('|',jugA,'| |',jugB,'|')
            print('|___|',' |___|')
            
    elif(rule == 6):
        if(jugA != 0):
            if(jugB <4):
                transfer = min(jugA, 4 - jugB)
                jugB += transfer
                jugA -= transfer
                print('| |',' | |')
                print('|',jugA,'| |',jugB,'|')
                print('|___|',' |___|')
            else:
                print("4 gallon jug is already full")
        else:
            print("3 gallon jub is already empty")
            print('| |',' | |')
            print('|',jugA,'| |',jugB,'|')
            print('|___|',' |___|')
                     
    else:
        print('Enter valid rule')
        
print('Final state achieved!')
print('| |',' | |')
print('|',jugAF,'| |',jugBF,'|')
print('|___|',' |___|')
print('3 gallon jug',' 4 gallon jug')