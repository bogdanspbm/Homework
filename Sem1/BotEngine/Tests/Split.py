arr1 =  'My name is %name% and i am %years% it"s 15 % of students in world'
arr2 = 'My name is Bogdan and i am 15 it"s 15 % of students in world'


def find_overlap(first, second):
        last_right = ''
    #try:
        for i in range(len(first)):
            test1, test2 = first[i:], second[:len(first) - i]
            if test1 == test2:
                last_right = test1
        return last_right
    #except:
        #return last_right


def try_to_write_var(myinput, funcinput):
    splits = (funcinput + '.').split('%')

    myinp = myinput + '.'

    first_eq = []
    sec_eq = []

    new_keys = []
    new_vals = []

    flag = 0

    for i in range(len(splits) - 2):
        if i % 2 == 0:
            a = myinp.split(splits[i + 2])
            b = myinp.split(splits[i])
            val = find_overlap(a[0], b[1])
            if val != '':
                new_keys.append(splits[i + 1])
                new_vals.append(val)

    for i in range(len(splits)):
        if i == len(splits):
            break
        if i % 2 == 1:
            splits.remove(splits[i])

    for val in new_vals:
        myinp.replace(val, '%')

    myinp = myinp.split('%')

    if len(myinp) == len(splits):
        for i in range(len(myinp)):
            if myinp[i] != splits[i]:
                flag = 1
    else:
        flag = 1

    if flag == 0:
        for i in range(len(new_keys)):
            print(new_vals[i])
        return 1
    return 0

try_to_write_var(arr2,arr1)