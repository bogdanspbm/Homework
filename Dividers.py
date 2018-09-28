def Dividers(n):
    if n < 0:
        n *= -1
    divs = []
    for i in range(n):
        if n % (i+1) == 0:
            divs.append(i+1)
            divs.append(-1 * (i+1))
    return(divs)

#print(Dividers(int(input('Enter number: '))))