arr1 =  'My name is %name% and i am %years% it"s 15 % of students in world'
arr2 = 'My name is Bogdan and i am 15 it"s 15 % of students in world'


def try_to_write_var(self, myinput, funcinput):
    splits = funcinput + '.'.split('%')

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
            val = self.find_overlap(a, b)
            if val != '':
                new_keys.append(split[i + 1])
                new_vals.append(val)

    for i in range(len(splits)):
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
            self.add_global_var(new_keys[i], new_vals[i])
        return 1
    return 0