def Dividers(n):
    divs = ""
    for i in range(n):
        if n % (i+1) == 0:
            divs += str(i + 1) + " "
    return(divs)

#print(Dividers(int(input('Enter number: '))))