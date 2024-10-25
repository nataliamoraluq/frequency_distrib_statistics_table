tupla1 = (30, 46, 71, 63, 95)
tupla2 = (30, 46, 72, 63, 95)
for x in tupla1:
    for y in tupla2:
        if(x==y):
            tupla1.count('x')
            #print(x)
            #print(tupla1.count('x'))
            #print(enumerate(tupla1))
        else:
            print('0')