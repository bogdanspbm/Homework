import datetime as time


print(exec('bool(19 == 19)'))

print(bool('19 == 19'))

if exec('19 == 19'):
    print('ok')
else:
    print('bad')


print(time.datetime.weekday(time.datetime.now()))
print('here')