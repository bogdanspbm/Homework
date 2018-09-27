def Dividers(n):
    if n < 0:
        n *= -1
    divs = ""
    for i in range(n):
        if n % (i+1) == 0:
            divs += str(i + 1) + " " + str((i+1) * -1) + " "
    return(divs)

#print(Dividers(int(input('Enter number: '))))